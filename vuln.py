#! /bin/bash
from termcolor import colored as col
import sys
import subprocess
import time
import os
try:
    print(col(os.popen("figlet Vulnix").read(), 'green'))
except:
    print(col("Installing Requirements..." , 'red'))
def ip_grabber(host_ip):
    global victim_ip
    try:
        print(col("Ip_found\n",'green')+os.popen("nmap -sV "+host_ip+" | grep -Eo '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}'").read())
        victim_ip=input(col('Enter your vm_ip : ' , 'blue'))
    except:
        print(col("Looks like you entered a wrong host_ip..." , 'red'))
host_ip=input(col("Enter your host_ip : ", "blue"))
ip_grabber(host_ip)
def scanner(victim_ip):
    try:
        print(col(os.popen("nmap "+victim_ip+" | grep open").read() , 'green'))
    except:
        print(col("Seems as host is down at "+victim_ip , 'red'))
scanner(victim_ip)