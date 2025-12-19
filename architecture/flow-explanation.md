# Architecture Flow Explanation

This document explains the end-to-end architecture and data flow of the
Smart On-Call Alerting System built on AWS.

## System Overview
The system is designed to monitor EC2 CPU usage and send alerts only when
a sustained and actionable issue occurs, avoiding unnecessary alert noise.

## Architecture Flow

EC2 Instance  
→ CloudWatch Metrics  
→ CloudWatch Alarm  
→ AWS Lambda (Decision Engine)  
→ Amazon SNS  
→ On-Call Engineer (Email)

## Step-by-Step Flow

### 1. EC2 (Workload Source)
- An EC2 instance runs a real workload generated using the Linux `stress` tool.
- CPUUtilization metrics are continuously emitted to Amazon CloudWatch.

### 2. CloudWatch (Monitoring Layer)
- CloudWatch collects CPUUtilization metrics at 5-minute intervals.
- A CloudWatch Alarm evaluates the metrics using multiple datapoints.
- Short-lived CPU spikes are ignored to prevent noise.

### 3. CloudWatch Alarm (Signal Generator)
- The alarm transitions to the **ALARM** state only when the CPU threshold
  is breached for a sustained period.
- Instead of directly notifying engineers, the alarm invokes a Lambda function.

### 4. AWS Lambda (Decision Engine)
- Lambda acts as the brain of the system.
- It evaluates the alarm event and current CPU value.
- Determines alert severity (Medium / High / Critical).
- Checks execution status to prevent duplicate alerts.
- If the condition is valid, Lambda publishes the alert to SNS.

### 5. Amazon SNS (Notification Layer)
- SNS receives the alert from Lambda.
- Delivers a structured email notification to the on-call engineer.
- Ensures reliable and decoupled alert delivery.

### 6. On-Call Engineer (Action Layer)
- The engineer receives a clear, severity-based alert.
- The alert includes a suggested action for quick resolution.
- Duplicate and noisy alerts are suppressed.

## Design Principles
- **Separation of responsibilities**: Monitoring, decision-making, and delivery
  are handled by different services.
- **Noise reduction**: Alerts are triggered only for sustained issues.
- **Scalability**: Each component can scale independently.
- **Production readiness**: The system follows real-world alerting practices.

## Conclusion
This architecture ensures that alerts are meaningful, actionable, and reliable.
The system focuses on signal quality rather than alert quantity, helping
engineers respond faster and with less stress.
