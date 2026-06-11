# Smart On-Call Alerting System on AWS

A serverless AWS-based monitoring solution that reduces alert fatigue by sending notifications only for sustained and actionable incidents instead of temporary resource spikes.

## Project Overview

In many cloud environments, short-lived CPU spikes often trigger unnecessary alerts. This can lead to alert fatigue, delayed responses, and missed critical incidents.

The Smart On-Call Alerting System addresses this problem by monitoring EC2 CPU utilization and generating alerts only when predefined thresholds are consistently breached over a period of time.

## Architecture

EC2 Instance → CloudWatch Metrics → CloudWatch Alarm → AWS Lambda → Amazon SNS → Engineer Email

## AWS Services Used

* Amazon EC2
* Amazon CloudWatch
* AWS Lambda
* Amazon SNS
* AWS IAM

## Features

* CPU utilization monitoring in real time
* Noise-controlled alerting using CloudWatch evaluation periods
* Serverless event-driven architecture
* Email notifications through Amazon SNS
* Severity-based alert messages
* Suggested actions included in notifications
* Reduced duplicate and unnecessary alerts

## Testing Performed

### 1. CPU Stress Simulation

* Created an EC2 instance
* Generated CPU load using Linux stress commands
* Maintained load for several minutes to simulate a production issue

### 2. CloudWatch Alarm Validation

* Configured CPU utilization alarms
* Used multiple datapoints and evaluation periods
* Verified alarm state transitions

### 3. Lambda Execution Verification

* Monitored Lambda invocations
* Confirmed successful execution without errors
* Validated alert generation logic

### 4. SNS Notification Testing

* Created and confirmed SNS subscriptions
* Verified successful email delivery
* Checked alert content and severity information

## Repository Structure

```text
├── architecture/     # Architecture diagrams and workflow
├── cloudwatch/       # Alarm configuration details
├── ec2/              # CPU stress testing documentation
├── iam/              # IAM roles and permissions
├── lambda/           # Lambda function source code
├── sns/              # SNS topic configuration
└── LICENSE
```

## Business Benefits

* Reduced alert fatigue
* Faster incident response
* Improved system reliability
* Better operational efficiency
* Cleaner monitoring workflows

## Future Improvements

* Slack and Microsoft Teams integration
* Multi-level severity classification
* Auto-remediation using Systems Manager
* Dashboard visualization using CloudWatch Dashboards
* Multi-metric alert correlation

## Author

**Mohd Alisher Hussain**

Aspiring Cloud Engineer | Computer Science Engineering Student


## License

This project is licensed under the MIT License.
