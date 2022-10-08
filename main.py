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

    @staticmethod
    def search_name(name):
        for i in HomeLibrary.__library:
            if name == i[0]:
                return HomeLibrary.to_string(i)

    @staticmethod
    def search_year(year):
        for i in HomeLibrary.__library:
            if year == i[2]:
                return HomeLibrary.to_string(i)

    @staticmethod
    def sort_by_author():
        sorted(HomeLibrary.__library[0])
        HomeLibrary.__library.sort()

    @staticmethod
    def sort_by_name():
        sorted(HomeLibrary.__library[1])
        HomeLibrary.__library.sort()

    @staticmethod
    def sort_by_year():
        sorted(HomeLibrary.__library[2])
        HomeLibrary.__library.sort()

    @staticmethod
    def delete_by_name(name):
        for i in HomeLibrary.__library:
            if name == i[0]:
                HomeLibrary.__library.remove(i)
                return
        print('Книга с таким название не найдена')


HomeLibrary('Онегин', 'Пушкин', '1833')
HomeLibrary('Мцыри', 'Лермонтов', '1840')
HomeLibrary('Война и мир', 'Толстой', '1865')

print('Пушкин -->', HomeLibrary.search_author('Пушкин'))
print('Некрасов -->', HomeLibrary.search_author('Некрасов'))
print('Мцыри -->', HomeLibrary.search_name('Мцыри'))
print('Отцы и дети -->', HomeLibrary.search_name('Отцы и дети'))
print('1865 -->', HomeLibrary.search_year('1865'))
print('1900 -->', HomeLibrary.search_year('1900'))

print()
print('Unsorted')
HomeLibrary.show()
print('\nSorted by author')
HomeLibrary.sort_by_author()
HomeLibrary.show()
print('\nSorted by name')
HomeLibrary.sort_by_name()
HomeLibrary.show()
print('\nSorted by year')
HomeLibrary.sort_by_year()
HomeLibrary.show()
print()
HomeLibrary.delete_by_name(input('Введите какую книгу удалить: '))
HomeLibrary.show()
