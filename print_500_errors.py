import os
import re
import datetime

# current datetime for time reference
currentDatetime = datetime.datetime.now()

logsPath = './logs/'

files = [f for f in os.listdir(logsPath)]

# scan all logs in logsPath
for file in files:
  with open(logsPath + file,'r') as f:
    for line in f:
      # select datetime string from log
      d = line.split(" ")[4]
      # skip row if error tag is not present
      if "[:error]" not in line:
        continue
      # parse row datetime
      logRowDate = datetime.datetime.strptime(d, "%d/%m/%Y:%H:%M:%S")
      # compare to current datetime
      if logRowDate >= currentDatetime - datetime.timedelta(600) and logRowDate <= currentDatetime: # and logRowDate <= '2017/11/09-23:00:13':
        # since criteria is met, print request error
        print line.split("]")[4]
