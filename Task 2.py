import csv

while True:
    try:
       Total = int(input('What is the maximum number of students for each department? '))
       if Total < 1:
           raise TypeError
       break
    except:
        print('Wrong Input')


with open('Applicants2.csv', 'r') as file:
    csv_reader = csv.reader(file)
    Applicants = list(csv_reader)

categories = ['Biotech', 'Chemistry', 'Engineering', 'Mathematics', 'Physics']

Biotech = list()
Chemistry = list()
Engineering = list()
Mathematics = list()
Physics = list()

def accept(list1,list2,list3,number1,number2,number3):
    for applicant in list1:
        if applicant[number1] == list2[number2]:
            while len(list3) <= number3 - 1:
                list3.append(applicant)
                list1.remove(applicant)
                break
    return list3
    
Biotech = accept(Applicants,categories,Biotech,3,0,Total)
Chemistry = accept(Applicants,categories,Chemistry,3,1,Total)
Engineering = accept(Applicants,categories,Engineering,3,2,Total)
Mathematics = accept(Applicants,categories,Mathematics,3,3,Total)
Physics = accept(Applicants,categories,Physics,3,4,Total)
Biotech = accept(Applicants,categories,Biotech,4,0,Total)
Chemistry = accept(Applicants,categories,Chemistry,4,1,Total)
Engineering = accept(Applicants,categories,Engineering,4,2,Total)
Mathematics = accept(Applicants,categories,Mathematics,4,3,Total)
Physics = accept(Applicants,categories,Physics,4,4,Total)



print('Biotech')
for i in range(0, Total):
    print(Biotech[i][0],Biotech[i][1],Biotech[i][2])
print('\n')
print('Chemistry')
for i in range(0, Total):
    print(Chemistry[i][0],Chemistry[i][1],Chemistry[i][2])
print('\n')
print('Engineering')
for i in range(0, Total):
    print(Engineering[i][0],Engineering[i][1],Engineering[i][2])
print('\n')
print('Mathematics')
for i in range(0, Total):
    print(Mathematics[i][0],Mathematics[i][1],Mathematics[i][2])
print('\n')
print('Physics')
for i in range(0, Total):
    print(Physics[i][0],Physics[i][1],Physics[i][2])