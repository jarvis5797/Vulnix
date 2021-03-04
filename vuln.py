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
def ip_grabber():
    global victim_ip
    print(col("Ip_found : \n"+os.popen("arp -a | grep vulnix").read() , 'yellow'))
    victim_ip=input(col('Enter your vm_ip : ' , 'blue'))
ip_grabber()
def scanner(victim_ip):
    try:
        print(col(os.popen("nmap "+victim_ip+" | grep open").read() , 'yellow'))
    except:
        print(col("Seems as host is down at "+victim_ip , 'red'))
scanner(victim_ip)