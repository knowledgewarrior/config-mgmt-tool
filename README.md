# Config Management Tool

## Instructions
 
This is a simple configuration management tool similar to Ansible.

It reads a playbook (YAML format) and executes actions based on it against a remote target.

The following resources are implemented:

package (install/remove a package)

command (run random remote commands)

service (start/stop/restart)

update (package manager)

### TBD
directory (create/delete)

file (create/upload/delete remote file)

## Prerequisites

Add VPC_ID and SUBNET_ID to the top of `create-instances.sh` script to create an EC2 instance.

Install the preqrequisites.  Python3 and Pip3 are required, plus add libraries:

`pip3 install -r requirements.txt`

## Running wonoloconfigmgmt

Change the `ec2_hostname` on line 64 to the URL or IP address of the EC2 host

Run the script:

`python3 wonoloconfigmgmt.py`

The script will loop through the `config.yaml` file and perform actions as per requirements:

- tail /var/log/cloud-init.log

- ls -l /etc

- system-update

- add package rolldice

- run rolldice using 3 D20s (D&D anyone?)

- add nginx service

- remove package rolldice

- stop service nginx

- start service nginx

- remove package nginx
