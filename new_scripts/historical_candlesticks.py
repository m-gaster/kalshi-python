import argparse
import csv
import json
import os
import time
from datetime import datetime
from typing import Dict, List
import requests

EMAIL=""
PASSWORD=""

# Configuration
TRADING_API_URL = "https://trading-api.kalshi.com"
ELECTIONS_API_URL = "https://api.elections.kalshi.com"

ELECTIONS_SERIES_TICKERS_SET = {
    "ADAMS",
    "TIPPINGPOINT",
    "SENATEWI",
    "SENATETX",
    "SENATEPARTYWI",
    "SENATEPARTYTX",
    "SENATEPARTYPA",
    "SENATEPARTYOH",
    "SENATEPARTYNV",
    "SENATEPARTYNE",
    "SENATEPARTYMT",
    "SENATEPARTYMI",
    "SENATEPARTYMD",
    "SENATEPARTYFL",
    "SENATEPARTYAZ",
    "SENATEPARTY",
    "SENATEPA",
    "SENATEOH",
    "SENATENV",
    "SENATENE",
    "SENATEMT",
    "SENATEMOV",
    "SENATEMI",
    "SENATEMD",
    "SENATEFL",
    "SENATEAZ",
    "PRESPARTYSTATEPA",
    "PRESPARTYSTATENV",
    "PRESPARTYSTATENC",
    "PRESPARTYSTATEMI",
    "PRESPARTYSTATEGA",
    "PRESPARTYSTATEAZ",
    "PRESPARTYPA",
    "PRESPARTYNV",
    "PRESPARTYNC",
    "PRESPARTYMI",
    "PRESPARTYGA",
    "PRESPARTYFULL",
    "PRESPARTYAZ",
    "PRESPARTYWI",
    "PRESNOM-R",
    "PRESNOMR",
    "PRESNOM-D",
    "PRESNOMD",
    "PRES",
    "POWER",
    "POPVOTEMOVPA",
    "POPVOTEMOV",
    "POPVOTE",
    "HOUSEPARTYMI07",
    "HOUSEMOV",
    "GOVPARTYNH",
    "GOVPARTYNH",
    "ECMOV",
    "CONTROLS",
    "CONTROLH",
    "CLOSESTSTATE",
    "POPVOTEMOVNV",
    "POPVOTEMOVAZ",
    "POPVOTEMOVMI",
    "POPVOTEMOVWI",
    "POPVOTEMOVNC",
    "POPVOTEMOVGA",
    "PRESPARTYFL",
    "PRESPARTYTX",
    "PRESPARTYOH",
    "PRESPARTYCA",
    "PRESPARTYIL",
    "PRESPARTYNY",
    "PRESPARTYNJ",
    "PRESPARTYVA",
    "PRESPARTYWA",
    "PRESPARTYTN",
    "PRESPARTYMA",
    "PRESPARTYIN",
    "PRESPARTYMO",
    "PRESPARTYMD",
    "PRESPARTYCO",
    "PRESPARTYMN",
    "PRESPARTYSC",
    "PRESPARTYAL",
    "PRESPARTYLA",
    "PRESPARTYKY",
    "PRESPARTYOR",
    "PRESPARTYOK",
    "PRESPARTYCT",
    "PRESPARTYUT",
    "PRESPARTYIA",
    "PRESPARTYAR",
    "PRESPARTYKS",
    "PRESPARTYMS",
    "PRESPARTYNM",
    "PRESPARTYNE",
    "PRESPARTYID",
    "PRESPARTYWV",
    "PRESPARTYHI",
    "PRESPARTYNH",
    "PRESPARTYME",
    "PRESPARTYMT",
    "PRESPARTYRI",
    "PRESPARTYDE",
    "PRESPARTYSD",
    "PRESPARTYND",
    "PRESPARTYAK",
    "PRESPARTYVT",
    "PRESPARTYWY",
    "PRESPARTYNE3",
    "PRESPARTYME2",
    "PRESPARTYNE1",
    "PRESPARTYDC",
    "CABINETMUSK",
    "PRESPARTYME1",
    "CABINETRFK",
    "PRESPARTYNE2",
    "CABINETTULSI",
    "RSENATESEATS",
    "CABINETDIMON",
    "MERGED",
    "ROGANKH",
    "ROGANDJT",
    "PRESINDEXD",
}


def get_series_ticker(market_ticker):
    return market_ticker.split("-")[0]


def login(base_url):
    print("Logging in...")
    resp = requests.post(
        f"{base_url}/trade-api/v2/login",
        json={"email": EMAIL, "password": PASSWORD},
    )
    if resp.status_code == 200:
        return resp.json()["token"]
    else:
        print(f"Login failed with status code: {resp.status_code}")
        return None


class KalshiHistoricalCandlesticksReader:
    def __init__(self, base_url, auth_token):
        self.base_url = base_url
        self.headers = {"Authorization": f"Bearer {auth_token}"}

    def get_markets(self, ticker: str) -> List[str]:
        """Fetch all market tickers for a series or event ticker"""
        parts = ticker.split("-")

        if len(parts) == 1:  # Series ticker
            params = {"series_ticker": ticker}
        elif len(parts) == 2:  # Event ticker
            params = {"event_ticker": ticker}
        else:  # Market ticker
            return [ticker]

        resp = requests.get(
            f"{self.base_url}/trade-api/v2/markets", headers=self.headers, params=params
        )

        if resp.status_code != 200:
            print(f"Error fetching markets: {resp.text}")
            return []

        markets_data = resp.json().get("markets", [])
        return [market["ticker"] for market in markets_data]

    def fetch_candlesticks(
        self, market_ticker: str, start_ts: int, end_ts: int, period_interval: int = 1
    ) -> List[Dict]:
        """Fetch a single batch of candlesticks"""
        series_ticker = get_series_ticker(market_ticker)
        url = f"{self.base_url}/trade-api/v2/series/{series_ticker}/markets/{market_ticker}/candlesticks"
        params = {
            "start_ts": start_ts,
            "end_ts": end_ts,
            "period_interval": period_interval,
        }

        response = requests.get(url, headers=self.headers, params=params)
        if response.status_code != 200:
            print(f"Error Response Body: {response.text}")
            return []

        return response.json().get("candlesticks", [])

    def fetch_all_historical_data(self, market_ticker, end_ts=None, period_interval=1):
        """
        Fetch all historical candlestick data by paginating backwards.

        Args:
            market_ticker: The market identifier
            end_ts: Optional end timestamp (defaults to current time)
            period_interval: Interval in minutes (default 1m)

        Returns:
            List of candlestick data
        """
        # If no end_ts provided, use current time
        if end_ts is None:
            end_ts = int(time.time())

        all_candlesticks = []
        current_end = end_ts
        batch_size = 5000  # Maximum allowed by API
        empty_batch_count = 0  # Track consecutive empty batches

        while True:
            # Calculate start time for this batch
            current_start = current_end - (batch_size * period_interval * 60)

            print(
                f"Fetching data from {datetime.fromtimestamp(current_start)} to {datetime.fromtimestamp(current_end)}"
            )

            # Fetch batch
            batch = self.fetch_candlesticks(
                market_ticker=market_ticker,
                start_ts=current_start,
                end_ts=current_end,
                period_interval=period_interval,
            )

            # Track empty batches
            if not batch:
                empty_batch_count += 1
                if empty_batch_count >= 10:  # Stop after 10 consecutive empty batches
                    break
            else:
                empty_batch_count = 0  # Reset counter if we find data

            # DEDUPLICATION CHECK - Make sure we're not fetching duplicate data
            if all_candlesticks and batch:
                last_batch_ts = batch[-1]["end_period_ts"]
                first_existing_ts = all_candlesticks[0]["end_period_ts"]
                if last_batch_ts >= first_existing_ts:
                    print(f"Warning: Overlap detected. Exiting early.")
                    break

            # Prepend batch to our results (since we're going backwards)
            all_candlesticks = batch + all_candlesticks

            # Update end time for next batch
            current_end = current_start

            # Optional: Add delay to avoid rate limiting
            time.sleep(0.1)

        return all_candlesticks

    def save_to_json(self, data, filename):
        with open(filename, "w") as f:
            json.dump(data, f, indent=2)
        print(f"Data saved to {filename}")

    def save_to_csv(self, data, filename):
        if not data:
            print("No data to save to CSV.")
            return

        flattened_data = []
        for candlestick in data:
            flat_candlestick = {
                "end_period_ts": candlestick["end_period_ts"],
                "yes_bid_open": candlestick["yes_bid"]["open"],
                "yes_bid_low": candlestick["yes_bid"]["low"],
                "yes_bid_high": candlestick["yes_bid"]["high"],
                "yes_bid_close": candlestick["yes_bid"]["close"],
                "yes_ask_open": candlestick["yes_ask"]["open"],
                "yes_ask_low": candlestick["yes_ask"]["low"],
                "yes_ask_high": candlestick["yes_ask"]["high"],
                "yes_ask_close": candlestick["yes_ask"]["close"],
                "price_open": candlestick["price"]["open"],
                "price_low": candlestick["price"]["low"],
                "price_high": candlestick["price"]["high"],
                "price_close": candlestick["price"]["close"],
                "price_mean": candlestick["price"]["mean"],
                "price_previous": candlestick["price"]["previous"],
                "volume": candlestick["volume"],
                "open_interest": candlestick["open_interest"],
            }
            flattened_data.append(flat_candlestick)

        keys = flattened_data[0].keys()
        with open(filename, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(flattened_data)
        print(f"Data saved to {filename}")


def process_market(
    fetcher: KalshiHistoricalCandlesticksReader, market_ticker: str, output_dir: str, end_ts: int = None
):
    """Process a single market's historical data"""
    data = fetcher.fetch_all_historical_data(
        market_ticker=market_ticker,
        end_ts=end_ts,
        period_interval=1,
    )

    if not data:
        print(f"No data found for {market_ticker}")
        return

    first_ts = data[0]["end_period_ts"]
    last_ts = data[-1]["end_period_ts"]
    total_seconds = last_ts - first_ts
    weeks = total_seconds // (7 * 24 * 3600)
    remaining_seconds = total_seconds % (7 * 24 * 3600)
    days = remaining_seconds // (24 * 3600)
    print(
        f"\nData for {market_ticker} spans {weeks} weeks and {days} days (total of {len(data)} candlesticks)"
    )

    # Save data
    json_filename = os.path.join(output_dir, f"{market_ticker}_candlesticks.json")
    csv_filename = os.path.join(output_dir, f"{market_ticker}_candlesticks.csv")
    fetcher.save_to_json(data, json_filename)
    fetcher.save_to_csv(data, csv_filename)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch historical candlestick data for Kalshi markets")
    parser.add_argument("ticker", help="Series ticker, event ticker, or market ticker")
    args = parser.parse_args()

    # Determine base URL
    series_ticker = get_series_ticker(args.ticker)
    base_url = (
        ELECTIONS_API_URL
        if series_ticker in ELECTIONS_SERIES_TICKERS_SET
        or args.ticker.startswith("KX")
        else TRADING_API_URL
    )

    # Initialize fetcher
    auth_token = login(base_url)
    if not auth_token:
        exit(1)
    fetcher = KalshiHistoricalCandlesticksReader(base_url=base_url, auth_token=auth_token)

    # Create output directory
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    # Get all relevant market tickers
    market_tickers = fetcher.get_markets(args.ticker)
    print(f"\nFound {len(market_tickers)} markets to process")

    # Process each market
    for i, market_ticker in enumerate(market_tickers, 1):
        print(f"\nProcessing market {i}/{len(market_tickers)}: {market_ticker}")
        process_market(fetcher, market_ticker, output_dir)