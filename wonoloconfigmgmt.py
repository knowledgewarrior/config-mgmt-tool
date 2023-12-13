import yaml
import paramiko
import os

def parse_yaml(file_path):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
    return data

def apply_configuration(client, config):
    #TBD refactor to be less fugly, ie loop through an array or something
    for task in config:
        if task['action'] == 'command':
            _, stdout, stderr = client.exec_command(task['command'])
            print(stdout.read().decode())
            print(stderr.read().decode())
        elif task['action'] == 'add-package':
            install_command = f"sudo apt-get install -y {task['package_name']}"
            _, stdout, stderr = client.exec_command(install_command)
            print(stdout.read().decode())
            print(stderr.read().decode())
        elif task['action'] == 'remove-package':
            remove_command = f"sudo apt-get remove -y {task['package_name']}"
            _, stdout, stderr = client.exec_command(remove_command)
            print(stdout.read().decode())
            print(stderr.read().decode())
        elif task['action'] == 'system-update':
            update_command = f"sudo apt-get update -y"
            _, stdout, stderr = client.exec_command(update_command)
            print(stdout.read().decode())
            print(stderr.read().decode())
        elif task['action'] == 'stop-service':
            stop_service_command = f"sudo systemctl stop {task['service_name']}"
            _, stdout, stderr = client.exec_command(stop_service_command)
            print(stdout.read().decode())
            print(stderr.read().decode())
        elif task['action'] == 'start-service':
            start_service_command = f"sudo systemctl start {task['service_name']}"
            _, stdout, stderr = client.exec_command(start_service_command)
            print(stdout.read().decode())
            print(stderr.read().decode())
        else:
            print(f"Unknown action: {task['action']}")


def write_to_file(client, file_path, content):
    print(f"Writing to file: {file_path}")
    with open(file_path, 'w') as file:
        client.file.write(content)

def ssh_connect(hostname, username, private_key_path):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    private_key = paramiko.RSAKey(filename=private_key_path)
    client.connect(hostname, username=username, pkey=private_key)

    return client

def ssh_disconnect(client):
    client.close()

if __name__ == "__main__":
    # TBD: change from single hostname to an array of hostnames in the config.yaml file
    ec2_hostname = 'ec2-3-239-247-106.compute-1.amazonaws.com'
    ec2_username = 'ubuntu'
    home_directory = os.path.expanduser( '~' )
    private_key_path = home_directory + '/.ssh/wonolo-key'

    config_file = "config.yaml"
    configuration = parse_yaml(config_file)

    # Connect to the remote EC2 instance
    ssh_client = ssh_connect(ec2_hostname, ec2_username, private_key_path)

    # Loop through yaml file and apply
    apply_configuration(ssh_client, configuration)

    # Disconnect from the remote EC2 instance
    ssh_disconnect(ssh_client)