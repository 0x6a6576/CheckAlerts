#! python3
#
# This script is for checking the alerts on Sophos Central based on the description and severity.
#
# Copyright 2018 - Jevin Lizardo
#

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from time import sleep
import sys
import logging
import pickle
import os
import time
import argparse


# Check for ID existence before any further action
def check_page(checkparam):
    try:
        element_present = EC.presence_of_element_located((By.ID, checkparam))
        WebDriverWait(browser, 120).until(element_present)
        print('Check succeeded! The ID %s is now present. Proceeding..' % checkparam)
    except TimeoutException:
        logging.error('Timed out while waiting for %s to load.' % checkparam)
        
# Log in automatically
def login_page(uname,pw):

    check_page('username')
    time.sleep(6)
    
    browser.find_element_by_id('username').send_keys(uname)
    browser.find_element_by_id('password').send_keys(pw)
    logging.info('Successfully entered username and password. Logging in..')
    browser.find_element_by_id('loginButton').click()

# Check the alert boxes
def check_box(severity,alert,scroll):
    
    check_page('dashboard-feed')
    '''
    try:
        os.remove('cookies.pkl')
    except:
        pass
    pickle.dump(browser.get_cookies() , open("cookies.pkl","wb"))
    '''
    
    browser.get('https://cloud.sophos.com/manage/alerts/' + severity)

    check_page('alerts-table-description-1')
    time.sleep(5)

    # Focus on the table to scroll
    browser.find_element_by_id('alerts-table-date-0').click()
    logging.error('Unable to find the alerts-table-date-0 element.')

    # Load the alerts. Default is 5 pages unless specified.
    i = 0
    while i != scroll:
        browser.find_element_by_tag_name('body').send_keys(Keys.END)
        time.sleep(2)
        i += 1

    # Check all the boxes if criteria matches
    for row in browser.find_elements_by_tag_name('tr'):
        try:
            if alert.lower() in row.find_element_by_class_name('table-cell-lg').text.lower():
                row.find_element_by_class_name('cell-selection').click()
        except:
            '''
            Redundant code but leaving it here for now for future enhancement.
            '''
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            row.find_element_by_class_name('cell-selection').click()
    
# Commandline Arguments
def parse_args():
    
    parser = argparse.ArgumentParser(
        description = '''This program is for clearing alerts on Sophos Central.''',
        epilog = '''Copyright 2018, Jevin Lizardo SSS IT Security''')
    parser.add_argument('-s', '--severity',
                        choices=['high','medium','info'],
                        type=str.lower,
                        required=True,
                        help='High, Medium or Info')
    parser.add_argument('-d', '--description',
                        required=True,
                        help='Description of the alert. ie. PUA, Malware etc.')
    parser.add_argument('-n', '--scroll',
                        choices=range(1,16),
                        type=int,
                        metavar="[1-15]",
                        default=5,
                        help='Specify the number of times (1-15) the alert page will be scrolled. Default is 5.')
    parser.add_argument('-u', '--username',
                        help='Sophos Central Username. Optional. If not supplied, manual login is required.')
    parser.add_argument('-p', '--password',
                        help='Sophos Central Password. Optional. If not supplied, manual login is required.')
    args = parser.parse_args()
    return args
    
def main():
    
    args = parse_args()

    # Global Variables
    global browser
    browser = webdriver.Firefox()
    print('Loading Firefox.. Please wait..')
    browser.get('https://cloud.sophos.com/manage/dashboard')

    '''
    # Load Cookies
    if os.path.exists('cookies.pkl'):
        print('Loading existing cookie..')
        try:
            for cookie in pickle.load(open('cookies.pkl', 'rb')):
                browser.add_cookie(cookie)
        except:
        # Skip exception error for now
            pass
    
    # Refresh the page
    browser.get('https://cloud.sophos.com/manage/dashboard')
    '''
    
    # Logging
    logFormat = '%(asctime)s - %(levelname)s - %(message)s'
    logging.basicConfig(filename='clearpua.log', level=logging.INFO, format=logFormat)

    if args.username and args.password:
        print('Username and password was supplied for automatic login..')
        login_page(args.username,args.password)
        check_box(args.severity,args.description,args.scroll)
    else:
        print('No username or password was supplied, proceeding..')
        check_box(args.severity,args.description,args.scroll)
        

if __name__ == '__main__':
    main()

