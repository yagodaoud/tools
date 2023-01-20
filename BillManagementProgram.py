#I've always wanted to keep control of all of the bills I have to pay every month, but was too lazy to put the on a file, so I created this code. 
#If I have already paid them I just green them out on excel, but I will add a "paid" section further. 

import pandas as pd
import seaborn as sns

bills = {}

bill_names = input("Enter the bill names (comma separated): ").split(",")

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']


for name in bill_names: #The loop will read the name of the bills first, then will proceed to read each due date and value individually 
    value = input(f"Enter the value for {name}: ")
    due_dates = {}
    for month in months:
        due_date = input(f"Enter the due day for {name} in {month}: ")
        due_dates[month] = f"{due_date}"
    bills[name] = {"Value":float(value), "Due Dates":due_dates}

df = pd.DataFrame.from_dict(bills) #Convert it to a dataframe
df = df.T #Transposes the dataframe so the bills' names are shown vertically


df_due_dates = df['Due Dates'].apply(pd.Series)

df = df.drop(columns=['Due Dates'])
df = pd.concat([df,df_due_dates], axis = 1)
df = sns.load_dataset("tips")

print(df)

df.to_excel(r'C:\Users\yagod\Desktop\Coding\.venv\Docs\Contas.xlsx', index=True) #Change the path to where you want the doc to be stored
