# work_test - програма для отримання даних з сайту Clockify.me
## How to use program
open web-site clockify.me and get your own API-key and change example api-key in file api_key.txt
after delete "#" before on line 101 and run the code
## api_key.txt - file where is locate your api-key
## main.py - program code
#### get_api_key():
**arguments**: 
n/a
**returns**:
api_key (type string)

#### get_list(url):
**arguments**:
*url*- link which build in depence what kind of information you want to get
**returns**:
list of tasks
#### get_time(url):
**arguments**:
*url* - link (example:https://reports.api.clockify.me/v1/shared-reports/{sharedReportId})
**returns**:
list of full information about task in project

#### time_function(x):
**arguments**:
*x*- integer number
**returns**:
return time like hh:mm:ss(type string)

#### make_list(d):
**arguments**:
*d* - list from what we want to get information about name of tasks, time per task and date of making task
**returns**:
list of tasks and time for each task

