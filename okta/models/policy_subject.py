# coding: utf-8

"""
    Okta API

    Allows customers to easily access the Okta API  # noqa: E501

    OpenAPI spec version: 2.9.2
    Contact: devex-public@okta.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

from okta.helpers import to_snake_case

class PolicySubject(object):
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
        'filter': 'str',
        'format': 'list[str]',
        'match_attribute': 'str',
        'match_type': 'PolicySubjectMatchType',
        'user_name_template': 'PolicyUserNameTemplate'
    }

    attribute_map = {
        'filter': 'filter',
        'format': 'format',
        'match_attribute': 'matchAttribute',
        'match_type': 'matchType',
        'user_name_template': 'userNameTemplate'
    }

    def __init__(self, config=None):
        if config is not None:
            config = {to_snake_case(key): value for key, value in config.items()}
            self.set_attributes(**config)

    @classmethod
    def from_kwargs(cls, **kwargs):
        return cls(config=kwargs)

    def set_attributes(self, filter=None, format=None, match_attribute=None, match_type=None, user_name_template=None):  # noqa: E501
        """PolicySubject - a model defined in Swagger"""  # noqa: E501
        self._filter = None
        self._format = None
        self._match_attribute = None
        self._match_type = None
        self._user_name_template = None
        self.discriminator = None
        if filter is not None:
            self.filter = filter
        if format is not None:
            self.format = format
        if match_attribute is not None:
            self.match_attribute = match_attribute
        if match_type is not None:
            self.match_type = match_type
        if user_name_template is not None:
            self.user_name_template = user_name_template

    @property
    def filter(self):
        """Gets the filter of this PolicySubject.  # noqa: E501


        :return: The filter of this PolicySubject.  # noqa: E501
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this PolicySubject.


        :param filter: The filter of this PolicySubject.  # noqa: E501
        :type: str
        """

        self._filter = filter

    @property
    def format(self):
        """Gets the format of this PolicySubject.  # noqa: E501


        :return: The format of this PolicySubject.  # noqa: E501
        :rtype: list[str]
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this PolicySubject.


        :param format: The format of this PolicySubject.  # noqa: E501
        :type: list[str]
        """

        self._format = format

    @property
    def match_attribute(self):
        """Gets the match_attribute of this PolicySubject.  # noqa: E501


        :return: The match_attribute of this PolicySubject.  # noqa: E501
        :rtype: str
        """
        return self._match_attribute

    @match_attribute.setter
    def match_attribute(self, match_attribute):
        """Sets the match_attribute of this PolicySubject.


        :param match_attribute: The match_attribute of this PolicySubject.  # noqa: E501
        :type: str
        """

        self._match_attribute = match_attribute

    @property
    def match_type(self):
        """Gets the match_type of this PolicySubject.  # noqa: E501


        :return: The match_type of this PolicySubject.  # noqa: E501
        :rtype: PolicySubjectMatchType
        """
        return self._match_type

    @match_type.setter
    def match_type(self, match_type):
        """Sets the match_type of this PolicySubject.


        :param match_type: The match_type of this PolicySubject.  # noqa: E501
        :type: PolicySubjectMatchType
        """

        self._match_type = match_type

    @property
    def user_name_template(self):
        """Gets the user_name_template of this PolicySubject.  # noqa: E501


        :return: The user_name_template of this PolicySubject.  # noqa: E501
        :rtype: PolicyUserNameTemplate
        """
        return self._user_name_template

    @user_name_template.setter
    def user_name_template(self, user_name_template):
        """Sets the user_name_template of this PolicySubject.


        :param user_name_template: The user_name_template of this PolicySubject.  # noqa: E501
        :type: PolicyUserNameTemplate
        """

        self._user_name_template = user_name_template

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
        if issubclass(PolicySubject, dict):
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
        if not isinstance(other, PolicySubject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other