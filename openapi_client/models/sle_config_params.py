# coding: utf-8

"""
    sle-management-client

    Python SLE Provider Management Client

    OpenAPI spec version: 0.1.0
    Contact: oss@visionspace.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class SleConfigParams(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    AUTHENTICATION_DELAY = "authentication-delay"
    TRANSMIT_QUEUE_SIZE = "transmit-queue-size"
    STARTUP_TIMER = "startup-timer"
    ALLOW_NON_USE_HEARTBEAT = "allow-non-use-heartbeat"
    MIN_HEARBEAT = "min-hearbeat"
    MAX_HEARTBEAT = "max-heartbeat"
    MIN_DEADFACTOR = "min-deadfactor"
    MAX_DEADFACTOR = "max-deadfactor"
    MAX_TRACE_SIZE = "max-trace-size"
    MIN_REPORTING_CYCLE = "min-reporting-cycle"
    MAX_REPORTING_CYCLE = "max-reporting-cycle"
    SERVER_TYPES = "server-types"
    LOCAL_ID = "local-id"
    LOCAL_PASSWORD = "local-password"
    REMOTE_PEERS = "remote-peers"

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
    }

    attribute_map = {
    }

    def __init__(self):  # noqa: E501
        """SleConfigParams - a model defined in OpenAPI"""  # noqa: E501
        self.discriminator = None

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SleConfigParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
