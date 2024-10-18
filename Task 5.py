import requests
import json
import pandas as pd
import csv
import matplotlib.pyplot as plt
import numpy as np


while True:
    try:
        Total = int(input('Maximum number of students for each department? '))
        if Total < 1:
            raise TypeError
        break
    except:
        print('Wrong Input')


url1 = 'https://my.api.mockaroo.com/applicants5j.json?key=94adc0d0'
get1 = requests.get(url1)
data1 = json.loads(get1.text)

df = pd.DataFrame(data1)
df['cs_math_score'] = (df['cs_score']+df['math_score'])/2
df['chemistry_physics_score'] = (df['chemistry_score']+df['physics_score'])/2
df['admissions_exam'] = df['admissions_exam'].fillna(0.0)
categories = ['Biotech', 'Chemistry', 'Engineering', 'Mathematics','Physics']
headers = df.columns


def accept1(dataframe, alist, blist,clist, number1, number2, number3, number4, number5):
    dataframe = dataframe.sort_values( by = [blist[number2], blist[number3]], ascending=[False, True])
    for applicant in dataframe.iterrows():
        if applicant[1][number5] == clist[number4]:
            while len(alist) <= number1 - 1:
                alist.append((applicant[1][1],applicant[1][0],applicant[1][number2]))
                dataframe = dataframe.drop(applicant[0])
                break
    dataframe = dataframe.sort_values( by = [blist[9], blist[number3]], ascending=[False, True])
    for applicant in df.iterrows():
        if applicant[1][number5] == clist[number4]:
            while len(alist) <= Total - 1:
                alist.append((applicant[1][1],applicant[1][0],applicant[1][9]))
                dataframe = dataframe.drop(applicant[0])
                break        
    return alist


Biotech = list()
Chemistry = list()
Engineering = list()
Mathematics = list()
Physics = list()

Biotech = accept1(df, Biotech, headers, categories, Total, 11, 1, 0, 7)
Chemistry = accept1(df, Chemistry, headers, categories, Total, 4, 1, 1, 7)
Engineering = accept1(df, Engineering, headers, categories, Total, 10, 1, 2, 7)
Mathematics = accept1(df, Mathematics, headers, categories, Total, 5, 1, 3, 7)
Physics = accept1(df, Physics, headers, categories, Total, 3, 1, 4, 7)
Biotech = accept1(df, Biotech, headers, categories, Total, 11, 1, 0, 8)
Chemistry = accept1(df, Chemistry, headers, categories, Total, 4, 1, 1, 8)
Engineering = accept1(df, Engineering, headers, categories, Total, 10, 1, 2, 8)
Mathematics = accept1(df, Mathematics, headers, categories, Total, 5, 1, 3, 8)
Physics = accept1(df, Physics, headers, categories, Total, 3, 1, 4, 8)

Biotech = pd.DataFrame(Biotech)
Chemistry = pd.DataFrame(Chemistry)
Engineering = pd.DataFrame(Engineering)
Mathematics = pd.DataFrame(Mathematics)
Physics = pd.DataFrame(Physics)

def myprint(dataframe, list, number):
    print(list[number])
    for i in range(0, len(dataframe)):
        print(dataframe[0][i], dataframe[1][i], ':', dataframe[2][i])
    print('\n')


myprint(Biotech, categories, 0)
myprint(Chemistry, categories, 1)
myprint(Engineering, categories, 2)
myprint(Mathematics, categories, 3)
myprint(Physics, categories, 4)

def mywrite(dataframe, list, number):
    writer.writerow([list[number]])
    for i in range(0, len(dataframe)):
        writer.writerow([dataframe[0][i], dataframe[1][i], dataframe[2][i]])
    writer.writerow('\n')

with open('allAcceptedStudents.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    mywrite(Biotech,categories,0)
    mywrite(Chemistry,categories,1)
    mywrite(Engineering,categories,2)
    mywrite(Mathematics,categories,3)
    mywrite(Physics,categories,4)

x = [Biotech.loc[:][2].to_string(index=False).split('\n'),Chemistry[:][2].to_string(index=False).split('\n'),Engineering[:][2].to_string(index=False).split('\n'),Mathematics[:][2].to_string(index=False).split('\n'),Chemistry[:][2].to_string(index=False).split('\n')]
x = sum(x, [])
y = list()
for i in range(0, len(x)):
    y.append(float(x[i]))

plt.hist(y)
plt.xlabel('Score')
plt.ylabel('Number of Students')
plt.title('Students Score Breakdown', fontweight ="bold")
plt.show()