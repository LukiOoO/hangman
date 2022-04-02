import csv


# names = input("Enter names separated by commas: ").title().split(",")
# tasks = input("Enter task counts separated by commas: ").split(",")
# grades = input("Enter grades separated by commas: ").split(",")


def replace():



    message = f"Hi {} {y},\n\nThis is a reminder that you have {x} tasks left to \
    submit before you can graduate. You're current grade is {x} and can increase \
    to if you submit all assignments before the due date.\n\n"
    print(message)

    for name, task, grade in zip(names, tasks, grades):
    print(message.format(name, task, grade, int(grade) + 1))

def name():
    try:
        with open("students.csv", "r", encoding="utf-8") as w:
            csv_reader = csv.reader(w)
            name_list = []
            for x in csv_reader:
                name_list.append(x[1])
    except FileNotFoundError:
        print("Nie ma takiego pliku")

    return name_list
def surname():
    try:
        with open("students.csv", "r", encoding="utf-8") as w:
            csv_reader = csv.reader(w)
            surname = []
            for x in csv_reader:
                surname.append(x[2])
    except FileNotFoundError:
        print("Nie ma takiego pliku")

    return surname

name()
surname()

replace()

'''

I'll finish up soon
'''