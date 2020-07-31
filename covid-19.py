import matplotlib.pyplot as plt
import csv
from datetime import datetime




total_cases ="Data/total_cases.csv"
total_deaths = "Data/total_deaths.csv"
new_cases="Data/new_cases.csv"
new_deaths="Data/new_deaths.csv" 




with open(total_cases) as f:
    reader = csv.reader(f)
    header_row = next(reader)      
    total_case, dates =[] ,[]  
    for row in reader:
        date = datetime.strptime(row[0] , '%Y-%m-%d')
        dates.append(date)
        case = int(row[1])
        total_case.append(case)



with open(total_deaths) as f:
    reader = csv.reader(f)
    header_row = next(reader)      
    total_deaths =[]  
    for row in reader:
        death = int(row[1])
        total_deaths.append(death)

with open(new_cases) as f:
    reader = csv.reader(f)
    header_row = next(reader)      
    new_cases =[]  
    for row in reader:
        cases = int(row[1])
        new_cases.append(cases)



        
with open(new_deaths) as f:
    reader = csv.reader(f)
    header_row = next(reader)      
    new_deaths =[]  
    for row in reader:
        case = int(row[1])
        new_deaths.append(case)
       



plt.style.use('seaborn')
fig ,ax= plt.subplots()





ax.plot(dates , total_case, c ='purple')
ax.plot(dates , total_deaths, c ='red')
ax.plot(dates , new_cases, c ='green')
ax.plot(dates , new_deaths, c ='yellow')
ax.set_ylim([0 , max(total_case)])

plt.title("covid 19 latest report" ,fontsize = 20)
# plt.xlabel("dates (begining of the virus to current)" , fontsize =16)
plt.legend(["total cases","total deaths", "new cases" , "new deaths" ] )



fig.autofmt_xdate()
plt.show()