from operator import itemgetter

while True:
    try:
        Total = int(input('Total Applicants? '))
        if Total < 1:
            raise TypeError
        break
    except:
        print('Wrong Input')

while True:
    try:
        Accepted = int(input('How many to Accept? '))
        if Accepted > Total:
            raise TypeError
        break
    except:
        print('Wrong Input')

while True:
    try:
        Applicants = list()
        Applicants2 = list()
        for i in range(0, Total):
            Applicants.append(input('Type the first name last name GPA (separated by whitespace) of each applicant: '))
        if len(Applicants) != Total:
            raise TypeError
        for applicant in Applicants:
            Applicants2.append(applicant.split(' '))
        for applicant in Applicants2:
            float(applicant[2])
        break
    except:
        print('Wrong Input')

Applicants2 = sorted(Applicants2, key=itemgetter(2), reverse=True)

print('Successful applicants:')
for i in range(0, Accepted):
    print(Applicants2[i][0],Applicants2[i][1],Applicants2[i][2])


