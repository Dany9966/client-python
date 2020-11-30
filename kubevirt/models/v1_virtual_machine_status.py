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


class V1VirtualMachineStatus(object):
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
        'conditions': 'list[V1VirtualMachineCondition]',
        'created': 'bool',
        'ready': 'bool',
        'snapshot_in_progress': 'str',
        'state_change_requests': 'list[V1VirtualMachineStateChangeRequest]',
        'volume_requests': 'list[V1VirtualMachineVolumeRequest]',
        'volume_snapshot_statuses': 'list[V1VolumeSnapshotStatus]'
    }

    attribute_map = {
        'conditions': 'conditions',
        'created': 'created',
        'ready': 'ready',
        'snapshot_in_progress': 'snapshotInProgress',
        'state_change_requests': 'stateChangeRequests',
        'volume_requests': 'volumeRequests',
        'volume_snapshot_statuses': 'volumeSnapshotStatuses'
    }

    def __init__(self, conditions=None, created=None, ready=None, snapshot_in_progress=None, state_change_requests=None, volume_requests=None, volume_snapshot_statuses=None):
        """
        V1VirtualMachineStatus - a model defined in Swagger
        """

        self._conditions = None
        self._created = None
        self._ready = None
        self._snapshot_in_progress = None
        self._state_change_requests = None
        self._volume_requests = None
        self._volume_snapshot_statuses = None

        if conditions is not None:
          self.conditions = conditions
        if created is not None:
          self.created = created
        if ready is not None:
          self.ready = ready
        if snapshot_in_progress is not None:
          self.snapshot_in_progress = snapshot_in_progress
        if state_change_requests is not None:
          self.state_change_requests = state_change_requests
        if volume_requests is not None:
          self.volume_requests = volume_requests
        if volume_snapshot_statuses is not None:
          self.volume_snapshot_statuses = volume_snapshot_statuses

    @property
    def conditions(self):
        """
        Gets the conditions of this V1VirtualMachineStatus.
        Hold the state information of the VirtualMachine and its VirtualMachineInstance

        :return: The conditions of this V1VirtualMachineStatus.
        :rtype: list[V1VirtualMachineCondition]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """
        Sets the conditions of this V1VirtualMachineStatus.
        Hold the state information of the VirtualMachine and its VirtualMachineInstance

        :param conditions: The conditions of this V1VirtualMachineStatus.
        :type: list[V1VirtualMachineCondition]
        """

        self._conditions = conditions

    @property
    def created(self):
        """
        Gets the created of this V1VirtualMachineStatus.
        Created indicates if the virtual machine is created in the cluster

        :return: The created of this V1VirtualMachineStatus.
        :rtype: bool
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this V1VirtualMachineStatus.
        Created indicates if the virtual machine is created in the cluster

        :param created: The created of this V1VirtualMachineStatus.
        :type: bool
        """

        self._created = created

    @property
    def ready(self):
        """
        Gets the ready of this V1VirtualMachineStatus.
        Ready indicates if the virtual machine is running and ready

        :return: The ready of this V1VirtualMachineStatus.
        :rtype: bool
        """
        return self._ready

    @ready.setter
    def ready(self, ready):
        """
        Sets the ready of this V1VirtualMachineStatus.
        Ready indicates if the virtual machine is running and ready

        :param ready: The ready of this V1VirtualMachineStatus.
        :type: bool
        """

        self._ready = ready

    @property
    def snapshot_in_progress(self):
        """
        Gets the snapshot_in_progress of this V1VirtualMachineStatus.
        SnapshotInProgress is the name of the VirtualMachineSnapshot currently executing

        :return: The snapshot_in_progress of this V1VirtualMachineStatus.
        :rtype: str
        """
        return self._snapshot_in_progress

    @snapshot_in_progress.setter
    def snapshot_in_progress(self, snapshot_in_progress):
        """
        Sets the snapshot_in_progress of this V1VirtualMachineStatus.
        SnapshotInProgress is the name of the VirtualMachineSnapshot currently executing

        :param snapshot_in_progress: The snapshot_in_progress of this V1VirtualMachineStatus.
        :type: str
        """

        self._snapshot_in_progress = snapshot_in_progress

    @property
    def state_change_requests(self):
        """
        Gets the state_change_requests of this V1VirtualMachineStatus.
        StateChangeRequests indicates a list of actions that should be taken on a VMI e.g. stop a specific VMI then start a new one.

        :return: The state_change_requests of this V1VirtualMachineStatus.
        :rtype: list[V1VirtualMachineStateChangeRequest]
        """
        return self._state_change_requests

    @state_change_requests.setter
    def state_change_requests(self, state_change_requests):
        """
        Sets the state_change_requests of this V1VirtualMachineStatus.
        StateChangeRequests indicates a list of actions that should be taken on a VMI e.g. stop a specific VMI then start a new one.

        :param state_change_requests: The state_change_requests of this V1VirtualMachineStatus.
        :type: list[V1VirtualMachineStateChangeRequest]
        """

        self._state_change_requests = state_change_requests

    @property
    def volume_requests(self):
        """
        Gets the volume_requests of this V1VirtualMachineStatus.
        VolumeRequests indicates a list of volumes add or remove from the VMI template and hotplug on an active running VMI.

        :return: The volume_requests of this V1VirtualMachineStatus.
        :rtype: list[V1VirtualMachineVolumeRequest]
        """
        return self._volume_requests

    @volume_requests.setter
    def volume_requests(self, volume_requests):
        """
        Sets the volume_requests of this V1VirtualMachineStatus.
        VolumeRequests indicates a list of volumes add or remove from the VMI template and hotplug on an active running VMI.

        :param volume_requests: The volume_requests of this V1VirtualMachineStatus.
        :type: list[V1VirtualMachineVolumeRequest]
        """

        self._volume_requests = volume_requests

    @property
    def volume_snapshot_statuses(self):
        """
        Gets the volume_snapshot_statuses of this V1VirtualMachineStatus.
        VolumeSnapshotStatuses indicates a list of statuses whether snapshotting is supported by each volume.

        :return: The volume_snapshot_statuses of this V1VirtualMachineStatus.
        :rtype: list[V1VolumeSnapshotStatus]
        """
        return self._volume_snapshot_statuses

    @volume_snapshot_statuses.setter
    def volume_snapshot_statuses(self, volume_snapshot_statuses):
        """
        Sets the volume_snapshot_statuses of this V1VirtualMachineStatus.
        VolumeSnapshotStatuses indicates a list of statuses whether snapshotting is supported by each volume.

        :param volume_snapshot_statuses: The volume_snapshot_statuses of this V1VirtualMachineStatus.
        :type: list[V1VolumeSnapshotStatus]
        """

        self._volume_snapshot_statuses = volume_snapshot_statuses

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
        if not isinstance(other, V1VirtualMachineStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
