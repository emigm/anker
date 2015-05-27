#!/usr/bin/python

import docker


def main():
    '''Main function'''

    module = AnsibleModule(
        argument_spec = dict(
            all = dict(default=False, choices=BOOLEANS, required=False),
            docker_api_version = dict(default='auto', required=False),
            docker_url = dict(
                default='unix://var/run/docker.sock', required=False),
            label = dict(required=False),
            quiet = dict(default=False, choices=BOOLEANS, required=False),
            status = dict(
                choices=['restarting', 'running', 'paused', 'exited'],
                required=False),
        ),
        supports_check_mode=True
    )

    params = module.params

    all_ = params['all']
    docker_api_version = params['docker_api_version']
    docker_url = params['docker_url']
    label = params['label']
    quiet = params['quiet']
    status = params['status']

    try:
        cli = docker.Client(base_url=docker_url, version=docker_api_version)

        filters = dict()
        if label is not None:
            filters['label'] = label
        else:
            pass
       
        if status is not None:
            filters['status'] = status
        else:
            pass

        containers = cli.containers(
            all=all_, filters=filters, quiet=quiet)
        ansible_facts = {
            'docker_facts': {
                'containers': containers,
            },
        }
    except Exception as ex:
        module.fail_json(msg=ex.message)

    module.exit_json(
        changed=True, ansible_facts=ansible_facts)


# Module entry point

from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()
