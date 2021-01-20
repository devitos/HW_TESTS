documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]
directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def name_by_doc():
    doc_number = input('Введите номер документа: ')
    first_name = None
    for information in documents:
        if information["number"] == doc_number:
            first_name = information['name'].split()[0]
    if first_name == None:
        first_name = 'Некорректный номер документа!'
    return first_name


def dir_by_doc():
    doc_number = input('Введите номер документа: ')
    direct = None
    for dir_number in directories.keys():
        for numbers in directories[dir_number]:
            if numbers == doc_number:
                direct = f'Документ находится на полке ' + dir_number
    if direct == None:
        direct = 'Некорректный номер документа!'
    return direct


def doc_list():
    for inform in documents:
        doc_type = inform['type']
        doc_numb = inform['number']
        full_name = inform['name']
        print(f'{doc_type} "{doc_numb}" "{full_name}"')
    return


def doc_add():
    new_type = input('Введите тип документа: ')
    new_number = input('Введите номер документа: ')
    new_name = input('Введите имя: ')
    new_dir = input('Введите номер каталога: ')
    result = None
    for folders in directories:
        if new_dir == folders:
            directories[new_dir].append(new_number)
            documents.append({"type": new_type, "number": new_number, "name": new_name})
            result = (f'{new_name} {new_type} "{new_number}"  записан в каталог {new_dir}')
    if result == None:
        result = ('Неправильный номер каталога!')
    return result


def delete_doc():
    del_number = input('Введите номер документа на удаление: ')
    result = None
    for catalog in directories:
        for numbers in directories[catalog]:
            if numbers == del_number:
                directories[catalog].remove(numbers)
    for info in documents:
        if info["number"] == del_number:
            result = (f'{info["name"]} {info["type"]} "{info["number"]}" был удалён')
            documents.remove(info)
    if result == None:
        result = ('Такого номера не существует!')
    return result


def dir_move():
    moved_number = input('Введите номер документы, который хотите переместить: ')
    new_dir = input('Введите номер полки, на которую хотите переместить: ')
    result = 'Некорректные данные'
    for dir in directories:
        for numbers in directories[dir]:
            if numbers == moved_number:
                directories[dir].remove(numbers)
                directories[new_dir].append(moved_number)
                result = ('Данные перемещены!')
    return result


'''
Никак не разобрался как разделить аннонсирования некорректный номер полки и некорректный номер документа, чтобы пользователь знал, какие именно данные некорректны
'''


def create_dir():
    new_directory = input('Введите название новой полки: ')
    result = ('Полка создана')
    for dir in directories:
        if new_directory == dir:
            result = ('Такая полка уже существует')
    directories.setdefault(new_directory)
    return result


def main():
    while True:
        user_input = input('Введите команду: ')
        if user_input == 'p':
            print(name_by_doc())
        elif user_input == 's':
            print(dir_by_doc())
        elif user_input == 'l':
            doc_list()
        elif user_input == 'a':
            print(doc_add())
        elif user_input == 'd':
            print(delete_doc())
        elif user_input == 'm':
            print(dir_move())
        elif user_input == 'as':
            print(create_dir())
        elif user_input == 'q':
            print('Bye, bye!')
            break


if __name__ == '__main__':
    main()
