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


class V1alpha2VolumePreferences(object):
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
        'preferred_storage_class_name': 'str'
    }

    attribute_map = {
        'preferred_storage_class_name': 'preferredStorageClassName'
    }

    def __init__(self, preferred_storage_class_name=None):
        """
        V1alpha2VolumePreferences - a model defined in Swagger
        """

        self._preferred_storage_class_name = None

        if preferred_storage_class_name is not None:
          self.preferred_storage_class_name = preferred_storage_class_name

    @property
    def preferred_storage_class_name(self):
        """
        Gets the preferred_storage_class_name of this V1alpha2VolumePreferences.
        PreffereedStorageClassName optionally defines the preferred storageClass

        :return: The preferred_storage_class_name of this V1alpha2VolumePreferences.
        :rtype: str
        """
        return self._preferred_storage_class_name

    @preferred_storage_class_name.setter
    def preferred_storage_class_name(self, preferred_storage_class_name):
        """
        Sets the preferred_storage_class_name of this V1alpha2VolumePreferences.
        PreffereedStorageClassName optionally defines the preferred storageClass

        :param preferred_storage_class_name: The preferred_storage_class_name of this V1alpha2VolumePreferences.
        :type: str
        """

        self._preferred_storage_class_name = preferred_storage_class_name

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
        if not isinstance(other, V1alpha2VolumePreferences):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
