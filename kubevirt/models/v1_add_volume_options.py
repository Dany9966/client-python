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


class V1AddVolumeOptions(object):
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
        'disk': 'V1Disk',
        'name': 'str',
        'volume_source': 'V1HotplugVolumeSource'
    }

    attribute_map = {
        'disk': 'disk',
        'name': 'name',
        'volume_source': 'volumeSource'
    }

    def __init__(self, disk=None, name=None, volume_source=None):
        """
        V1AddVolumeOptions - a model defined in Swagger
        """

        self._disk = None
        self._name = None
        self._volume_source = None

        self.disk = disk
        self.name = name
        self.volume_source = volume_source

    @property
    def disk(self):
        """
        Gets the disk of this V1AddVolumeOptions.
        Disk represents the hotplug disk that will be plugged into the running VMI

        :return: The disk of this V1AddVolumeOptions.
        :rtype: V1Disk
        """
        return self._disk

    @disk.setter
    def disk(self, disk):
        """
        Sets the disk of this V1AddVolumeOptions.
        Disk represents the hotplug disk that will be plugged into the running VMI

        :param disk: The disk of this V1AddVolumeOptions.
        :type: V1Disk
        """
        if disk is None:
            raise ValueError("Invalid value for `disk`, must not be `None`")

        self._disk = disk

    @property
    def name(self):
        """
        Gets the name of this V1AddVolumeOptions.
        Name represents the name that will be used to map the disk to the corresponding volume. This overrides any name set inside the Disk struct itself.

        :return: The name of this V1AddVolumeOptions.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this V1AddVolumeOptions.
        Name represents the name that will be used to map the disk to the corresponding volume. This overrides any name set inside the Disk struct itself.

        :param name: The name of this V1AddVolumeOptions.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def volume_source(self):
        """
        Gets the volume_source of this V1AddVolumeOptions.
        VolumeSource represents the source of the volume to map to the disk.

        :return: The volume_source of this V1AddVolumeOptions.
        :rtype: V1HotplugVolumeSource
        """
        return self._volume_source

    @volume_source.setter
    def volume_source(self, volume_source):
        """
        Sets the volume_source of this V1AddVolumeOptions.
        VolumeSource represents the source of the volume to map to the disk.

        :param volume_source: The volume_source of this V1AddVolumeOptions.
        :type: V1HotplugVolumeSource
        """
        if volume_source is None:
            raise ValueError("Invalid value for `volume_source`, must not be `None`")

        self._volume_source = volume_source

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
        if not isinstance(other, V1AddVolumeOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
