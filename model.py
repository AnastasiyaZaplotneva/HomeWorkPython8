import csv

def import_dictionary():
    with open("list_of_employees.cvs", mode="r", encoding='utf-8') as f:
        dict_reader = csv.DictReader(f)
        list_of_dict = list(dict_reader)
    return list_of_dict

def find_employee(k):
    array = import_dictionary()
    for i in array:
        for value in i.values():
            if value == k:
                print(i)
   

def find_position(k):
    array = import_dictionary()
    for i in array:
        for value in i.values():
            if value == k:
                print(i)


def find_salary(k):
    array = import_dictionary()
    for i in array:
        for value in i.values():
            if value == k:
                print(i)


def add_employee():
    name = input('Name: ')
    surname = input('Surname: ')
    position = input('Position: ')
    salary = input('Salary: ')
    with open('list_of_employees.cvs', mode="a", encoding='utf-8') as data:
        employee = f'{name},{surname},{position},{salary}\n'
        data.write(employee)
    

def delete_employee(k):
    array = import_dictionary()
    for i in array:
        for value in i.values():
            if value == k:
                array.remove(i)
    with open('list_of_employees.cvs', mode="w", encoding='utf-8', newline='') as data:
        fc = csv.DictWriter(data, fieldnames=array[0].keys())
        fc.writeheader()
        fc.writerows(array)



def update_data_employee():
    k = input('Введите старые данные: ')
    new_val = input('Введите новые данные: ')
    array = import_dictionary()
    for i in array:
        for value in i.values():
            if value == k:
                value == new_val
    with open('list_of_employees.cvs', mode="w", encoding='utf-8', newline='') as data:
        fc = csv.DictWriter(data, fieldnames=array[0].keys())
        fc.writeheader()
        fc.writerows(array)

def export_data_screen():
    with open("list_of_employees.cvs", mode="r", encoding='utf-8') as f:
    # Создаем объект DictReader, указываем символ-разделитель ","
        file_reader = csv.DictReader(f, delimiter = ",")
        for row in file_reader:
            print(f' {row["Name"]},{row["Surname"]}, {row["Position"]},{row["Salary"]}', end='\n')


def complete_work():
    print("До свидания!")
