import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date
import sys
import seaborn 


user = input('codewars user name: ')
url = f'https://www.codewars.com/api/v1/users/{user}/code-challenges/completed'

kata = requests.get(url).json()
try:
    requests.get(url).raise_for_status()
except:
    print('Please enter a valid Code Wars username.')
    sys.exit()

#create a list of the dates the katas were completed
kata_dates = []
for dates in kata['data']:
	kata_dates.append(dates['completedAt'].split('T')[0])

#create a list of the number of kata completed in a day

katas_in_day = []

for dates in kata_dates:
    katas_in_day.append(kata_dates.count(dates))

#create a dataframe with how many katas per day for each day a kata was done
df = pd.DataFrame({
        'dates' : kata_dates,
        'katas in day' : katas_in_day
})

df = df.drop_duplicates()
df = df.set_index('dates')



#add the missing dates and set value to 0, followed stack overflow solution
start_date = df.index[-1]
end_date = date.today()
idx = pd.date_range(start_date, end_date)
df.index = pd.DatetimeIndex(df.index)
df = df.reindex(idx, fill_value = 0)

seaborn.scatterplot(data =df)

plt.show()

