# coding: utf-8

"""
    Kalshi Trade API

    This documentation describes Kalshi's trading API (known as Trade API v2). By using this API, you agree to Kalshi's Developer Agreement (https://kalshi.com/developer-agreement).  # noqa: E501

    OpenAPI spec version: 2.0.0
    Contact: support@kalshi.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class GetPositionsResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'cursor': 'str',
        'event_positions': 'list[EventPosition]',
        'market_positions': 'list[MarketPosition]'
    }

    attribute_map = {
        'cursor': 'cursor',
        'event_positions': 'event_positions',
        'market_positions': 'market_positions'
    }

    def __init__(self, cursor=None, event_positions=None, market_positions=None):  # noqa: E501
        """GetPositionsResponse - a model defined in Swagger"""  # noqa: E501
        self._cursor = None
        self._event_positions = None
        self._market_positions = None
        self.discriminator = None
        if cursor is not None:
            self.cursor = cursor
        self.event_positions = event_positions
        self.market_positions = market_positions

    @property
    def cursor(self):
        """Gets the cursor of this GetPositionsResponse.  # noqa: E501

        The Cursor represents a pointer to the next page of records in the pagination. Use the value returned here in the cursor query parameter for this end-point to get the next page containing limit records. An empty value of this field indicates there is no next page.  # noqa: E501

        :return: The cursor of this GetPositionsResponse.  # noqa: E501
        :rtype: str
        """
        return self._cursor

    @cursor.setter
    def cursor(self, cursor):
        """Sets the cursor of this GetPositionsResponse.

        The Cursor represents a pointer to the next page of records in the pagination. Use the value returned here in the cursor query parameter for this end-point to get the next page containing limit records. An empty value of this field indicates there is no next page.  # noqa: E501

        :param cursor: The cursor of this GetPositionsResponse.  # noqa: E501
        :type: str
        """

        self._cursor = cursor

    @property
    def event_positions(self):
        """Gets the event_positions of this GetPositionsResponse.  # noqa: E501

        List of event positions.  # noqa: E501

        :return: The event_positions of this GetPositionsResponse.  # noqa: E501
        :rtype: list[EventPosition]
        """
        return self._event_positions

    @event_positions.setter
    def event_positions(self, event_positions):
        """Sets the event_positions of this GetPositionsResponse.

        List of event positions.  # noqa: E501

        :param event_positions: The event_positions of this GetPositionsResponse.  # noqa: E501
        :type: list[EventPosition]
        """
        if event_positions is None:
            raise ValueError("Invalid value for `event_positions`, must not be `None`")  # noqa: E501

        self._event_positions = event_positions

    @property
    def market_positions(self):
        """Gets the market_positions of this GetPositionsResponse.  # noqa: E501

        List of market positions.  # noqa: E501

        :return: The market_positions of this GetPositionsResponse.  # noqa: E501
        :rtype: list[MarketPosition]
        """
        return self._market_positions

    @market_positions.setter
    def market_positions(self, market_positions):
        """Sets the market_positions of this GetPositionsResponse.

        List of market positions.  # noqa: E501

        :param market_positions: The market_positions of this GetPositionsResponse.  # noqa: E501
        :type: list[MarketPosition]
        """
        if market_positions is None:
            raise ValueError("Invalid value for `market_positions`, must not be `None`")  # noqa: E501

        self._market_positions = market_positions

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(GetPositionsResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, GetPositionsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other