## 📣 Amazon SNS – On-Call Alert Notification

### 🔹 SNS Topic Details
- **Service**: Amazon Simple Notification Service (SNS)
- **Topic Name**: `on-call-cpu-alerts`
- **Region**: Same as EC2 and Lambda
- **Topic Type**: Standard

---

### 🔹 Subscription Configuration
- **Protocol**: Email  
- **Subscriber**: On-call Engineer  
- **Subscription Status**: ✅ Confirmed  

> A confirmation email was received and approved to activate alert delivery.

---

### 🔹 Purpose of Using SNS
Amazon SNS is used as the **final notification layer** of the alerting system.

It ensures:
- Reliable and durable alert delivery
- Loose coupling between Lambda and notification channels
- Easy future extension to SMS, Slack, or PagerDuty

---

### 🔹 Alert Delivery Flow
1. AWS Lambda publishes an alert message to the SNS topic  
2. SNS forwards the alert to the on-call engineer’s email  
3. The engineer receives a **clear, actionable, and severity-based alert**

---

### 🔹 Alert Message Content
Each alert email contains:
- **Severity level** (Medium / High / Critical)
- **Current CPU utilization value**
- **Problem summary**
- **Suggested action for faster resolution**

This ensures alerts are **to-the-point** and **free from noise**.

---

### 🔹 Why Amazon SNS
- Fully managed AWS service
- High availability and scalability
- Native integration with AWS Lambda
- Ideal for production-grade alerting systems

---

### ✅ Outcome
- Guaranteed alert delivery to on-call engineer
- Reduced alert fatigue
- Faster incident response
- Production-ready notification pipeline

