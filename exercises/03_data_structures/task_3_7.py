# -*- coding: utf-8 -*-
'''
Задание 3.7

Преобразовать MAC-адрес в двоичную строку (без двоеточий).

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

MAC = 'AAAA:BBBB:CCCC'
print(' '.join('{:08b}'.format(int(x,16)) for x in MAC.replace(':','')))