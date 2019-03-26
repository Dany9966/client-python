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


class V1Network(object):
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
        'genie': 'V1GenieNetwork',
        'multus': 'V1MultusNetwork',
        'name': 'str',
        'pod': 'V1PodNetwork'
    }

    attribute_map = {
        'genie': 'genie',
        'multus': 'multus',
        'name': 'name',
        'pod': 'pod'
    }

    def __init__(self, genie=None, multus=None, name=None, pod=None):
        """
        V1Network - a model defined in Swagger
        """

        self._genie = None
        self._multus = None
        self._name = None
        self._pod = None

        if genie is not None:
          self.genie = genie
        if multus is not None:
          self.multus = multus
        self.name = name
        if pod is not None:
          self.pod = pod

    @property
    def genie(self):
        """
        Gets the genie of this V1Network.

        :return: The genie of this V1Network.
        :rtype: V1GenieNetwork
        """
        return self._genie

    @genie.setter
    def genie(self, genie):
        """
        Sets the genie of this V1Network.

        :param genie: The genie of this V1Network.
        :type: V1GenieNetwork
        """

        self._genie = genie

    @property
    def multus(self):
        """
        Gets the multus of this V1Network.

        :return: The multus of this V1Network.
        :rtype: V1MultusNetwork
        """
        return self._multus

    @multus.setter
    def multus(self, multus):
        """
        Sets the multus of this V1Network.

        :param multus: The multus of this V1Network.
        :type: V1MultusNetwork
        """

        self._multus = multus

    @property
    def name(self):
        """
        Gets the name of this V1Network.
        Network name. Must be a DNS_LABEL and unique within the vm. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names

        :return: The name of this V1Network.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this V1Network.
        Network name. Must be a DNS_LABEL and unique within the vm. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names

        :param name: The name of this V1Network.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def pod(self):
        """
        Gets the pod of this V1Network.

        :return: The pod of this V1Network.
        :rtype: V1PodNetwork
        """
        return self._pod

    @pod.setter
    def pod(self, pod):
        """
        Sets the pod of this V1Network.

        :param pod: The pod of this V1Network.
        :type: V1PodNetwork
        """

        self._pod = pod

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
        if not isinstance(other, V1Network):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
