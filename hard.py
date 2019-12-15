#!/usr/bin/python
# -*- coding: utf-8 -*-




"""
Rail Fence шифр используется для кодирования строк путем последовательного размещения 
каждого символа по диагонали вдоль набора «рельсов». 
Сначала начните движение по диагонали и вниз. 
Когда вы достигнете дна, поменяйте направление и двигайтесь по диагонали вверх, 
пока не дойдете до верхней направляющей. Продолжайте, пока не дойдете до конца строки. 
Каждый «рельс» затем читается слева направо, чтобы получить закодированную строку.


Например, строка WEAREDISCOVEREDFLEEATONCE может быть представлена в трехрельсовой системе следующим образом:
W E C R L T E
E R D S O E E F E A O C
A I V D E N


Зашифрованная строка будет:
WECRLTEERDSOEEFEAOCAIVDEN


Реализуйте функцию railFenceCipher, которая принимает 3 аргумента и возвращает закодированную или декодированную строку:
mode - true, если строку нужно зашифровать или false, если строку нужно расшифровать
string - строку
n - количество «рельс» n > = 2


Примеры:
railFenceCipher(true, '', 10); // => ''
railFenceCipher(true, 'Hello, World!', 4); // => 'Hoo!el,Wrdl l'
railFenceCipher(false, 'H !e,Wdloollr', 4); // => 'Hello, World!'
"""



def rail_fence_cipher(mode, string, n):
	""" функция которая принимает 3 аргумента и возвращает закодированную или декодированную строку:
	mode = true, если строку нужно зашифровать вызывает подфункцию f_cipher()
	mode = false, если строку нужно расшифровать вызывает подфункцию f_decipher()
	string - строку
	n - количество «рельс» n > = 2
	"""
	

	def f_cipher(string, key):
		"""фуенкция зашифровывовавает строку Rail Fence шифром
		на вход принимает строку - string и количество "рельсов"  - key
		возыращает зашифрованную строку
		"""
		j = 0
		i = -1

		indx_list = [] 
		for _ in range(len(string)):
			if i < key-1:
				i += 1
				indx_list.append(i)
			elif j > 0:
				j -= 1
				indx_list.append(j)
			if j == 0:
				j = key-1
				i = 0

		matrix = [[''] * len(string) for _ in range(key)]

		for i in range(len(string)):
			matrix[indx_list[i]].append(string[i])

		reslt_list = [elem for line in matrix for elem in line]
		
		return ''.join(reslt_list)


	def f_transpose_array(array):
		"""функция транспонированирует матрицу 
		входная [3][5], возвращает [5][3]
		"""
		result = [[0 for y in range(len(array))] for x in range(len(array[0]))]

		for i in range( len(array) ):
			for j in range( len(array[0]) ):
				result[j][i] = array[i][j]

		return result


	def f_decipher(string, key):
		"""фуенкция дешифрует Rail Fence шифр
		на вход принимает зашифрованную строку - string и количество "рельсов" - key
		возыращает расшифрованную строку
		"""

		decipher_reslt = ''

		matrix = [['' for i in range(len(string))] for j in range(key)]

		indx = 0
		i = 1 

		for line in range(len(matrix)):
			row = 0 

			for col in range(len(matrix[ row ])):
				if row + i < 0 or row + i >= len(matrix):
					i *= -1

				if row == line:
					matrix[row][col] += string[indx]
					indx += 1 

				row += i


		matrix1 = f_transpose_array(matrix)

		
		for line in matrix:
			decipher_reslt += ''.join(line)

		return decipher_reslt

	# шифрование или дешифрование строки в зависимости от переданого значения mode (True | False)
	if mode:
		return f_cipher(string, n)
	else:
		return f_decipher(string, n)




# mode=4 'Hello, World!' <-> 'H !e,Wdloollr'
# mode=3 'WEAREDISCOVEREDFLEEATONCE' <-> 'WECRLTEERDSOEEFEAOCAIVDEN'


s_in = 'Hello, World!'

print(rail_fence_cipher(False, s_in, 4), end='')







