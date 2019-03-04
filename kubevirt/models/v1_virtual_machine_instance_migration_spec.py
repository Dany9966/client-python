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


class V1VirtualMachineInstanceMigrationSpec(object):
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
        'configuration': 'V1MigrationConfig',
        'vmi_name': 'str'
    }

    attribute_map = {
        'configuration': 'configuration',
        'vmi_name': 'vmiName'
    }

    def __init__(self, configuration=None, vmi_name=None):
        """
        V1VirtualMachineInstanceMigrationSpec - a model defined in Swagger
        """

        self._configuration = None
        self._vmi_name = None

        if configuration is not None:
          self.configuration = configuration
        if vmi_name is not None:
          self.vmi_name = vmi_name

    @property
    def configuration(self):
        """
        Gets the configuration of this V1VirtualMachineInstanceMigrationSpec.

        :return: The configuration of this V1VirtualMachineInstanceMigrationSpec.
        :rtype: V1MigrationConfig
        """
        return self._configuration

    @configuration.setter
    def configuration(self, configuration):
        """
        Sets the configuration of this V1VirtualMachineInstanceMigrationSpec.

        :param configuration: The configuration of this V1VirtualMachineInstanceMigrationSpec.
        :type: V1MigrationConfig
        """

        self._configuration = configuration

    @property
    def vmi_name(self):
        """
        Gets the vmi_name of this V1VirtualMachineInstanceMigrationSpec.
        The name of the VMI to perform the migration on. VMI must exist in the migration objects namespace

        :return: The vmi_name of this V1VirtualMachineInstanceMigrationSpec.
        :rtype: str
        """
        return self._vmi_name

    @vmi_name.setter
    def vmi_name(self, vmi_name):
        """
        Sets the vmi_name of this V1VirtualMachineInstanceMigrationSpec.
        The name of the VMI to perform the migration on. VMI must exist in the migration objects namespace

        :param vmi_name: The vmi_name of this V1VirtualMachineInstanceMigrationSpec.
        :type: str
        """

        self._vmi_name = vmi_name

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
        if not isinstance(other, V1VirtualMachineInstanceMigrationSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
