#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
Для заданного списка целых неотрицательных чисел [x1, x2, x3, ..., xn] 
вычислите последнюю цифру x1 ^ (x2 ^ (x3 ^ (... ^ xn))).

Например, lastDigit([3, 4, 2]) == 1 потому что 3 ^ (4 ^ 2) = 3 ^ 16 = 43046721.

Степенная функция растет быстро. Например, 9 ^ (9 ^ 9) имеет более 369 миллионов цифр. 

"""




def f_a_powx_pown(array:list):
	# принимает список 
	# l=len(array), array[l-1] возводит в степень array[l]
	# возвращает последнюю цифру результирующего числа
	
	if array == []:
		return 1

	elif len(array) == 2:
		return (array[0] ** array[1]) % 10

	else:
		array[-2] = (array[-2] ** array[-1]) % 100
		return f_a_powx_pown(array[:len(array) - 1])




#in_list = [3,4,2]   # 43046721
#in_list = [0,0,0]   # 0
#in_list = [0,0]   # 1
#in_list = [1,2]   # 1
#in_list = [3,4,5]   # 1
#in_list = [3,4,5]   # 1
#in_list = [7,6,21]   # 4
#in_list = [499942,898102,846073]   # 4
#in_list = []  # 1
in_list = [12, 30, 31]   # 6




print(f_a_powx_pown(in_list))





