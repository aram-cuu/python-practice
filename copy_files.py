import os
import re
import datetime

# ssh parameters
logsPath = './logs/'
remoteUser = 'ansible'
remoteHost = '10.0.4.100'
remotePath = '/home/ansible/logs/'

# today's date object
now = datetime.datetime.now()

# regex filter as a string with today's info
todaysRegex = '[{0}]+_[{1}]+_[0{2}]+_'.format(now.year,now.month,now.day)

# file will only contain todays log file names
files = [f for f in os.listdir(logsPath) if re.match(r'{0}+(1[89]|2[01])+.*\.log'.format(todaysRegex), f)]

for file in files:
  os.system("scp {0} {1}@{2}:{3}".format(logsPath + file, remoteUser, remoteHost, remotePath))
