# coding: utf-8

"""
    KubeVirt API

    This is KubeVirt API an add-on for Kubernetes.

    OpenAPI spec version: 1.0.0
    Contact: kubevirt-dev@googlegroups.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1MultusNetwork(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'default': 'bool',
        'network_name': 'str'
    }

    attribute_map = {
        'default': 'default',
        'network_name': 'networkName'
    }

    def __init__(self, default=None, network_name=None):
        """
        V1MultusNetwork - a model defined in Swagger
        """

        self._default = None
        self._network_name = None

        if default is not None:
          self.default = default
        self.network_name = network_name

    @property
    def default(self):
        """
        Gets the default of this V1MultusNetwork.
        Select the default network and add it to the multus-cni.io/default-network annotation.

        :return: The default of this V1MultusNetwork.
        :rtype: bool
        """
        return self._default

    @default.setter
    def default(self, default):
        """
        Sets the default of this V1MultusNetwork.
        Select the default network and add it to the multus-cni.io/default-network annotation.

        :param default: The default of this V1MultusNetwork.
        :type: bool
        """

        self._default = default

    @property
    def network_name(self):
        """
        Gets the network_name of this V1MultusNetwork.
        References to a NetworkAttachmentDefinition CRD object. Format: <networkName>, <namespace>/<networkName>. If namespace is not specified, VMI namespace is assumed.

        :return: The network_name of this V1MultusNetwork.
        :rtype: str
        """
        return self._network_name

    @network_name.setter
    def network_name(self, network_name):
        """
        Sets the network_name of this V1MultusNetwork.
        References to a NetworkAttachmentDefinition CRD object. Format: <networkName>, <namespace>/<networkName>. If namespace is not specified, VMI namespace is assumed.

        :param network_name: The network_name of this V1MultusNetwork.
        :type: str
        """
        if network_name is None:
            raise ValueError("Invalid value for `network_name`, must not be `None`")

        self._network_name = network_name

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, V1MultusNetwork):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
