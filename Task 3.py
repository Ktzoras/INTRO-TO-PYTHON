import json

while True:
    try:
        Total = int(input('What is the maximum number of students for each department? '))
        if Total < 1:
            raise TypeError
        break
    except:
      print('Wrong Input')


with open('Applicants3.json', 'r') as file:
    data = json.load(file)


Applicants = dict()

for i in range(0, len(data)):
    Applicants[i] = data[i]


categories = ['Biotech', 'Chemistry', 'Engineering', 'Mathematics','Physics']
titles = ['first_name', 'last_name', 'gender', 'physics_score', 'chemistry_score', 'math_score', 'cs_score', 'OPTION1', 'OPTION2']


Biotech = list()
Chemistry = list() 
Engineering = list()
Mathematics = list()
Physics = list()

def accept(dict,list1,list2,list3,number1, number2, number3):
    for item in list(dict.items()):
        if item[1][list3[number1]] == list1[number2]:
            if len(list2) < Total:
                list2.append([item[1][list3[0]],item[1][list3[1]],item[1][list3[number3]]])
                dict.pop(item[0])   
    list2.sort(key=lambda x: x[2], reverse=True)
    return list2

Biotech = accept(Applicants, categories, Biotech, titles, 7, 0, 4)
Chemistry = accept(Applicants, categories, Chemistry, titles, 7, 1, 4)
Engineering = accept(Applicants, categories, Engineering, titles, 7, 2, 6)
Mathematics = accept(Applicants, categories, Mathematics, titles, 7, 3, 5)
Physics = accept(Applicants, categories, Physics, titles, 7, 4, 3)
Biotech = accept(Applicants, categories, Biotech, titles, 8, 0, 4)
Chemistry = accept(Applicants, categories, Chemistry, titles, 8, 1, 4)
Engineering = accept(Applicants, categories, Engineering, titles, 8, 2, 6)
Mathematics = accept(Applicants, categories, Mathematics, titles, 8, 3, 5)
Physics = accept(Applicants, categories, Physics, titles, 8, 4, 3)

print('Biotech')
for i in range(0, len(Biotech)):
    print(Biotech[i][0],Biotech[i][1],':',Biotech[i][2])
print('\n')
print('Chemistry')
for i in range(0, len(Chemistry)):
    print(Chemistry[i][0],Chemistry[i][1],':',Chemistry[i][2])
print('\n')
print('Engineering')
for i in range(0, len(Engineering)):
    print(Engineering[i][0],Engineering[i][1],':',Engineering[i][2])
print('\n')
print('Mathematics')
for i in range(0, len(Mathematics)):
    print(Mathematics[i][0],Mathematics[i][1],':',Mathematics[i][2])
print('\n')
print('Physics')
for i in range(0, len(Physics)):
    print(Physics[i][0],Physics[i][1],':',Physics[i][2])    
