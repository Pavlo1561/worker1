class Pupil():
    def __init__(self,surname,name,mark):
        self.surname = surname
        self.name = name
        self.mark = mark

#pupil_amount = 0
#best_pupils = []
#sum=0

pupils = []
def print_class(pupils):
    for pupil in pupils:
        print(pupil.surname, pupil.name, '-', pupil.mark)
    print('\n') 

def print_five(pupils):
    print('Відмінники:')
    for pupil in pupils:
        if pupil.mark == 5:
            print(pupil.surname)
    print('\n')

with open('pupils.txt', 'r', encoding = 'UTF-8') as file:
    for line in file:
        data = line.split(' ')
        pupil = Pupil(data[0],data[1],int(data[2]))
        pupils.append(pupil)
        print('\n')

print_class(pupils)
print_five(pupils)