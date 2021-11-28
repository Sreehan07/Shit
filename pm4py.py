import pm4py
import os
import pandas as pd


# reading csv file using pandas library
event_log = pd.read_csv('PM\\running-example.csv', ';')

# 1) find out how many events have taken place
print(len(event_log))

# 2) find out how many cases are there in this file
print(len(event_log.case_id.unique()))


# 3) find out what is the most expensive case in this file
def ExpensiveCaseId(event_log):

    # find no. of cases in the event log
    CaseIds = event_log.case_id.unique()
    
    total_cost = 0
    
