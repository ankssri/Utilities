
import json
import requests

#DT Tenant
tenant = "https://<your tenant>.live.dynatrace.com"
#DT API Token
ApiTokenValue = "<Your DT API Token>"

#Step 1 GET json directly from DT server. This example is for only 1 metric
querystring = {'resolution':'10m','Api-Token':ApiTokenValue, 'metricSelector':'builtin:host.cpu.usage'}
ResponsefromDT = requests.get(tenant+"/api/v2/metrics/query", params=querystring)
print('1. JSON API Download Success-----------------')
#print(ResponsefromDT.json())
print('-----------------')

#Step 2 Save data to file on drive
with open('CPUHealth.python', 'w') as json_file:
  json.dump(ResponsefromDT.json(), json_file)
print('2. Save Success ------------------')

#Step 3 load json file from local directory
with open('C:\Ankur\Scripts\CPUMetric.json') as f:
  data_DICT = json.load(f)

# Step 4 Output: dt metrics format
print('3 Print file -----------------')
print(data_DICT)

print('4 Print name & values of CPU metric -----------------')
print(data_DICT["result"][0]["metricId"])
print(data_DICT["result"][0]["data"][0]["values"])

print('Check if any time Host CPU usage is greater than 75%-----------------')
for x in data_DICT['result'][0]['data'][0]['values']:
  print(x)
  if x is None:
      y = 0
  else:
      y = float(x) #converting string to float
      if y > 75:   #if CPU is more than 75 then print and exit
          print('done')
          break
      else:
          print('All Good')












