#!/bin/sh

curl \
  --remote-name \
  https://raw.githubusercontent.com/vmware/pyvmomi/master/pyVmomi/ServerObjects.py

./gen.py
