#!/usr/bin/env python3

import csv
from datetime import datetime

  
def fwd_start(product):
    if not product['report_date'] or not product['start_date']:
        return "FALSE"
    
    else:

        start_date = convert_to_date(product['start_date'])
        trade_date = convert_to_date(product['trade_date'])
        report_date = convert_to_date(product['report_date'])
        
        # scenario 'no start date'
        if start_date is None:
            return "FALSE"
        
        # primary sceanrio
        if start_date > report_date:

            if trade_date is not None and trade_date < report_date:
                return "TRUE"
            else:
                return "FALSE"
        
        # etc.... all edge cases
        
    return "FALSE"
    
def convert_to_date(date_string):
    date_format = '%d/%m/%y'
    try:
        return datetime.strptime(date_string,date_format) 
    except:
        return None   
# We can create a generic implementation of the tests as follows:
def csv_to_dict():
    """Returns tests in CSV as a dictionary"""
    tests = []

    file_path = 'watchers/fwd_start/tests/fwd_start_tests.csv'
    input_file = csv.DictReader(open(file_path))

    for row in input_file:
        tests.append(row)
    
    return tests    
  
def test_fwd_start():
    tests = csv_to_dict()
    for test in tests:
        try:
            print('testing ' + test['description'])
            print(test)
            assert fwd_start(test) == test['fwd_start']
            print('Passed')
        except AssertionError:
            print('Failed')



if __name__ == '__main__':
    test_fwd_start()