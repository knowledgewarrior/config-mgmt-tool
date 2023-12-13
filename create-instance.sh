#!/usr/bin/env bash

# Creates prerequisites and an EC2 instance
export PROJECT_NAME="wonolo-ec2"
export INSTANCE_TYPE="t4g.micro"
export INSTANCE_COUNT=1
export VPC_ID="vpc-xxxxxxxxxx"
export SUBNET_ID="subnet-xxxxxxxxxx"
export SSH_KEY_NAME="wonolo-key"
# ubuntu 18.04 in us-east-1
export AMI_ID="ami-03d57c6f085140d11"

echo "creating security group"
# create security group
SECURITY_GROUP_ID=`aws ec2 create-security-group \
    --group-name $PROJECT_NAME-sg \
    --description "Wonolo DevOps Assignment" \
    --tag-specifications 'ResourceType=security-group,Tags=[{Key=Name,Value=$PROJECT_NAME-sg}]' \
    --vpc-id $VPC_ID \
    --query "GroupId" \
    --output text`

echo "security group ${SECURITY_GROUP_ID} created"

echo "authorizing ssh for security group ${SECURITY_GROUP_ID}"
# authorize ssh for security group
aws ec2 authorize-security-group-ingress \
    --group-id $SECURITY_GROUP_ID \
    --protocol tcp \
    --port 22 \
    --cidr "0.0.0.0/0" 

echo "creating ssh key pair"
# create key pair to use with ec2 instance
aws ec2 create-key-pair --key-name  $SSH_KEY_NAME \
   --query 'KeyMaterial' --output text > ~/.ssh/$SSH_KEY_NAME

# change permission for file to secure as per ssh
chmod 600 ~/.ssh/$SSH_KEY_NAME

echo "creating ec2 instance"
aws ec2 run-instances \
    --image-id $AMI_ID \
    --count $INSTANCE_COUNT \
    --instance-type $INSTANCE_TYPE \
    --key-name $SSH_KEY_NAME \
    --security-group-ids $SECURITY_GROUP_ID \
    --subnet-id $SUBNET_ID \
    --block-device-mappings "[{\"DeviceName\":\"/dev/sdf\",\"Ebs\":{\"VolumeSize\":30,\"DeleteOnTermination\":false}}]" \
    --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=$PROJECT_NAME}]' 'ResourceType=volume,Tags=[{Key=Name,Value=$PROJECT_NAME-disk}]'
