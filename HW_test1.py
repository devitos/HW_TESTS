import pytest
import Buh1


class TestAnyThing:

    def setup(self):
        print('\nНачинаем тестирование')

    def test_name_by_doc1(self):
        Buh1.input = lambda doc_number: '10006'
        print('\nПроверка name_by_doc правильный номер')
        assert Buh1.name_by_doc() == 'Аристарх'

    def test_name_by_doc2(self):
        Buh1.input = lambda doc_number: '234'
        print('\nПроверка name_by_doc неправильный номер')
        assert Buh1.name_by_doc() == 'Некорректный номер документа!'

    def test_dir_by_doc1(self):
        Buh1.input = lambda doc_number: '2207 876234'
        print('\nПроверка dir_by_doc с правильным номером документа')
        assert Buh1.dir_by_doc() == 'Документ находится на полке 1'

    def test_dir_by_doc2(self):
        Buh1.input = lambda doc_number: '2564854'
        print('\nПроверка dir_by_doc с неправильным номером документа')
        assert Buh1.dir_by_doc() == 'Некорректный номер документа!'

    def test_add_doc1(self):
        input_values = ['Паспорт', '115 364', 'Владимир Христофоров', '3']
        result = []

        # Нашел в интернете следующую конструкцию, так и не разобрался что она делает и как работает.
        def mock_input(s):
            result.append(s)
            return input_values.pop(0)
        Buh1.input = mock_input
        # Buh1.print = lambda s: result.append(s)
        print('\nПроверка doc_add с правильным номером полки')
        assert Buh1.doc_add() == 'Владимир Христофоров Паспорт "115 364"  записан в каталог 3'

    def test_add_doc2(self):
        input_values = ['Паспорт', '115 364', 'Владимир Христофоров', '4']

        # Преобразовал предыдущую конструкцию в такую, всё равно не очень понятно как она работает, если есть
        # возможность объясните пожалуйста.
        def mock_input(*args):
            return input_values.pop(0)
        Buh1.input = mock_input
        print('\nПроверка doc_add с неправильным номером полки')
        assert Buh1.doc_add() == 'Неправильный номер каталога!'

    def test_delete_doc1(self):
        input_values = ['10006']

        def mock_input(*args):
            return input_values.pop(0)
        Buh1.input = mock_input
        print('\nПроверка del_doc с правильным номером паспорта')
        assert Buh1.delete_doc() == 'Аристарх Павлов insurance "10006" был удалён'

    def test_delete_doc2(self):
        input_values = ['12123123123']

        def mock_input(*args):
            return input_values.pop(0)
        Buh1.input = mock_input
        print('\nПроверка del_doc с правильным номером паспорта')
        assert Buh1.delete_doc() == 'Такого номера не существует!'

    def teardown(self):
        print('Закончили тестирование')