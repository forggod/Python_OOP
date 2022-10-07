# TODO: Задание 5. Разработать класс «Домашняя библиотека».
#  Предусмотреть возможность работы с произвольным числом книг, поиска книг по автору,
#  названию, году издания, добавления книг в библиотеку, удаления и
#  сортировки по разным признакам.


class HomeLibrary:
    library = []

    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year
        HomeLibrary.library.append((self.name, self.author, self.year))

    @staticmethod
    def show():
        for i in HomeLibrary.library:
            print(*i)


HomeLibrary('Онегин', 'Пушкин', '1833')
HomeLibrary('Мцыри', 'Лермонтов', '1840')
HomeLibrary('Война и мир', 'Толстой', '1865')

HomeLibrary.show()
