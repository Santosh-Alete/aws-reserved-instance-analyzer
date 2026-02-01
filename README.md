# AWS Reserved Instance Analyzer

A Python-based tool to analyze AWS Reserved Instance (RI) and Savings Plan utilization, identify coverage gaps, and recommend optimal commitment purchases for the next quarter.

## Features

- **RI Utilization Tracking**: Monitor current Reserved Instance usage and coverage percentages
- **Savings Plan Analysis**: Track Savings Plan utilization across EC2, Fargate, and Lambda
- **Coverage Gap Detection**: Identify On-Demand instances that could benefit from commitments
- **Usage Pattern Analysis**: Analyze 90-day historical usage to recommend optimal RI purchases
- **Cost Savings Estimation**: Calculate potential savings from recommended commitments
- **Team Notifications**: Send email alerts to development teams based on resource tags
- **Quarterly Recommendations**: Generate purchase recommendations for next quarter

## Architecture

```
┌─────────────────┐
│  AWS Account    │
│  - EC2          │
│  - RDS          │
│  - Cost Explorer│
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  RI Analyzer    │
│  - Fetch RIs    │
│  - Analyze Usage│
│  - Calculate    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Reports        │
│  - CSV Export   │
│  - Email Alerts │
│  - Dashboards   │
└─────────────────┘
```

## Installation

```bash
# Clone repository
git clone https://github.com/santosh-alete/aws-reserved-instance-analyzer.git
cd aws-reserved-instance-analyzer

# Install dependencies
pip install -r requirements.txt

# Configure AWS credentials
aws configure
```

## Configuration

Create a `config.yaml` file:

```yaml
aws:
  regions:
    - us-east-1
    - us-west-2
  
analysis:
  lookback_days: 90
  coverage_threshold: 80  # Alert if coverage drops below this
  utilization_threshold: 75  # Alert if utilization drops below this

notifications:
  enabled: true
  smtp_host: smtp.gmail.com
  smtp_port: 587
  from_email: finops@company.com
  
tags:
  team_tag: Team
  environment_tag: Environment
```

## Usage

### Analyze Current RI Utilization

```bash
python ri_analyzer.py --mode utilization --output report.csv
```

### Generate Quarterly Recommendations

```bash
python ri_analyzer.py --mode recommendations --quarter Q2-2026
```

### Send Team Notifications

```bash
python ri_analyzer.py --mode notify --teams engineering,platform
```

### Full Analysis

```bash
python ri_analyzer.py --mode full --output-dir ./reports
```

## Output Examples

### Utilization Report
```
Reserved Instance Utilization Report
Generated: 2026-02-22

Total Active RIs: 45
Average Utilization: 87.3%
Coverage: 82.1%

Top Underutilized RIs:
- m5.2xlarge (us-east-1): 45% utilized
- r5.xlarge (us-west-2): 62% utilized

Potential Savings: $12,450/month
```

### Recommendation Report
```
Q2 2026 Purchase Recommendations

Based on 90-day usage analysis:

High Priority:
- m5.large (us-east-1): 15 instances → $8,200/year savings
- t3.medium (us-west-2): 8 instances → $2,100/year savings

Medium Priority:
- r5.xlarge (us-east-1): 5 instances → $3,500/year savings

Total Estimated Savings: $13,800/year
```

## Metrics Tracked

- **RI Utilization**: Percentage of purchased RI hours actually used
- **RI Coverage**: Percentage of total instance hours covered by RIs
- **On-Demand Spend**: Cost of instances running without commitments
- **Savings Opportunity**: Potential savings from optimal RI purchases
- **Commitment Waste**: Cost of unused RI capacity

## Email Notifications

The tool sends notifications to teams when:
- RI utilization drops below threshold (default: 75%)
- Coverage gaps exceed threshold (default: 20%)
- New purchase recommendations are available
- Quarterly review is due

## Scheduling

Run as a cron job for automated monitoring:

```bash
# Daily utilization check
0 8 * * * /usr/bin/python3 /path/to/ri_analyzer.py --mode utilization

# Weekly recommendations
0 9 * * 1 /usr/bin/python3 /path/to/ri_analyzer.py --mode recommendations

# Monthly team notifications
0 10 1 * * /usr/bin/python3 /path/to/ri_analyzer.py --mode notify
```

## AWS Permissions Required

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ce:GetReservationUtilization",
        "ce:GetReservationCoverage",
        "ce:GetReservationPurchaseRecommendation",
        "ce:GetCostAndUsage",
        "ec2:DescribeReservedInstances",
        "ec2:DescribeInstances",
        "rds:DescribeReservedDBInstances",
        "rds:DescribeDBInstances",
        "savingsplans:DescribeSavingsPlans",
        "savingsplans:DescribeSavingsPlansOfferingRates"
      ],
      "Resource": "*"
    }
  ]
}
```

## Real-World Impact

At my previous organization:
- Increased RI coverage from 65% to 90%
- Identified $400K in annual savings opportunities
- Reduced RI waste by 40% through better utilization tracking
- Automated quarterly planning process, saving 20 hours/month

## Contributing

Contributions welcome! Please open an issue or submit a PR.

## License

MIT License

## Author

Santosh Sreenivasulu  
Cloud FinOps Engineer  
[LinkedIn](https://linkedin.com/in/santosh-alete) | [GitHub](https://github.com/santosh-alete)
