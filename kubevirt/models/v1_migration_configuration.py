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


class V1MigrationConfiguration(object):
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
        'allow_auto_converge': 'str',
        'bandwidth_per_migration': 'K8sIoApimachineryPkgApiResourceQuantity',
        'completion_timeout_per_gi_b': 'str',
        'node_drain_taint_key': 'str',
        'parallel_migrations_per_cluster': 'str',
        'parallel_outbound_migrations_per_node': 'str',
        'progress_timeout': 'str',
        'unsafe_migration_override': 'str'
    }

    attribute_map = {
        'allow_auto_converge': 'allowAutoConverge',
        'bandwidth_per_migration': 'bandwidthPerMigration',
        'completion_timeout_per_gi_b': 'completionTimeoutPerGiB',
        'node_drain_taint_key': 'nodeDrainTaintKey',
        'parallel_migrations_per_cluster': 'parallelMigrationsPerCluster',
        'parallel_outbound_migrations_per_node': 'parallelOutboundMigrationsPerNode',
        'progress_timeout': 'progressTimeout',
        'unsafe_migration_override': 'unsafeMigrationOverride'
    }

    def __init__(self, allow_auto_converge=None, bandwidth_per_migration=None, completion_timeout_per_gi_b=None, node_drain_taint_key=None, parallel_migrations_per_cluster=None, parallel_outbound_migrations_per_node=None, progress_timeout=None, unsafe_migration_override=None):
        """
        V1MigrationConfiguration - a model defined in Swagger
        """

        self._allow_auto_converge = None
        self._bandwidth_per_migration = None
        self._completion_timeout_per_gi_b = None
        self._node_drain_taint_key = None
        self._parallel_migrations_per_cluster = None
        self._parallel_outbound_migrations_per_node = None
        self._progress_timeout = None
        self._unsafe_migration_override = None

        self.allow_auto_converge = allow_auto_converge
        if bandwidth_per_migration is not None:
          self.bandwidth_per_migration = bandwidth_per_migration
        if completion_timeout_per_gi_b is not None:
          self.completion_timeout_per_gi_b = completion_timeout_per_gi_b
        if node_drain_taint_key is not None:
          self.node_drain_taint_key = node_drain_taint_key
        if parallel_migrations_per_cluster is not None:
          self.parallel_migrations_per_cluster = parallel_migrations_per_cluster
        if parallel_outbound_migrations_per_node is not None:
          self.parallel_outbound_migrations_per_node = parallel_outbound_migrations_per_node
        if progress_timeout is not None:
          self.progress_timeout = progress_timeout
        self.unsafe_migration_override = unsafe_migration_override

    @property
    def allow_auto_converge(self):
        """
        Gets the allow_auto_converge of this V1MigrationConfiguration.

        :return: The allow_auto_converge of this V1MigrationConfiguration.
        :rtype: str
        """
        return self._allow_auto_converge

    @allow_auto_converge.setter
    def allow_auto_converge(self, allow_auto_converge):
        """
        Sets the allow_auto_converge of this V1MigrationConfiguration.

        :param allow_auto_converge: The allow_auto_converge of this V1MigrationConfiguration.
        :type: str
        """
        if allow_auto_converge is None:
            raise ValueError("Invalid value for `allow_auto_converge`, must not be `None`")

        self._allow_auto_converge = allow_auto_converge

    @property
    def bandwidth_per_migration(self):
        """
        Gets the bandwidth_per_migration of this V1MigrationConfiguration.

        :return: The bandwidth_per_migration of this V1MigrationConfiguration.
        :rtype: K8sIoApimachineryPkgApiResourceQuantity
        """
        return self._bandwidth_per_migration

    @bandwidth_per_migration.setter
    def bandwidth_per_migration(self, bandwidth_per_migration):
        """
        Sets the bandwidth_per_migration of this V1MigrationConfiguration.

        :param bandwidth_per_migration: The bandwidth_per_migration of this V1MigrationConfiguration.
        :type: K8sIoApimachineryPkgApiResourceQuantity
        """

        self._bandwidth_per_migration = bandwidth_per_migration

    @property
    def completion_timeout_per_gi_b(self):
        """
        Gets the completion_timeout_per_gi_b of this V1MigrationConfiguration.

        :return: The completion_timeout_per_gi_b of this V1MigrationConfiguration.
        :rtype: str
        """
        return self._completion_timeout_per_gi_b

    @completion_timeout_per_gi_b.setter
    def completion_timeout_per_gi_b(self, completion_timeout_per_gi_b):
        """
        Sets the completion_timeout_per_gi_b of this V1MigrationConfiguration.

        :param completion_timeout_per_gi_b: The completion_timeout_per_gi_b of this V1MigrationConfiguration.
        :type: str
        """

        self._completion_timeout_per_gi_b = completion_timeout_per_gi_b

    @property
    def node_drain_taint_key(self):
        """
        Gets the node_drain_taint_key of this V1MigrationConfiguration.

        :return: The node_drain_taint_key of this V1MigrationConfiguration.
        :rtype: str
        """
        return self._node_drain_taint_key

    @node_drain_taint_key.setter
    def node_drain_taint_key(self, node_drain_taint_key):
        """
        Sets the node_drain_taint_key of this V1MigrationConfiguration.

        :param node_drain_taint_key: The node_drain_taint_key of this V1MigrationConfiguration.
        :type: str
        """

        self._node_drain_taint_key = node_drain_taint_key

    @property
    def parallel_migrations_per_cluster(self):
        """
        Gets the parallel_migrations_per_cluster of this V1MigrationConfiguration.

        :return: The parallel_migrations_per_cluster of this V1MigrationConfiguration.
        :rtype: str
        """
        return self._parallel_migrations_per_cluster

    @parallel_migrations_per_cluster.setter
    def parallel_migrations_per_cluster(self, parallel_migrations_per_cluster):
        """
        Sets the parallel_migrations_per_cluster of this V1MigrationConfiguration.

        :param parallel_migrations_per_cluster: The parallel_migrations_per_cluster of this V1MigrationConfiguration.
        :type: str
        """

        self._parallel_migrations_per_cluster = parallel_migrations_per_cluster

    @property
    def parallel_outbound_migrations_per_node(self):
        """
        Gets the parallel_outbound_migrations_per_node of this V1MigrationConfiguration.

        :return: The parallel_outbound_migrations_per_node of this V1MigrationConfiguration.
        :rtype: str
        """
        return self._parallel_outbound_migrations_per_node

    @parallel_outbound_migrations_per_node.setter
    def parallel_outbound_migrations_per_node(self, parallel_outbound_migrations_per_node):
        """
        Sets the parallel_outbound_migrations_per_node of this V1MigrationConfiguration.

        :param parallel_outbound_migrations_per_node: The parallel_outbound_migrations_per_node of this V1MigrationConfiguration.
        :type: str
        """

        self._parallel_outbound_migrations_per_node = parallel_outbound_migrations_per_node

    @property
    def progress_timeout(self):
        """
        Gets the progress_timeout of this V1MigrationConfiguration.

        :return: The progress_timeout of this V1MigrationConfiguration.
        :rtype: str
        """
        return self._progress_timeout

    @progress_timeout.setter
    def progress_timeout(self, progress_timeout):
        """
        Sets the progress_timeout of this V1MigrationConfiguration.

        :param progress_timeout: The progress_timeout of this V1MigrationConfiguration.
        :type: str
        """

        self._progress_timeout = progress_timeout

    @property
    def unsafe_migration_override(self):
        """
        Gets the unsafe_migration_override of this V1MigrationConfiguration.

        :return: The unsafe_migration_override of this V1MigrationConfiguration.
        :rtype: str
        """
        return self._unsafe_migration_override

    @unsafe_migration_override.setter
    def unsafe_migration_override(self, unsafe_migration_override):
        """
        Sets the unsafe_migration_override of this V1MigrationConfiguration.

        :param unsafe_migration_override: The unsafe_migration_override of this V1MigrationConfiguration.
        :type: str
        """
        if unsafe_migration_override is None:
            raise ValueError("Invalid value for `unsafe_migration_override`, must not be `None`")

        self._unsafe_migration_override = unsafe_migration_override

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
        if not isinstance(other, V1MigrationConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
