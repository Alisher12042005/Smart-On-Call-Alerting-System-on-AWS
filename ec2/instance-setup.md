# EC2 Instance Setup

This document describes the EC2 instance configuration used for testing
the Smart On-Call Alerting System.

## Instance Details
- **Instance Type**: t2.micro
- **AMI**: Amazon Linux 2
- **Region**: ap-south-1
- **Architecture**: x86_64

## Purpose of EC2 Instance
The EC2 instance is used to:
- Simulate real application workload
- Generate controlled CPU usage
- Validate CloudWatch alarm behavior under load

## Access Method
- **Connection Type**: EC2 Instance Connect
- **User**: ec2-user

## Monitoring Configuration
- Default EC2 monitoring enabled
- CPUUtilization metric collected by Amazon CloudWatch

## Security Considerations
- Instance runs inside a security group with limited inbound access
- No public services exposed
- Used only for testing purposes

## Expected Outcome
The instance serves as a workload generator to verify that alerts are
triggered only during sustained high CPU usage.
