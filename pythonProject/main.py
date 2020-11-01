# -*- coding: utf-8 -*-
# Вариант запроса Д
# Вариант предметной области 14: CD-диск - библиотека CD-дисков

from operator import itemgetter
class Disk:
    # диск
    def __init__(self, id, title, memory, library_id):
        self.id = id
        self.title = title
        self.memory = memory
        self.library_id = library_id

class Library:
    # библиотека
    def __init__(self, id, name):
        self.id = id
        self.name = name


class DisLib:
    # диски библиотеки для связи
    # многие-ко-многим
    def __init__(self,  lib_id, dis_id):
        self.lib_id = lib_id
        self.dis_id = dis_id

# библиотеки
lib = [
    Library(1, "Games"),
    Library(2, "Movies"),
    Library(3, "Music"),

    Library(4, "Methodical manual"),
    Library(5, "Photos")
]

# библиотеки
dis = [
    Disk(1, "GTA V", 650, 1),
    Disk(2, "Summer 2019", 700, 5),
    Disk(4, "Gremlin", 680, 1),
    Disk(5, "Engineering", 800, 4),
    Disk(6, "Travis Scott", 750, 3),
    Disk(7, "Leonid Agutin", 700, 3),
    Disk(8, "Graduation", 750, 5),
    Disk(9, "Analytical geometry", 650, 4),
    Disk(10, "A star is born", 800, 2)
]

dis_lib = [
    DisLib(1, 1),
    DisLib(4, 2),
    DisLib(5, 3),
    DisLib(1, 4),
    DisLib(3, 5),
    DisLib(4, 6),
    DisLib(4, 7),
    DisLib(5, 8),
    DisLib(3, 9),
    DisLib(2, 10)
]

def main():
    # соединение данных один-ко-многим
    one_to_many = [(d.title, d.memory, l.name)
                   for l in lib
                   for d in dis
                   if d.library_id == l.id]

    # соединение данных многие-ко-многим
    many_to_many_temp = [(l.name, dl.lib_id, dl.dis_id)
                         for l in lib
                         for dl in dis_lib
                         if l.id == dl.lib_id]

    many_to_many = [(d.title, d.memory, lib_name)
                    for lib_name, lib_id, dis_id in many_to_many_temp
                    for d in dis if d.id == dis_id]

    print('Задание Д1')
    res1 = []
    for i in one_to_many:
        if i[0][-2:] == "in":
            res1.append(i[0:3:2])
    print(res1)

    print('\nTЗадание Д2')
    res2_unsorted = []
    for l in lib:
        l_dis = list(filter(lambda i: i[2] == l.name, one_to_many))
        if len(l_dis) > 0:
            o_memory = [memory for _, memory, _ in l_dis]
            o_memory_sum = sum(o_memory)
            o_memory_count = len(o_memory)
            o_memory_average = o_memory_sum / o_memory_count
            res2_unsorted.append((l.name, int(o_memory_average)))
    res2 = sorted(res2_unsorted, key=itemgetter(1), reverse=True)
    print(res2)

    print('\nЗадание Д3')
    res3 = {}
    for l in lib:
        if l.name[0] == "M":
            l_dis = list(filter(lambda i: i[2] == l.name, many_to_many))
            l_dis_title = [x for x, _, _ in l_dis]
            res3[l.name] = l_dis_title
    print(res3)


if __name__ == '__main__':
    main()


