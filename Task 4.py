import requests
import json
import pandas as pd

while True:
    try:
        Total = int(input('Maximum number of students for each department? '))
        if Total < 1:
            raise TypeError
        break
    except:
        print('Wrong Input')


url1 = 'https://my.api.mockaroo.com/applicants4j.json?key=94adc0d0'
get1 = requests.get(url1)
data1 = json.loads(get1.text)

df = pd.DataFrame(data1)
df['cs_math_score'] = (df['cs_score']+df['math_score'])/2
df['chemistry_physics_score'] = (df['chemistry_score']+df['physics_score'])/2
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
    return alist


Biotech = list()
Chemistry = list()
Engineering = list()
Mathematics = list()
Physics = list()

Biotech = accept1(df, Biotech, headers, categories, Total, 10, 1, 0, 7)
Chemistry = accept1(df, Chemistry, headers, categories, Total, 4, 1, 1, 7)
Engineering = accept1(df, Engineering, headers, categories, Total, 9, 1, 2, 7)
Mathematics = accept1(df, Mathematics, headers, categories, Total, 5, 1, 3, 7)
Physics = accept1(df, Physics, headers, categories, Total, 3, 1, 4, 7)
Biotech = accept1(df, Biotech, headers, categories, Total, 10, 1, 0, 8)
Chemistry = accept1(df, Chemistry, headers, categories, Total, 4, 1, 1, 8)
Engineering = accept1(df, Engineering, headers, categories, Total, 9, 1, 2, 8)
Mathematics = accept1(df, Mathematics, headers, categories, Total, 5, 1, 3, 8)
Physics = accept1(df, Physics, headers, categories, Total, 3, 1, 4, 8)

Biotech = pd.DataFrame(Biotech)
Chemistry = pd.DataFrame(Chemistry)
Engineering = pd.DataFrame(Engineering)
Mathematics = pd.DataFrame(Mathematics)
Physics = pd.DataFrame(Physics)


def myprint(dataframe, list, number):
    print(list[number].upper())
    for i in range(0, len(dataframe)):
        print(dataframe[0][i],',', dataframe[1][i], ',', dataframe[2][i])
    print('\n')


myprint(Biotech, categories, 0)
myprint(Chemistry, categories, 1)
myprint(Engineering, categories, 2)
myprint(Mathematics, categories, 3)
myprint(Physics, categories, 4)

Biotech.to_csv('biotech.csv', index=False, header=False)
Chemistry.to_csv('chemistry.csv', index=False, header=False)
Engineering.to_csv('engineering.csv', index=False, header=False)
Mathematics.to_csv('mathematics.csv', index=False, header=False)
Physics.to_csv('physics.csv', index=False, header=False)