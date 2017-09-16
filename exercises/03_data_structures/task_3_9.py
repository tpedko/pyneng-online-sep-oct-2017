# -*- coding: utf-8 -*-
'''
Задание 3.9

Найти индекс последнего вхождения элемента.

Например, для списка num_list, число 10 последний раз встречается с индексом 4;
в списке word_list, слово 'ruby' последний раз встречается с индексом 6.

Сделать решение общим (то есть, не привязываться к конкретному элементу в конкретном списке)
и проверить на двух списках, которые указаны и на разных элементах.


Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

num_list = [10, 2, 30, 100, 10, 50, 11, 30, 15, 7]
word_list = ['python', 'ruby', 'perl', 'ruby', 'perl', 'python', 'ruby', 'perl']


num_list.reverse()
print(len(num_list) - num_list.index(10)-1)

word_list.reverse()
print(len(word_list) - word_list.index('ruby')-1)