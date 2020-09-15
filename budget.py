import boto3
import json
import os
import datetime
import requests
import calendar
from dateutil.relativedelta import relativedelta

START_DATE='2020-09-01'
END_DATE='2021-02-28'

START_TIME_DT = datetime.datetime.strptime(START_DATE, '%Y-%m-%d')
END_TIME_DT  =  datetime.datetime.strptime(END_DATE, '%Y-%m-%d')

budgetClient = boto3.client('budgets')

response = budgetClient.create_budget(
                AccountId='280032839570',
                Budget={
                    'BudgetName': 'EC2 Budget for Project A',
                    'BudgetLimit': {
                        'Amount': '50',
                        'Unit': 'USD'
                    },
                    'CostFilters': {
                        'Service': [
                            'Amazon Elastic Compute Cloud - Compute',
                        ],
                        'TagKeyValue': ['user:Project$A']
                    },
                    'CostTypes': {
                        'IncludeTax': True,
                        'IncludeSubscription': True,
                        'UseBlended': False
                    },
                    'TimeUnit': 'MONTHLY',
                    'TimePeriod': {
                        'Start': START_TIME_DT,
                        'End': END_TIME_DT
                    },
                    'CalculatedSpend': {
                        'ActualSpend': {
                            'Amount': '50',
                            'Unit': 'USD'
                        }
                    },
                    'BudgetType': 'COST'
                },
                NotificationsWithSubscribers=[
                {
                    'Notification': {
                        'NotificationType': 'ACTUAL',
                        'ComparisonOperator': 'GREATER_THAN',
                        'Threshold': 100
                    },
                    'Subscribers': [
                    {
                        'SubscriptionType': 'SNS',
                        'Address': "arn:aws:sns:us-west-2:280032839570:NotifyMe"
                    },
                    ]
                }
                ]
            )
print(response)