# CPU Stress Testing

This document explains how CPU stress testing was performed on the EC2
instance to validate the alerting system.

## Why Stress Testing Was Required
Cloud monitoring systems must be tested under real load conditions.
Stress testing helps verify:
- Alarm accuracy
- Noise suppression logic
- End-to-end alert flow

## Stress Tool Used
- **Tool**: stress
- **Operating System**: Amazon Linux 2

## Command Executed
```bash
stress --cpu 2 --timeout 900
