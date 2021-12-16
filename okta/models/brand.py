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

class Brand(object):
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
        'links': 'dict(str, object)',
        'agree_to_custom_privacy_policy': 'bool',
        'custom_privacy_policy_url': 'str',
        'id': 'str',
        'remove_powered_by_okta': 'bool'
    }

    attribute_map = {
        'links': '_links',
        'agree_to_custom_privacy_policy': 'agreeToCustomPrivacyPolicy',
        'custom_privacy_policy_url': 'customPrivacyPolicyUrl',
        'id': 'id',
        'remove_powered_by_okta': 'removePoweredByOkta'
    }

    def __init__(self, config=None):
        if config is not None:
            config = {to_snake_case(key): value for key, value in config.items()}
            self.set_attributes(**config)

    @classmethod
    def from_kwargs(cls, **kwargs):
        return cls(config=kwargs)

    def set_attributes(self, links=None, agree_to_custom_privacy_policy=None, custom_privacy_policy_url=None, id=None, remove_powered_by_okta=None):  # noqa: E501
        """Brand - a model defined in Swagger"""  # noqa: E501
        self._links = None
        self._agree_to_custom_privacy_policy = None
        self._custom_privacy_policy_url = None
        self._id = None
        self._remove_powered_by_okta = None
        self.discriminator = None
        if links is not None:
            self.links = links
        if agree_to_custom_privacy_policy is not None:
            self.agree_to_custom_privacy_policy = agree_to_custom_privacy_policy
        if custom_privacy_policy_url is not None:
            self.custom_privacy_policy_url = custom_privacy_policy_url
        if id is not None:
            self.id = id
        if remove_powered_by_okta is not None:
            self.remove_powered_by_okta = remove_powered_by_okta

    @property
    def links(self):
        """Gets the links of this Brand.  # noqa: E501


        :return: The links of this Brand.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Brand.


        :param links: The links of this Brand.  # noqa: E501
        :type: dict(str, object)
        """

        self._links = links

    @property
    def agree_to_custom_privacy_policy(self):
        """Gets the agree_to_custom_privacy_policy of this Brand.  # noqa: E501


        :return: The agree_to_custom_privacy_policy of this Brand.  # noqa: E501
        :rtype: bool
        """
        return self._agree_to_custom_privacy_policy

    @agree_to_custom_privacy_policy.setter
    def agree_to_custom_privacy_policy(self, agree_to_custom_privacy_policy):
        """Sets the agree_to_custom_privacy_policy of this Brand.


        :param agree_to_custom_privacy_policy: The agree_to_custom_privacy_policy of this Brand.  # noqa: E501
        :type: bool
        """

        self._agree_to_custom_privacy_policy = agree_to_custom_privacy_policy

    @property
    def custom_privacy_policy_url(self):
        """Gets the custom_privacy_policy_url of this Brand.  # noqa: E501


        :return: The custom_privacy_policy_url of this Brand.  # noqa: E501
        :rtype: str
        """
        return self._custom_privacy_policy_url

    @custom_privacy_policy_url.setter
    def custom_privacy_policy_url(self, custom_privacy_policy_url):
        """Sets the custom_privacy_policy_url of this Brand.


        :param custom_privacy_policy_url: The custom_privacy_policy_url of this Brand.  # noqa: E501
        :type: str
        """

        self._custom_privacy_policy_url = custom_privacy_policy_url

    @property
    def id(self):
        """Gets the id of this Brand.  # noqa: E501


        :return: The id of this Brand.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Brand.


        :param id: The id of this Brand.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def remove_powered_by_okta(self):
        """Gets the remove_powered_by_okta of this Brand.  # noqa: E501


        :return: The remove_powered_by_okta of this Brand.  # noqa: E501
        :rtype: bool
        """
        return self._remove_powered_by_okta

    @remove_powered_by_okta.setter
    def remove_powered_by_okta(self, remove_powered_by_okta):
        """Sets the remove_powered_by_okta of this Brand.


        :param remove_powered_by_okta: The remove_powered_by_okta of this Brand.  # noqa: E501
        :type: bool
        """

        self._remove_powered_by_okta = remove_powered_by_okta

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
        if issubclass(Brand, dict):
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
        if not isinstance(other, Brand):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other