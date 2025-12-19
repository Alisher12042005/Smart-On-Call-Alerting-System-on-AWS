import json
import boto3
import datetime

sns = boto3.client('sns')
SNS_TOPIC_ARN = "arn:aws:sns:eu-north-1:361769601373:OnCallAlerts"

# Temporary in-memory store for last alert timestamps
# Note: This works only for warm Lambda instances. For full production, use DynamoDB.
last_alerts = {}

def lambda_handler(event, context):
    alarm = event['detail']
    
    metric_name = alarm['configuration']['metrics'][0]['metricStat']['metric']['metricName']
    threshold = alarm['configuration']['metrics'][0]['metricStat']['stat']
    state = alarm['state']['value']
    reason = alarm['state']['reason']
    
    # Extract CPU value
    cpu_value = float(reason.split('[')[1].split(' ')[0])
    
    # Severity logic
    if cpu_value >= 95:
        severity = "CRITICAL 🔴"
        action = "Immediate action required. Consider scaling or restarting service."
    elif cpu_value >= 85:
        severity = "HIGH 🟠"
        action = "Investigate running processes and monitor closely."
    else:
        severity = "MEDIUM 🟡"
        action = "Monitor the system. No immediate action required."
    
    # Duplicate alert suppression
    instance_id = alarm['configuration']['metrics'][0]['metricStat']['metric']['dimensions'][0]['value']
    key = f"{instance_id}_{severity}"
    current_time = datetime.datetime.utcnow()
    
    if key in last_alerts:
        delta = (current_time - last_alerts[key]).total_seconds()
        if delta < 600:  # 10 minutes cooldown
            print(f"Duplicate alert suppressed for {key}, last sent {delta} seconds ago")
            return {"status": "alert_suppressed"}
    
    # Update last alert time
    last_alerts[key] = current_time

    # Prepare alert message
    message = f"""
🚨 ON-CALL ALERT

Instance: {instance_id}
Metric: {metric_name}
CPU Usage: {cpu_value}%
Severity: {severity}

Reason:
{reason}

Suggested Action:
{action}

Time: {current_time} UTC
"""
    # Publish to SNS
    sns.publish(
        TopicArn=SNS_TOPIC_ARN,
        Subject=f"{severity} - CPU Alert",
        Message=message
    )

    return {"status": "alert_sent"}
