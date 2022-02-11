import plotly.express as px
import pandas as pd
import csv
import statistics

df = pd.read_csv("savings_data_final.csv")

#fig = px.scatter(df, y="quant_saved", color="rem_any")
#fig.show()

with open("savings_data_final.csv", newline="") as f:
    reader =csv.reader(f)
    savings_data = list(reader)
    savings_data.pop(0)
total_entries = len(savings_data)
total_people_given_reminder = 0
for data in savings_data:
    if int(data[3])== 1:
        total_people_given_reminder += 1
import plotly.graph_objects as go

fig = go.Figure(go.Bar(x=["Reminded", "Not Reminded"], y=[total_people_given_reminder, (total_entries - total_people_given_reminder)]))
fig.show()

all_savings = []
for data in savings_data:
    all_savings.append(float(data[0]))



print(f"Mean of savings - {statistics.mean(all_savings)}")
print(f"Median of savings -  {statistics.median(all_savings)}")
print(f"Mode of savings - {statistics.mode(all_savings)}")

reminded_savings = []
not_reminded_savings = []

for data in savings_data:
    if int(data[3]) == 1:
        reminded_savings.append(float(data[0]))
    else:
        not_reminded_savings.append(float(data[0]))
print("Results for people who got reminded to save")
print(f"Mean of savings - {statistics.mean(reminded_savings)}")
print(f"Median of savings -  {statistics.median(reminded_savings)}")
print(f"Mode of savings - {statistics.mode(reminded_savings)}")

print("\n\n")
print("Results for people who were not reminded to save")
print(f"Mean of savings - {statistics.mean(not_reminded_savings)}")



print(f"Standard Deviation of all the data -> {statistics.stdev(all_savings)}")
print(f"Standard Deviation of reminded savings ->{statistics.stdev(reminded_savings)}")
print(f"Standard Deviation of not reminded savings -> {statistics.stdev(not_reminded_savings)}")


import numpy as np

age = []
savings = [] 
for data in savings_data:
    if float(data[5]) != 0:
        age.append(float(data[5]))
        savings.append(float(data[5]))
        correlation = np.corrcoef(age, savings)
        print(f"Correlation between age of person and savings -> {correlation}")

import plotly.figure_factory as ff

fig = ff.create_distplot([df["quant_saved"].tolist()], ["Savings"], show_hist=False)
fig.show()