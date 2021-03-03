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
    print(os.popen("nmap -sV "+host_ip+" | grep -Eo '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}'").read())
host_ip=input(col("Enter your host_ip : ", "blue"))
ip_grabber(host_ip)