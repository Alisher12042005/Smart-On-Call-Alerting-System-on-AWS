# CloudWatch CPU Alarm Configuration

This document describes the CloudWatch alarm configuration used in the
Smart On-Call Alerting System.

## Metric Details
- **Service**: Amazon EC2
- **Metric Name**: CPUUtilization
- **Namespace**: AWS/EC2
- **Statistic**: Average
- **Unit**: Percent

## Alarm Threshold
- **Threshold**: CPUUtilization ≥ 80%
- **Comparison Operator**: GreaterThanOrEqualToThreshold

## Evaluation Logic (Noise Control)
- **Period**: 5 minutes
- **Evaluation Periods**: 3
- **Datapoints to Alarm**: 2

> The alarm triggers only if the CPU remains above the threshold for
> at least 2 out of the last 3 evaluation periods.  
> This prevents alerts caused by short-lived CPU spikes.

## Alarm Actions
- **Trigger Type**: State change to ALARM
- **Action**: Invoke AWS Lambda function
- **Purpose**: Forward the alert to the decision engine instead of sending
  direct notifications

## Design Rationale
This configuration is intentionally designed to:
- Ignore transient CPU spikes
- Reduce alert noise
- Prevent alert fatigue
- Trigger alerts only for sustained performance issues

## Expected Behavior
- Short CPU spikes → **No alert**
- Sustained high CPU usage → **Alarm triggered**
- Alarm event → **Lambda function invoked**
