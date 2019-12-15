#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Реализуйте функцию uniqueWords, которая на вход получает строку s и возвращает строку вида 
w1: countW1, w2: countW2, где слова отсортированы в алфавитном порядке.


uniqueWords('Мир мир Акула акула аКулА бревно БревНо');
 => 'акула: 3, бревно: 2, мир: 2'

uniqueWords('Звезда звездА по По именИ имени имени солнце Солнце СОЛНЦЕ песня'); 
=> 'звезда: 2, имени: 3, песня: 1, по: 2, солнце: 3'
"""



def unique_words(s):
	#
	s_low_list = s.lower().split(' ')
	s_ls_list = list(set(s_low_list))
	s_ls_list.sort()
	

	restl_str = ''
	for elem in s_ls_list:
		restl_str = restl_str + elem + ': ' + str(s_low_list.count(elem)) + ', '

	return restl_str[:-2]



#s_in = 'Мир мир Акула акула аКулА бревно БревНо'
s_in = 'Звезда звездА по По именИ имени имени солнце Солнце СОЛНЦЕ песня'


print(unique_words(s_in))


