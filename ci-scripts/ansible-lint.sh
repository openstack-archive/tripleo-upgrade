#!/bin/bash

# ANSIBLE0006: Using command rather than module
#   we have a few use cases where we need to use curl and rsync
# ANSIBLE0007: Using command rather than an argument to e.g file
#   we have a lot of 'rm' command and we should use file module instead
# ANSIBLE0010: Package installs should not use latest.
#   Sometimes we need to update some packages.
# ANSIBLE0012: Commands should not change things if nothing needs doing
# ANSIBLE0013: Use Shell only when shell functionality is required
# ANSIBLE0016: Tasks that run when changed should likely be handlers
#   this requires refactoring roles, skipping for now
SKIPLIST="ANSIBLE0006,ANSIBLE0007,ANSIBLE0010,ANSIBLE0012,ANSIBLE0013,ANSIBLE0016"

ansible-lint -vvv -x $SKIPLIST ./ -R -r ./ci-scripts/ansible_rules
