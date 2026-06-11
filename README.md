# Smart On-Call Alerting System on AWS

A serverless monitoring and alerting solution built on AWS that helps reduce alert fatigue by notifying engineers only when a sustained and actionable issue occurs. The project demonstrates how cloud monitoring, event-driven computing, and automated notifications can be combined to improve operational reliability.

## Project Overview

In many cloud environments, temporary CPU spikes often trigger unnecessary alerts. These repeated notifications can overwhelm engineers, causing important incidents to be overlooked.

This project addresses that problem by monitoring an Amazon EC2 instance and generating alerts only when CPU utilization remains above a defined threshold for a sustained period. By filtering out short-lived spikes, the system ensures that alerts are meaningful and require attention.

## Architecture

The system follows an event-driven architecture:

```text
EC2 Instance
     ↓
CloudWatch Metrics
     ↓
CloudWatch Alarm
     ↓
AWS Lambda
     ↓
Amazon SNS
     ↓
Engineer Email
```

### How It Works

**Amazon EC2** hosts the workload being monitored. During testing, CPU stress was intentionally generated to simulate a production issue.

**Amazon CloudWatch** continuously collects performance metrics such as CPU utilization from the EC2 instance.

**CloudWatch Alarm** evaluates these metrics against predefined thresholds. The alarm is configured with multiple evaluation periods to ignore short spikes and detect only sustained problems.

**AWS Lambda** is triggered automatically when the alarm enters the ALARM state. The Lambda function processes the event and prepares an appropriate alert message.

**Amazon SNS (Simple Notification Service)** receives the alert from Lambda and delivers it to subscribed recipients.

Finally, the **on-call engineer receives an email notification** containing the severity of the issue and suggested actions for faster resolution.

## AWS Services Used

### Amazon EC2

Used to host the test workload and generate CPU utilization data for monitoring.

### Amazon CloudWatch

Used to collect system metrics and evaluate CPU performance in real time.

### AWS Lambda

Used to process alarm events without managing servers, making the solution fully serverless.

### Amazon SNS

Used to distribute notifications to subscribed email recipients.

### AWS IAM

Used to securely manage permissions between CloudWatch, Lambda, SNS, and other AWS services.

## Key Features

* Real-time CPU utilization monitoring
* Noise-controlled alerting using evaluation periods
* Event-driven serverless architecture
* Automated email notifications
* Severity-based alert messages
* Suggested actions included in alerts
* Reduced duplicate and unnecessary notifications

## Testing and Validation

To validate the system, an EC2 instance was created and CPU load was generated using Linux stress commands. The load was maintained for several minutes to simulate a real operational issue.

CloudWatch metrics and alarms were monitored to verify that the alarm entered the ALARM state only after the configured threshold conditions were met.

Lambda invocations were checked to ensure successful execution without errors, and SNS notifications were verified by confirming delivery of alert emails containing the expected information.

## Repository Structure

```text
architecture/   - Architecture diagrams and workflow explanation
cloudwatch/     - CloudWatch alarm configuration
ec2/            - CPU stress testing documentation
iam/            - IAM roles and permissions
lambda/         - Lambda function source code
sns/            - SNS topic and subscription configuration
```

## Business Benefits

This solution demonstrates how cloud-native monitoring systems can improve operational efficiency by:

* Reducing alert fatigue
* Improving incident response times
* Increasing system reliability
* Helping engineers focus on critical issues
* Supporting scalable monitoring practices

## Future Enhancements

Possible future improvements include:

* Slack and Microsoft Teams integration
* Multi-level severity classification
* Automated remediation workflows
* CloudWatch dashboards for visualization
* Multi-metric alert correlation

## Author

Mohd Alisher Hussain

Aspiring Cloud Engineer | Computer Science Engineering Student
