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

class LoginResponse(object):
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
        'member_id': 'str',
        'token': 'str'
    }

    attribute_map = {
        'member_id': 'member_id',
        'token': 'token'
    }

    def __init__(self, member_id=None, token=None):  # noqa: E501
        """LoginResponse - a model defined in Swagger"""  # noqa: E501
        self._member_id = None
        self._token = None
        self.discriminator = None
        if member_id is not None:
            self.member_id = member_id
        self.token = token

    @property
    def member_id(self):
        """Gets the member_id of this LoginResponse.  # noqa: E501

        Member's user ID.  # noqa: E501

        :return: The member_id of this LoginResponse.  # noqa: E501
        :rtype: str
        """
        return self._member_id

    @member_id.setter
    def member_id(self, member_id):
        """Sets the member_id of this LoginResponse.

        Member's user ID.  # noqa: E501

        :param member_id: The member_id of this LoginResponse.  # noqa: E501
        :type: str
        """

        self._member_id = member_id

    @property
    def token(self):
        """Gets the token of this LoginResponse.  # noqa: E501

        Access token for a member role session in the API.  # noqa: E501

        :return: The token of this LoginResponse.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this LoginResponse.

        Access token for a member role session in the API.  # noqa: E501

        :param token: The token of this LoginResponse.  # noqa: E501
        :type: str
        """
        if token is None:
            raise ValueError("Invalid value for `token`, must not be `None`")  # noqa: E501

        self._token = token

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
        if issubclass(LoginResponse, dict):
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
        if not isinstance(other, LoginResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other