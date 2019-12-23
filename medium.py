#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
Для заданного списка целых неотрицательных чисел [x1, x2, x3, ..., xn] 
вычислите последнюю цифру x1 ^ (x2 ^ (x3 ^ (... ^ xn))).

Например, lastDigit([3, 4, 2]) == 1 потому что 3 ^ (4 ^ 2) = 3 ^ 16 = 43046721.

Степенная функция растет быстро. Например, 9 ^ (9 ^ 9) имеет более 369 миллионов цифр. 
Ваш код должн эффективно работать с такими числами.

Примеры:




"""


def a_pow_simple_n(array:list):
	# принимает список числел и возвращает список состоящий из 
	# изначального первого элемента + простые числа 2,1,0
	new_array = []
	new_array.append(array[0])

	for i in range(1, len(array)):
		n = array[i]
		while n not in [0,1,2]:
			if n%2 == 0:
				new_array.append(2)
				n //= 2
			else:
				new_array.append(1)
				n -= 1
		new_array.append(n)
		
	return new_array












def f_apowx(array:list):
	# принимает список 
	# l=len(array), array[l-1] возводит в степень array[l]
	# возвращает последнюю цифру результирующего числа
	


	# упрощение степени до 2,1 нулевой элемент не меняется
	def a_pow_simple_n(array:list):
		# принимает список числел и возвращает список состоящий из 
		# изначального первого элемента + простые числа 2,1,0
		new_array = []
		new_array.append(array[0])

		for i in range(1, len(array)):
			n = array[i]
			while n not in [0,1,2]:
				if n%2 == 0:
					new_array.append(2)
					n -= 2
				else:
					new_array.append(1)
					n -= 1
			new_array.append(n)
			
		return new_array

	# возведение a[0] в степень в цикле
	def f_a0_pow_in_for(array:list):
		# циклическое возведение числа в степень array[0] возводится в степень array[1], ... и тд до array[last]
		# и возвращает результирующее число
		p = 1

		for i in range(1, len(array)):
			p = p * array[0] ** array[i]
			
		return p



	if len(array) == 2:
		tmp_list = a_pow_simple_n(array)
		tmp_a = f_a0_pow_in_for(tmp_list)
		return str(tmp_a)[-1]
	else:

		if array[-1] > 2:
			tmp_list = a_pow_simple_n(array[-2:])
			tmp_a = f_a0_pow_in_for(tmp_list)
			array[-2] = tmp_a
		else:
			array[-2] = array[-2] ** array[-1]

		return f_apowx(array[:len(array)-1])






in_list = [3,4,2]   # 43046721
in_list = [0,0,0]   # 0
in_list = [0,0]   # 1
in_list = [1,2]   # 1
in_list = [3,4,5]   # 1
in_list = [3,4,5]   # 1
in_list = [3,4,6]   # 4
in_list = [7,6,21]   # 4







#in_list = [499942,898102,846073]   # 4




print(f_apowx(in_list))


















"""


def f_apowx(array:list):
	# принимает список 
	# l=len(array), array[l-1] возводит в степень array[l]
	# возвращает последнюю цифру результирующего числа
	
	if len(array) == 2:
		return str(array[0]**array[-1])[-1]
	else:
		array[-2] = array[-2] ** array[-1]
		return f_apowx(array[:len(array)-1])

"""



