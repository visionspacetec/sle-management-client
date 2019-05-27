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


class ServiceInstance(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'start_time': 'int',
        'stop_time': 'int',
        'initiator_id': 'str',
        'responder_id': 'str',
        'return_timeout_period': 'int',
        'delivery_mode': 'str',
        'initiator': 'str',
        'permitted_frame_quality': 'list[str]',
        'latency_limit': 'int',
        'transfer_buffer_size': 'int',
        'report_cycle': 'int',
        'requested_frame_quality': 'str',
        'state': 'str'
    }

    attribute_map = {
        'start_time': 'start_time',
        'stop_time': 'stop_time',
        'initiator_id': 'initiator_id',
        'responder_id': 'responder_id',
        'return_timeout_period': 'return_timeout_period',
        'delivery_mode': 'delivery_mode',
        'initiator': 'initiator',
        'permitted_frame_quality': 'permitted_frame_quality',
        'latency_limit': 'latency_limit',
        'transfer_buffer_size': 'transfer_buffer_size',
        'report_cycle': 'report_cycle',
        'requested_frame_quality': 'requested_frame_quality',
        'state': 'state'
    }

    def __init__(self, start_time=None, stop_time=None, initiator_id='SLE_USER', responder_id='SLE_PROVIDER', return_timeout_period=15, delivery_mode='TIMELY_ONLINE', initiator='USER', permitted_frame_quality=["allFrames"], latency_limit=9, transfer_buffer_size=1, report_cycle=None, requested_frame_quality='allFrames', state='unbound'):  # noqa: E501
        """ServiceInstance - a model defined in OpenAPI"""  # noqa: E501

        self._start_time = None
        self._stop_time = None
        self._initiator_id = None
        self._responder_id = None
        self._return_timeout_period = None
        self._delivery_mode = None
        self._initiator = None
        self._permitted_frame_quality = None
        self._latency_limit = None
        self._transfer_buffer_size = None
        self._report_cycle = None
        self._requested_frame_quality = None
        self._state = None
        self.discriminator = None

        self.start_time = start_time
        self.stop_time = stop_time
        if initiator_id is not None:
            self.initiator_id = initiator_id
        if responder_id is not None:
            self.responder_id = responder_id
        if return_timeout_period is not None:
            self.return_timeout_period = return_timeout_period
        if delivery_mode is not None:
            self.delivery_mode = delivery_mode
        if initiator is not None:
            self.initiator = initiator
        if permitted_frame_quality is not None:
            self.permitted_frame_quality = permitted_frame_quality
        if latency_limit is not None:
            self.latency_limit = latency_limit
        if transfer_buffer_size is not None:
            self.transfer_buffer_size = transfer_buffer_size
        self.report_cycle = report_cycle
        if requested_frame_quality is not None:
            self.requested_frame_quality = requested_frame_quality
        if state is not None:
            self.state = state

    @property
    def start_time(self):
        """Gets the start_time of this ServiceInstance.  # noqa: E501

        ToDo - not yet supported  # noqa: E501

        :return: The start_time of this ServiceInstance.  # noqa: E501
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ServiceInstance.

        ToDo - not yet supported  # noqa: E501

        :param start_time: The start_time of this ServiceInstance.  # noqa: E501
        :type: int
        """

        self._start_time = start_time

    @property
    def stop_time(self):
        """Gets the stop_time of this ServiceInstance.  # noqa: E501

        ToDo - not yet supported  # noqa: E501

        :return: The stop_time of this ServiceInstance.  # noqa: E501
        :rtype: int
        """
        return self._stop_time

    @stop_time.setter
    def stop_time(self, stop_time):
        """Sets the stop_time of this ServiceInstance.

        ToDo - not yet supported  # noqa: E501

        :param stop_time: The stop_time of this ServiceInstance.  # noqa: E501
        :type: int
        """

        self._stop_time = stop_time

    @property
    def initiator_id(self):
        """Gets the initiator_id of this ServiceInstance.  # noqa: E501


        :return: The initiator_id of this ServiceInstance.  # noqa: E501
        :rtype: str
        """
        return self._initiator_id

    @initiator_id.setter
    def initiator_id(self, initiator_id):
        """Sets the initiator_id of this ServiceInstance.


        :param initiator_id: The initiator_id of this ServiceInstance.  # noqa: E501
        :type: str
        """

        self._initiator_id = initiator_id

    @property
    def responder_id(self):
        """Gets the responder_id of this ServiceInstance.  # noqa: E501


        :return: The responder_id of this ServiceInstance.  # noqa: E501
        :rtype: str
        """
        return self._responder_id

    @responder_id.setter
    def responder_id(self, responder_id):
        """Sets the responder_id of this ServiceInstance.


        :param responder_id: The responder_id of this ServiceInstance.  # noqa: E501
        :type: str
        """

        self._responder_id = responder_id

    @property
    def return_timeout_period(self):
        """Gets the return_timeout_period of this ServiceInstance.  # noqa: E501


        :return: The return_timeout_period of this ServiceInstance.  # noqa: E501
        :rtype: int
        """
        return self._return_timeout_period

    @return_timeout_period.setter
    def return_timeout_period(self, return_timeout_period):
        """Sets the return_timeout_period of this ServiceInstance.


        :param return_timeout_period: The return_timeout_period of this ServiceInstance.  # noqa: E501
        :type: int
        """

        self._return_timeout_period = return_timeout_period

    @property
    def delivery_mode(self):
        """Gets the delivery_mode of this ServiceInstance.  # noqa: E501

        ToDo - Only timely online supported  # noqa: E501

        :return: The delivery_mode of this ServiceInstance.  # noqa: E501
        :rtype: str
        """
        return self._delivery_mode

    @delivery_mode.setter
    def delivery_mode(self, delivery_mode):
        """Sets the delivery_mode of this ServiceInstance.

        ToDo - Only timely online supported  # noqa: E501

        :param delivery_mode: The delivery_mode of this ServiceInstance.  # noqa: E501
        :type: str
        """
        allowed_values = ["TIMELY_ONLINE", "COMPLETE_ONLINE", "OFFLINE"]  # noqa: E501
        if delivery_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `delivery_mode` ({0}), must be one of {1}"  # noqa: E501
                .format(delivery_mode, allowed_values)
            )

        self._delivery_mode = delivery_mode

    @property
    def initiator(self):
        """Gets the initiator of this ServiceInstance.  # noqa: E501


        :return: The initiator of this ServiceInstance.  # noqa: E501
        :rtype: str
        """
        return self._initiator

    @initiator.setter
    def initiator(self, initiator):
        """Sets the initiator of this ServiceInstance.


        :param initiator: The initiator of this ServiceInstance.  # noqa: E501
        :type: str
        """
        allowed_values = ["USER", "PROVIDER"]  # noqa: E501
        if initiator not in allowed_values:
            raise ValueError(
                "Invalid value for `initiator` ({0}), must be one of {1}"  # noqa: E501
                .format(initiator, allowed_values)
            )

        self._initiator = initiator

    @property
    def permitted_frame_quality(self):
        """Gets the permitted_frame_quality of this ServiceInstance.  # noqa: E501


        :return: The permitted_frame_quality of this ServiceInstance.  # noqa: E501
        :rtype: list[str]
        """
        return self._permitted_frame_quality

    @permitted_frame_quality.setter
    def permitted_frame_quality(self, permitted_frame_quality):
        """Sets the permitted_frame_quality of this ServiceInstance.


        :param permitted_frame_quality: The permitted_frame_quality of this ServiceInstance.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["allFrames", "erredFramesOnly", "goodFramesOnly"]  # noqa: E501
        if not set(permitted_frame_quality).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `permitted_frame_quality` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(permitted_frame_quality) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._permitted_frame_quality = permitted_frame_quality

    @property
    def latency_limit(self):
        """Gets the latency_limit of this ServiceInstance.  # noqa: E501


        :return: The latency_limit of this ServiceInstance.  # noqa: E501
        :rtype: int
        """
        return self._latency_limit

    @latency_limit.setter
    def latency_limit(self, latency_limit):
        """Sets the latency_limit of this ServiceInstance.


        :param latency_limit: The latency_limit of this ServiceInstance.  # noqa: E501
        :type: int
        """

        self._latency_limit = latency_limit

    @property
    def transfer_buffer_size(self):
        """Gets the transfer_buffer_size of this ServiceInstance.  # noqa: E501


        :return: The transfer_buffer_size of this ServiceInstance.  # noqa: E501
        :rtype: int
        """
        return self._transfer_buffer_size

    @transfer_buffer_size.setter
    def transfer_buffer_size(self, transfer_buffer_size):
        """Sets the transfer_buffer_size of this ServiceInstance.


        :param transfer_buffer_size: The transfer_buffer_size of this ServiceInstance.  # noqa: E501
        :type: int
        """

        self._transfer_buffer_size = transfer_buffer_size

    @property
    def report_cycle(self):
        """Gets the report_cycle of this ServiceInstance.  # noqa: E501


        :return: The report_cycle of this ServiceInstance.  # noqa: E501
        :rtype: int
        """
        return self._report_cycle

    @report_cycle.setter
    def report_cycle(self, report_cycle):
        """Sets the report_cycle of this ServiceInstance.


        :param report_cycle: The report_cycle of this ServiceInstance.  # noqa: E501
        :type: int
        """

        self._report_cycle = report_cycle

    @property
    def requested_frame_quality(self):
        """Gets the requested_frame_quality of this ServiceInstance.  # noqa: E501


        :return: The requested_frame_quality of this ServiceInstance.  # noqa: E501
        :rtype: str
        """
        return self._requested_frame_quality

    @requested_frame_quality.setter
    def requested_frame_quality(self, requested_frame_quality):
        """Sets the requested_frame_quality of this ServiceInstance.


        :param requested_frame_quality: The requested_frame_quality of this ServiceInstance.  # noqa: E501
        :type: str
        """
        allowed_values = ["allFrames", "erredFramesOnly", "goodFramesOnly"]  # noqa: E501
        if requested_frame_quality not in allowed_values:
            raise ValueError(
                "Invalid value for `requested_frame_quality` ({0}), must be one of {1}"  # noqa: E501
                .format(requested_frame_quality, allowed_values)
            )

        self._requested_frame_quality = requested_frame_quality

    @property
    def state(self):
        """Gets the state of this ServiceInstance.  # noqa: E501


        :return: The state of this ServiceInstance.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ServiceInstance.


        :param state: The state of this ServiceInstance.  # noqa: E501
        :type: str
        """

        self._state = state

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
        if not isinstance(other, ServiceInstance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other