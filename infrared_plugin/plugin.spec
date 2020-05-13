---
plugin_type: install
subparsers:
    tripleo-upgrade:
        description: Upgrade or update TripleO deployment
        include_groups: ["Ansible options", "Inventory", "Common options", "Answers file"]
        groups:
            - title: TripleO Upgrade
              options:
                  overcloud-upgrade:
                      type: Bool
                      help: |
                          Upgrade Overcloud.
                          NOTE: Upgrade require overcloud deployment script to be available in home directory of undercloud
                          user at undercloud node
                      default: false
                  undercloud-os-upgrade:
                      type: Bool
                      help: |
                          Upgrade Undercloud's Operating System
                      default: false
                  undercloud-upgrade:
                      type: Bool
                      help: |
                          Upgrade Undercloud
                      default: false
                  upgrade-workarounds:
                      type: Bool
                      help: |
                          Apply upgrade workarounds
                      default: false
                  upstream-container-images:
                      type: Bool
                      help: |
                          Use upstream or downstream container images during upgrade
                      default: false
                  undercloud-reboot:
                      type: Bool
                      help: |
                          Reboot undercloud post upgrade when ovs or kernel get upgraded
                      default: false
                  upgrade-floatingip-check:
                      type: Bool
                      help: |
                          Check floating ip connectivity during upgrade.
                          Note: This requires a running instance with attached floating ip and allowed icmp traffic.
                      default: false
                  upgrade-workload:
                      type: Bool
                      help: |
                          Launch workload before starting upgrade
                      default: false
                  upgrade-workloadimage:
                      type: Value
                      help: |
                          Image URL to be used for spawning instance before upgrade.
                      default: https://download.cirros-cloud.net/0.4.0/cirros-0.4.0-x86_64-disk.img
                  upgrade-workloadmemory:
                      type: Value
                      help: |
                          Memory assigned to the instance spawned before upgrade
                      default: 512
                  upgrade-workloaduser:
                      type: Value
                      help: |
                          User used for conecting to workload instance via SSH
                      default: cirros
                  upgrade-workloaddisk:
                      type: Value
                      help: |
                          Disk size assigned to the instance spawned before upgrade
                      default: 5
                  upgrade-workloadvcpu:
                      type: Value
                      help: |
                          Amount of vcpus assigned to the instance spawned before upgrade
                      default: 1
                  upgrade-workloadswap:
                      type: Value
                      help: |
                          Swap size assigned to the instance spawned before upgrade
                      default: 512
                  upgrade-compute-evacuate:
                      type: Bool
                      help: |
                          Migrate instances between compute nodes during upgrade.
                      default: true
                  upgrade-controller-reboot:
                      type: Bool
                      help: |
                          Reboot controller nodes post upgrade
                      default: true
                  upgrade-controller-post:
                      type: Bool
                      help: |
                          Run controller post upgrade checks
                      default: true
                  upgrade-reboot-force:
                      type: Bool
                      help: |
                          Hard reboot nodes during upgrade
                      default: false
                  upgrade-docker-local-registry:
                      type: Bool
                      help: Use local docker registry on the undercloud
                      default: false
                  upgrade-docker-registry-url:
                      type: Value
                      help: The alternative docker registry to use for deployment.
                      default: 'registry.example.local'
                  upgrade-remove-rpm:
                      type: Bool
                      help: Remove packages which get migrated to containers during upgrade
                      default: false
                  upgrade-hci:
                      type: Bool
                      help: |
                          The upgrade workflow for HCI deployments is slightly different.
                          This option accomdates HCI upgrade.
                      default: false
                  upgrade-postcomposable-workload:
                      type: Bool
                      help: |
                          Launch workload after major composable upgrade step
                      default: false
                  upgrade-l3agent-failover-check:
                      type: Bool
                      help: |
                          Check l3 agent does not failover during upgrade.
                          Existing neutron router is required.
                      default: false
                  upgrade-nova-actions-check:
                      type: Bool
                      help: |
                          Check Nova actions can be performed to an already existing
                          instance post upgrade.
                      default: false
            - title: TripleO Update
              options:
                  overcloud-update:
                      type: Bool
                      help: |
                          Update Overcloud.
                      default: false
                  undercloud-update:
                      type: Bool
                      help: |
                          Update Undercloud
                      default: false
                  updates-workarounds:
                      type: Bool
                      help: |
                          Apply updates  workarounds
                      default: false
                  deployment-files:
                      type: Value
                      help: |
                          Directory containing the templates of the overcloud deployment.
                      default: virt
                  enforce-rhel:
                      type: Bool
                      help: |
                         Skip Rhel Enforcment, false by default, use only when registred.
                      default: false
            - title: TripleO Options
              options:
                  overcloud-stack:
                      type: Value
                      help: Overcloud stack name
                      default: "overcloud"
                  overcloud-ssh-user:
                      type: Value
                      help: Overcloud ssh user name name
                      default: ''
                  config-heat:
                      type: NestedDict
                      action: append
                      help: |
                          Inject additional Tripleo Heat Templates configuration options under "paramater_defaults"
                          entry point.
                          Example:
                              --config-heat ComputeExtraConfig.nova::allow_resize_to_same_host=true
                              --config-heat NeutronOVSFirewallDriver=openvswitch
                          should inject the following yaml to "overcloud deploy" command:

                              ---
                              parameter_defaults:
                                  ComputeExtraConfig:
                                      nova::allow_resize_to_same_host: true
                                  NeutronOVSFirewallDriver: openvswitch

                          It is also possible to have . (dot) included in key by escaping it.
                          Example:
                              --config-heat "ControllerExtraConfig.opendaylight::log_levels.org\.opendaylight\.netvirt\.elan=TRACE"

                          should inject the following yaml to "overcloud deploy" command:

                               ---
                               parameter_defaults:
                                   ControllerExtraConfig:
                                       opendaylight::log_levels:
                                           org.opendaylight.netvirt.elan: TRACE
                  config-resource:
                      type: NestedDict
                      action: append
                      help: |
                          Inject additional Tripleo Heat Templates configuration options under "resource_registry"
                          entry point.
                          Example:
                              --config-resource OS::TripleO::BlockStorage::Net::SoftwareConfig=/home/stack/nic-configs/cinder-storage.yaml
                          should inject the following yaml to "overcloud deploy" command:

                              ---
                              resource_registry:
                                  OS::TripleO::BlockStorage::Net::SoftwareConfig: /home/stack/nic-configs/cinder-storage.yaml
                  rhsm-overcloud-env:
                      type: Value
                      help: Rhsm environment location to be passed during upgrade/update prepare step ssh user name name
                      default: ''


            - title: TripleO Fast Forward Upgrade
              options:
                  overcloud-ffu-upgrade:
                      type: Bool
                      help: |
                          Fast Forward Upgrade Overcloud
                          NOTE: Upgrade require overcloud deployment script to be available in home directory of undercloud
                          user at undercloud node
                      default: false
                  undercloud-ffu-os-upgrade:
                      type: Bool
                      help: |
                          Fast Forward Operating System Upgrade Undercloud (Leapp)
                      default: false
                  undercloud-ffu-upgrade:
                      type: Bool
                      help: |
                          Fast Forward Upgrade Undercloud
                      default: false
                  undercloud-ffu-releases:
                      type: ListValue
                      help: |
                          Undercloud FFU upgrade releases
                      default: 14,15,16
                  undercloud-ffu-repo:
                      type: Value
                      help: |
                          Undercloud FFU upgrade repository method
                      default: 'rhos-release'
                  upgrade-ffu-workarounds:
                      type: Bool
                      help: |
                          Apply FFU upgrade workarounds
                      default: false
                  overcloud-ffu-releases:
                      type: ListValue
                      help: |
                          Overcloud FFU upgrade releases
                      default: 14,15,16
                  overcloud-ffu-repo:
                      type: Value
                      help: |
                          Overcloud FFU upgrade repository method
                      default: 'rhos-release'
                  overcloud-ffu-bulk:
                      type: Bool
                      help: |
                          Fast Forward Upgrade all overcloud nodes at once
                      default: false
                  overcloud-ffu-compute-rolling:
                      type: Bool
                      help: |
                          Fast Forward Upgrade compute nodes one by one
                      default: false
            - title: Set up FFU packages
              options:
                  mirror:
                      type: Value
                      help: |
                          Enable usage of specified mirror (for rpm, pip etc) [brq,qeos,tlv - or hostname].
                          (Specified mirror needs to proxy multiple rpm source hosts and pypi packages.)
                  build:
                      help: |
                          String represents a timestamp of the OSP puddle.
                      type: Value
