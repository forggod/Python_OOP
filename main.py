# TODO: Задание 5. Разработать класс «Домашняя библиотека».
#  Предусмотреть возможность работы с произвольным числом книг, поиска книг по автору,
#  названию, году издания, добавления книг в библиотеку, удаления и
#  сортировки по разным признакам.


class HomeLibrary:
    __library = []

    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year
        HomeLibrary.__library.append((self.name, self.author, self.year))

    @staticmethod
    def show():
        for i in HomeLibrary.__library:
            print(*i)

    @staticmethod
    def to_string(line):

        return f'{line[0]} {line[1]} {line[2]}'

    @staticmethod
    def search_author(author):
        for i in HomeLibrary.__library:
            if author == i[1]:
                return HomeLibrary.to_string(i)


HomeLibrary('Онегин', 'Пушкин', '1833')
HomeLibrary('Мцыри', 'Лермонтов', '1840')
HomeLibrary('Война и мир', 'Толстой', '1865')

print(HomeLibrary.search_author('Пушкин'))
HomeLibrary.show()
