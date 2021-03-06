
ibm_dns_record -- Configure IBM Cloud 'ibm_dns_record' resource
===============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_dns_record' resource

This module does not support idempotency



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.16.0
- Terraform v0.12.20



Parameters
----------

  service (False, str, None)
    service info


  protocol (False, str, None)
    protocol info


  port (False, int, None)
    port number


  domain_id (True, int, None)
    (Required for new resource) Domain ID of dns record instance


  ttl (True, int, None)
    (Required for new resource) TTL configuration


  responsible_person (False, str, None)
    Responsible person for DNS record


  retry (False, int, None)
    Retry count


  minimum_ttl (False, int, None)
    Minimun TTL configuration


  weight (False, int, 0)
    weight info


  host (True, str, None)
    (Required for new resource) Hostname


  mx_priority (False, int, 0)
    Maximum priority


  type (True, str, None)
    (Required for new resource) DNS record type


  tags (False, list, None)
    tags set for the resource


  refresh (False, int, None)
    refresh rate


  priority (False, int, 0)
    priority info


  data (True, str, None)
    (Required for new resource) DNS record data


  expire (False, int, None)
    DNS record expiry info


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  iaas_classic_username (False, any, None)
    (Required when generation = 1) The IBM Cloud Classic Infrastructure (SoftLayer) user name. This can also be provided via the environment variable 'IAAS_CLASSIC_USERNAME'.


  iaas_classic_api_key (False, any, None)
    (Required when generation = 1) The IBM Cloud Classic Infrastructure API key. This can also be provided via the environment variable 'IAAS_CLASSIC_API_KEY'.


  region (False, any, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

