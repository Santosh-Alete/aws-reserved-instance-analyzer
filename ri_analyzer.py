#!/usr/bin/env python3
import boto3
from datetime import datetime, timedelta

class RIAnalyzer:
    def __init__(self):
        self.ce_client = boto3.client('ce')
    
    def get_ri_utilization(self):
        end_date = datetime.now().date()
        start_date = end_date - timedelta(days=90)
        
        response = self.ce_client.get_reservation_utilization(
            TimePeriod={
                'Start': start_date.strftime('%Y-%m-%d'),
                'End': end_date.strftime('%Y-%m-%d')
            }
        )
        return response

if __name__ == '__main__':
    analyzer = RIAnalyzer()
    print(analyzer.get_ri_utilization())
