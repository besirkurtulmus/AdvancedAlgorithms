# @auther Besir Kurtulmus
# coding: utf-8
'''
The MIT License (MIT)

Copyright (c) 2014 Ahmet Besir Kurtulmus

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''
from random import choice
from MergeSort import RandomList

def Selection(l, k):
	"""
	Description: Finds the k'th element in list l.

	Args:
		l (type list): The list which the search is going to be in.
		k (type int): The k'th element in the list.

	Examples:
	>>> l = RandomList(100, 0, 100)
	>>> Selection(l, 22)
	54
	"""
	v = choice(l)
	sL = []
	sR = []
	sV = []
	for i in l:
		if i < v:
			sL.append(i)
		elif i == v:
			sV.append(i)
		else:
			sR.append(i)
	if k <= len(sL):
		return Selection(sL, k)
	elif (k > len(sL)) and (k <= ((len(sL) + len(sV)))):
		return v
	elif k > (len(sL) + len(sV)):
		return Selection(sR, k - len(sL) - len(sV))
