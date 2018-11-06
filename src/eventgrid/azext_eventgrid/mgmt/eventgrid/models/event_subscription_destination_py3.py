# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class EventSubscriptionDestination(Model):
    """Information about the destination for an event subscription.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: WebHookEventSubscriptionDestination,
    EventHubEventSubscriptionDestination,
    StorageQueueEventSubscriptionDestination,
    HybridConnectionEventSubscriptionDestination

    All required parameters must be populated in order to send to Azure.

    :param endpoint_type: Required. Constant filled by server.
    :type endpoint_type: str
    """

    _validation = {
        'endpoint_type': {'required': True},
    }

    _attribute_map = {
        'endpoint_type': {'key': 'endpointType', 'type': 'str'},
    }

    _subtype_map = {
        'endpoint_type': {'WebHook': 'WebHookEventSubscriptionDestination', 'EventHub': 'EventHubEventSubscriptionDestination', 'StorageQueue': 'StorageQueueEventSubscriptionDestination', 'HybridConnection': 'HybridConnectionEventSubscriptionDestination'}
    }

    def __init__(self, **kwargs) -> None:
        super(EventSubscriptionDestination, self).__init__(**kwargs)
        self.endpoint_type = None
