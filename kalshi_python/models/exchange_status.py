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

class ExchangeStatus(object):
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
        'exchange_active': 'bool',
        'trading_active': 'bool'
    }

    attribute_map = {
        'exchange_active': 'exchange_active',
        'trading_active': 'trading_active'
    }

    def __init__(self, exchange_active=None, trading_active=None):  # noqa: E501
        """ExchangeStatus - a model defined in Swagger"""  # noqa: E501
        self._exchange_active = None
        self._trading_active = None
        self.discriminator = None
        self.exchange_active = exchange_active
        self.trading_active = trading_active

    @property
    def exchange_active(self):
        """Gets the exchange_active of this ExchangeStatus.  # noqa: E501

        False if the core Kalshi exchange is no longer taking any state changes at all. This includes but is not limited to trading, new users, and transfers. True unless we are under maintenance.  # noqa: E501

        :return: The exchange_active of this ExchangeStatus.  # noqa: E501
        :rtype: bool
        """
        return self._exchange_active

    @exchange_active.setter
    def exchange_active(self, exchange_active):
        """Sets the exchange_active of this ExchangeStatus.

        False if the core Kalshi exchange is no longer taking any state changes at all. This includes but is not limited to trading, new users, and transfers. True unless we are under maintenance.  # noqa: E501

        :param exchange_active: The exchange_active of this ExchangeStatus.  # noqa: E501
        :type: bool
        """
        if exchange_active is None:
            raise ValueError("Invalid value for `exchange_active`, must not be `None`")  # noqa: E501

        self._exchange_active = exchange_active

    @property
    def trading_active(self):
        """Gets the trading_active of this ExchangeStatus.  # noqa: E501

        True if we are currently permitting trading on the exchange. This is true during trading hours and false outside exchange hours. Kalshi reserves the right to pause at any time in case issues are detected.  # noqa: E501

        :return: The trading_active of this ExchangeStatus.  # noqa: E501
        :rtype: bool
        """
        return self._trading_active

    @trading_active.setter
    def trading_active(self, trading_active):
        """Sets the trading_active of this ExchangeStatus.

        True if we are currently permitting trading on the exchange. This is true during trading hours and false outside exchange hours. Kalshi reserves the right to pause at any time in case issues are detected.  # noqa: E501

        :param trading_active: The trading_active of this ExchangeStatus.  # noqa: E501
        :type: bool
        """
        if trading_active is None:
            raise ValueError("Invalid value for `trading_active`, must not be `None`")  # noqa: E501

        self._trading_active = trading_active

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
        if issubclass(ExchangeStatus, dict):
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
        if not isinstance(other, ExchangeStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other