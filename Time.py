import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print("Time management")

data=(["sleep","work","phone","study"])

print("Enter the time you use for each activity")
hours=[]

for activity in data:
    act = int(input(f" Enter the total no. of hours you spend for {activity} per day: "))
    hours.append(act)
    
total_time = sum(hours) 

sleep_hours = hours[0] 

print("Total time used:", total_time)
print("Active time:", total_time - sleep_hours)

datas = {
    "Activity" : data,
    "Hours" : hours
}

df = pd.DataFrame(datas)

print(df)

if sleep_hours<8:
    print("You need more sleep")
else:
    print("You are having enough sleep")

if total_time<24:
    print("You have ", 24 - total_time, "hour(s) for free time")
else:
    print("You have no free time")
 
plt.pie(hours ,labels = data)
plt.show()

