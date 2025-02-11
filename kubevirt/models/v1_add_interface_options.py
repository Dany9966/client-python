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


class V1AddInterfaceOptions(object):
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
        'name': 'str',
        'network_attachment_definition_name': 'str'
    }

    attribute_map = {
        'name': 'name',
        'network_attachment_definition_name': 'networkAttachmentDefinitionName'
    }

    def __init__(self, name=None, network_attachment_definition_name=None):
        """
        V1AddInterfaceOptions - a model defined in Swagger
        """

        self._name = None
        self._network_attachment_definition_name = None

        self.name = name
        self.network_attachment_definition_name = network_attachment_definition_name

    @property
    def name(self):
        """
        Gets the name of this V1AddInterfaceOptions.
        Name indicates the logical name of the interface.

        :return: The name of this V1AddInterfaceOptions.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this V1AddInterfaceOptions.
        Name indicates the logical name of the interface.

        :param name: The name of this V1AddInterfaceOptions.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def network_attachment_definition_name(self):
        """
        Gets the network_attachment_definition_name of this V1AddInterfaceOptions.
        NetworkAttachmentDefinitionName references a NetworkAttachmentDefinition CRD object. Format: <networkAttachmentDefinitionName>, <namespace>/<networkAttachmentDefinitionName>. If namespace is not specified, VMI namespace is assumed.

        :return: The network_attachment_definition_name of this V1AddInterfaceOptions.
        :rtype: str
        """
        return self._network_attachment_definition_name

    @network_attachment_definition_name.setter
    def network_attachment_definition_name(self, network_attachment_definition_name):
        """
        Sets the network_attachment_definition_name of this V1AddInterfaceOptions.
        NetworkAttachmentDefinitionName references a NetworkAttachmentDefinition CRD object. Format: <networkAttachmentDefinitionName>, <namespace>/<networkAttachmentDefinitionName>. If namespace is not specified, VMI namespace is assumed.

        :param network_attachment_definition_name: The network_attachment_definition_name of this V1AddInterfaceOptions.
        :type: str
        """
        if network_attachment_definition_name is None:
            raise ValueError("Invalid value for `network_attachment_definition_name`, must not be `None`")

        self._network_attachment_definition_name = network_attachment_definition_name

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
        if not isinstance(other, V1AddInterfaceOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
