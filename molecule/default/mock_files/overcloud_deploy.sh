#!/bin/bash

set -ux


### --start_docs
## Deploying the overcloud
## =======================

## Prepare Your Environment
## ------------------------

## * Source in the undercloud credentials.
## ::

source /home/zuul/stackrc

## * Deploy the overcloud!
## ::
openstack overcloud deploy --override-ansible-cfg /home/zuul/custom_ansible.cfg \
    --templates /usr/share/openstack-tripleo-heat-templates \
    --libvirt-type qemu  --timeout 120 --ntp-server 0.pool.ntp.org,1.pool.ntp.org,2.pool.ntp.org,3.pool.ntp.org -e /home/zuul/cloud-names.yaml       -e /usr/share/openstack-tripleo-heat-templates/environments/docker-ha.yaml   -e /home/zuul/containers-prepare-parameter.yaml   -e /usr/share/openstack-tripleo-heat-templates/environments/docker.yaml   -e /usr/share/openstack-tripleo-heat-templates/ci/environments/network/multiple-nics/network-isolation-absolute.yaml -e /usr/share/openstack-tripleo-heat-templates/ci/environments/network/multiple-nics/network-environment.yaml -e /home/zuul/overcloud_network_params.yaml  -e /home/zuul/overcloud_storage_params.yaml  -e /usr/share/openstack-tripleo-heat-templates/environments/low-memory-usage.yaml -e /home/zuul/src/opendev.org/openstack/tripleo-ci/test-environments/worker-config.yaml -e /usr/share/openstack-tripleo-heat-templates/environments/debug.yaml  -e /home/zuul/enable-tls.yaml -e /usr/share/openstack-tripleo-heat-templates/environments/ssl/tls-endpoints-public-ip.yaml -e /home/zuul/inject-trust-anchor.yaml   -e /usr/share/openstack-tripleo-heat-templates/environments/disable-telemetry.yaml    --validation-errors-nonfatal    -e /home/zuul/overcloud-topology-config.yaml  -e /home/zuul/overcloud-selinux-config.yaml  -e /usr/share/openstack-tripleo-heat-templates/ci/environments/ovb-ha.yaml   \
    "$@" && status_code=0 || status_code=$?
