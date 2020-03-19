#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_resource_key
short_description: Configure IBM Cloud 'ibm_resource_key' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_resource_key' resource

requirements:
    - IBM-Cloud terraform-provider-ibm v1.2.5
    - Terraform v0.12.20

options:
    resource_alias_id:
        description:
            - The id of the resource alias for which to create resource key
        required: False
        type: str
    credentials:
        description:
            - Credentials asociated with the key
        required: False
        type: dict
    tags:
        description:
            - None
        required: False
        type: list
        elements: str
    name:
        description:
            - (Required for new resource) The name of the resource key
        required: False
        type: str
    resource_instance_id:
        description:
            - The id of the resource instance for which to create resource key
        required: False
        type: str
    parameters:
        description:
            - Arbitrary parameters to pass. Must be a JSON object
        required: False
        type: dict
    status:
        description:
            - Status of resource key
        required: False
        type: str
    crn:
        description:
            - crn of resource key
        required: False
        type: str
    role:
        description:
            - (Required for new resource) Name of the user role.Valid roles are Writer, Reader, Manager, Administrator, Operator, Viewer, Editor.
        required: False
        type: str
    id:
        description:
            - (Required when updating or destroying existing resource) IBM Cloud Resource ID.
        required: False
        type: str
    state:
        description:
            - State of resource
        choices:
            - available
            - absent
        default: available
        required: False
    ibmcloud_api_key:
        description:
            - The API Key used for authentification. This can also be
              provided via the environment variable 'IC_API_KEY'.
        required: True
    ibmcloud_region:
        description:
            - Denotes which IBM Cloud region to connect to
        default: us-south
        required: False
    ibmcloud_zone:
        description:
            - Denotes which IBM Cloud zone to connect to in multizone
              environment. This can also be provided via the environmental
              variable 'IC_ZONE'.
        required: False

author:
    - Jay Carman (@jaywcarman)
'''

# Top level parameter keys required by Terraform module
TL_REQUIRED_PARAMETERS = [
    ('name', 'str'),
    ('role', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'resource_alias_id',
    'credentials',
    'tags',
    'name',
    'resource_instance_id',
    'parameters',
    'status',
    'crn',
    'role',
]

# define available arguments/parameters a user can pass to the module
from ansible.module_utils.basic import env_fallback
module_args = dict(
    resource_alias_id=dict(
        required=False,
        type='str'),
    credentials=dict(
        required=False,
        type='dict'),
    tags=dict(
        required=False,
        elements='',
        type='list'),
    name=dict(
        required=False,
        type='str'),
    resource_instance_id=dict(
        required=False,
        type='str'),
    parameters=dict(
        required=False,
        type='dict'),
    status=dict(
        required=False,
        type='str'),
    crn=dict(
        required=False,
        type='str'),
    role=dict(
        required=False,
        type='str'),
    id=dict(
        required=False,
        type='str'),
    state=dict(
        type='str',
        required=False,
        default='available',
        choices=(['available', 'absent'])),
    ibmcloud_api_key=dict(
        type='str',
        no_log=True,
        fallback=(env_fallback, ['IC_API_KEY']),
        required=True),
    ibmcloud_region=dict(
        type='str',
        fallback=(env_fallback, ['IC_REGION']),
        default='us-south'),
    ibmcloud_zone=dict(
        type='str',
        fallback=(env_fallback, ['IC_ZONE']))
)


def run_module():
    from ansible.module_utils.basic import AnsibleModule
    import ansible.module_utils.ibmcloud as ibmcloud

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

    # New resource required arguments checks
    missing_args = []
    if module.params['id'] is None:
        for arg, _ in TL_REQUIRED_PARAMETERS:
            if module.params[arg] is None:
                missing_args.append(arg)
        if missing_args:
            module.fail_json(msg=(
                "missing required arguments: " + ", ".join(missing_args)))

    result = ibmcloud.ibmcloud_terraform(
        resource_type='ibm_resource_key',
        tf_type='resource',
        parameters=module.params,
        ibm_provider_version='1.2.5',
        tl_required_params=TL_REQUIRED_PARAMETERS,
        tl_all_params=TL_ALL_PARAMETERS)

    if result['rc'] > 0:
        module.fail_json(
            msg=ibmcloud.Terraform.parse_stderr(result['stderr']), **result)

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()