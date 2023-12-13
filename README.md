# Wonolo Devops Assignment

## Instructions
 
Write a simple configuration management tool similar to Ansible.

It should be reading a playbook (YAML format), execute actions based on it against a remote target running Ubuntu 18.04 via SSH.

Be sure to include documentation on how to run the tool.

The following resources should be implemented:

package (install/remove a package)

file (create/upload/delete remote file)

service (start/stop/restart)

update (package manager)

directory (create/delete)

command (run random remote commands)

It is important that a playbook can be run multiple times without causing errors (idempotent).

The exercise should take somewhere between one to two hours to complete.

Some of the minimum requirements are:

The tool should be able to run actions against remote targets.
Please use one of the high-level languages such Python, Go, Ruby, etc as the choice for writing this tool.
Implement at least the package and command resources.

## Assumptions

Here is a list of assumptions made about this assignment:

- An EC2 instance running Ubuntu 18.04 is accessible via local AWS configuration

- An SSH key pair is available to use for accessing the EC2 instance

- Only one EC2 instance, a remote target, is used, i.e. not multiple instances or ASG.

## Notes

- I opted to do everything but create/upload/delete remote file and create/delete remote directories.  

- I spent around 3 hours total including thinking about the project and writing a BASH script to create an EC2 instance from minimal input.  

- FYI, I am not a fast coder by any means.

## Prerequisites

Add VPC_ID and SUBNET_ID to the top of `create-instance.sh` script to create an EC2 instance.

Install the preqrequisites.  Python3 and Pip3 are required, plus add libraries:

`pip3 install -r requirements.txt`

## Running wonoloconfigmgmt

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
