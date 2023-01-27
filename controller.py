import model
import view

def start():
    choose = view.show_menu()
    if choose == 1:
        key = input('Введите имя или фамилию сотрудника: ')
        model.find_employee(key)
    elif choose == 2:
        key = input('Введите должность: ')
        model.find_position(key)
    elif choose == 3:
        key = input('Введите зарплату: ')
        model.find_salary(key)
    elif choose == 4:
        model.add_employee()
    elif choose == 5:
        key = input('Введите имя или фамилию: ')
        model.delete_employee(key)
    elif choose == 6:
        model.export_data_screen()
    elif choose == 7:
        model.complete_work()
    

