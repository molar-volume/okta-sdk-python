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

class LogEvent(object):
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
        'actor': 'LogActor',
        'authentication_context': 'LogAuthenticationContext',
        'client': 'LogClient',
        'debug_context': 'LogDebugContext',
        'display_message': 'str',
        'event_type': 'str',
        'legacy_event_type': 'str',
        'outcome': 'LogOutcome',
        'published': 'datetime',
        'request': 'LogRequest',
        'security_context': 'LogSecurityContext',
        'severity': 'LogSeverity',
        'target': 'list[LogTarget]',
        'transaction': 'LogTransaction',
        'uuid': 'str',
        'version': 'str'
    }

    attribute_map = {
        'actor': 'actor',
        'authentication_context': 'authenticationContext',
        'client': 'client',
        'debug_context': 'debugContext',
        'display_message': 'displayMessage',
        'event_type': 'eventType',
        'legacy_event_type': 'legacyEventType',
        'outcome': 'outcome',
        'published': 'published',
        'request': 'request',
        'security_context': 'securityContext',
        'severity': 'severity',
        'target': 'target',
        'transaction': 'transaction',
        'uuid': 'uuid',
        'version': 'version'
    }

    def __init__(self, config=None):
        if config is not None:
            config = {to_snake_case(key): value for key, value in config.items()}
            self.set_attributes(**config)

    @classmethod
    def from_kwargs(cls, **kwargs):
        return cls(config=kwargs)

    def set_attributes(self, actor=None, authentication_context=None, client=None, debug_context=None, display_message=None, event_type=None, legacy_event_type=None, outcome=None, published=None, request=None, security_context=None, severity=None, target=None, transaction=None, uuid=None, version=None):  # noqa: E501
        """LogEvent - a model defined in Swagger"""  # noqa: E501
        self._actor = None
        self._authentication_context = None
        self._client = None
        self._debug_context = None
        self._display_message = None
        self._event_type = None
        self._legacy_event_type = None
        self._outcome = None
        self._published = None
        self._request = None
        self._security_context = None
        self._severity = None
        self._target = None
        self._transaction = None
        self._uuid = None
        self._version = None
        self.discriminator = None
        if actor is not None:
            self.actor = actor
        if authentication_context is not None:
            self.authentication_context = authentication_context
        if client is not None:
            self.client = client
        if debug_context is not None:
            self.debug_context = debug_context
        if display_message is not None:
            self.display_message = display_message
        if event_type is not None:
            self.event_type = event_type
        if legacy_event_type is not None:
            self.legacy_event_type = legacy_event_type
        if outcome is not None:
            self.outcome = outcome
        if published is not None:
            self.published = published
        if request is not None:
            self.request = request
        if security_context is not None:
            self.security_context = security_context
        if severity is not None:
            self.severity = severity
        if target is not None:
            self.target = target
        if transaction is not None:
            self.transaction = transaction
        if uuid is not None:
            self.uuid = uuid
        if version is not None:
            self.version = version

    @property
    def actor(self):
        """Gets the actor of this LogEvent.  # noqa: E501


        :return: The actor of this LogEvent.  # noqa: E501
        :rtype: LogActor
        """
        return self._actor

    @actor.setter
    def actor(self, actor):
        """Sets the actor of this LogEvent.


        :param actor: The actor of this LogEvent.  # noqa: E501
        :type: LogActor
        """

        self._actor = actor

    @property
    def authentication_context(self):
        """Gets the authentication_context of this LogEvent.  # noqa: E501


        :return: The authentication_context of this LogEvent.  # noqa: E501
        :rtype: LogAuthenticationContext
        """
        return self._authentication_context

    @authentication_context.setter
    def authentication_context(self, authentication_context):
        """Sets the authentication_context of this LogEvent.


        :param authentication_context: The authentication_context of this LogEvent.  # noqa: E501
        :type: LogAuthenticationContext
        """

        self._authentication_context = authentication_context

    @property
    def client(self):
        """Gets the client of this LogEvent.  # noqa: E501


        :return: The client of this LogEvent.  # noqa: E501
        :rtype: LogClient
        """
        return self._client

    @client.setter
    def client(self, client):
        """Sets the client of this LogEvent.


        :param client: The client of this LogEvent.  # noqa: E501
        :type: LogClient
        """

        self._client = client

    @property
    def debug_context(self):
        """Gets the debug_context of this LogEvent.  # noqa: E501


        :return: The debug_context of this LogEvent.  # noqa: E501
        :rtype: LogDebugContext
        """
        return self._debug_context

    @debug_context.setter
    def debug_context(self, debug_context):
        """Sets the debug_context of this LogEvent.


        :param debug_context: The debug_context of this LogEvent.  # noqa: E501
        :type: LogDebugContext
        """

        self._debug_context = debug_context

    @property
    def display_message(self):
        """Gets the display_message of this LogEvent.  # noqa: E501


        :return: The display_message of this LogEvent.  # noqa: E501
        :rtype: str
        """
        return self._display_message

    @display_message.setter
    def display_message(self, display_message):
        """Sets the display_message of this LogEvent.


        :param display_message: The display_message of this LogEvent.  # noqa: E501
        :type: str
        """

        self._display_message = display_message

    @property
    def event_type(self):
        """Gets the event_type of this LogEvent.  # noqa: E501


        :return: The event_type of this LogEvent.  # noqa: E501
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this LogEvent.


        :param event_type: The event_type of this LogEvent.  # noqa: E501
        :type: str
        """

        self._event_type = event_type

    @property
    def legacy_event_type(self):
        """Gets the legacy_event_type of this LogEvent.  # noqa: E501


        :return: The legacy_event_type of this LogEvent.  # noqa: E501
        :rtype: str
        """
        return self._legacy_event_type

    @legacy_event_type.setter
    def legacy_event_type(self, legacy_event_type):
        """Sets the legacy_event_type of this LogEvent.


        :param legacy_event_type: The legacy_event_type of this LogEvent.  # noqa: E501
        :type: str
        """

        self._legacy_event_type = legacy_event_type

    @property
    def outcome(self):
        """Gets the outcome of this LogEvent.  # noqa: E501


        :return: The outcome of this LogEvent.  # noqa: E501
        :rtype: LogOutcome
        """
        return self._outcome

    @outcome.setter
    def outcome(self, outcome):
        """Sets the outcome of this LogEvent.


        :param outcome: The outcome of this LogEvent.  # noqa: E501
        :type: LogOutcome
        """

        self._outcome = outcome

    @property
    def published(self):
        """Gets the published of this LogEvent.  # noqa: E501


        :return: The published of this LogEvent.  # noqa: E501
        :rtype: datetime
        """
        return self._published

    @published.setter
    def published(self, published):
        """Sets the published of this LogEvent.


        :param published: The published of this LogEvent.  # noqa: E501
        :type: datetime
        """

        self._published = published

    @property
    def request(self):
        """Gets the request of this LogEvent.  # noqa: E501


        :return: The request of this LogEvent.  # noqa: E501
        :rtype: LogRequest
        """
        return self._request

    @request.setter
    def request(self, request):
        """Sets the request of this LogEvent.


        :param request: The request of this LogEvent.  # noqa: E501
        :type: LogRequest
        """

        self._request = request

    @property
    def security_context(self):
        """Gets the security_context of this LogEvent.  # noqa: E501


        :return: The security_context of this LogEvent.  # noqa: E501
        :rtype: LogSecurityContext
        """
        return self._security_context

    @security_context.setter
    def security_context(self, security_context):
        """Sets the security_context of this LogEvent.


        :param security_context: The security_context of this LogEvent.  # noqa: E501
        :type: LogSecurityContext
        """

        self._security_context = security_context

    @property
    def severity(self):
        """Gets the severity of this LogEvent.  # noqa: E501


        :return: The severity of this LogEvent.  # noqa: E501
        :rtype: LogSeverity
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this LogEvent.


        :param severity: The severity of this LogEvent.  # noqa: E501
        :type: LogSeverity
        """

        self._severity = severity

    @property
    def target(self):
        """Gets the target of this LogEvent.  # noqa: E501


        :return: The target of this LogEvent.  # noqa: E501
        :rtype: list[LogTarget]
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this LogEvent.


        :param target: The target of this LogEvent.  # noqa: E501
        :type: list[LogTarget]
        """

        self._target = target

    @property
    def transaction(self):
        """Gets the transaction of this LogEvent.  # noqa: E501


        :return: The transaction of this LogEvent.  # noqa: E501
        :rtype: LogTransaction
        """
        return self._transaction

    @transaction.setter
    def transaction(self, transaction):
        """Sets the transaction of this LogEvent.


        :param transaction: The transaction of this LogEvent.  # noqa: E501
        :type: LogTransaction
        """

        self._transaction = transaction

    @property
    def uuid(self):
        """Gets the uuid of this LogEvent.  # noqa: E501


        :return: The uuid of this LogEvent.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this LogEvent.


        :param uuid: The uuid of this LogEvent.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def version(self):
        """Gets the version of this LogEvent.  # noqa: E501


        :return: The version of this LogEvent.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this LogEvent.


        :param version: The version of this LogEvent.  # noqa: E501
        :type: str
        """

        self._version = version

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
        if issubclass(LogEvent, dict):
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
        if not isinstance(other, LogEvent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other