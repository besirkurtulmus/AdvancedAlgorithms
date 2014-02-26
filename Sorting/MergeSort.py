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
from random import randint
import sys

# Set the recırsion limit to 1,000,000
sys.setrecursionlimit(1000000)

def Merge(list1, list2):
	"""
	Description: Merges two sorted lists.

	Args:
		list1 (List type): The first sorted list.
		list2 (List type): The second sorted list.

	Examples:
	>>> a = [1,3,5,7,9]
	>>> b = [2,4,6,8,10]
	>>> Merge(a,b)
	[1,2,3,4,5,6,7,8,9,10]
	"""
	if len(list1) == 0:
		return list2
	if len(list2) == 0:
		return list1
	if list1[0] <= list2[0]:
		return list1[:1] + Merge(list1[1:],list2)
	else:
		return list2[:1] + Merge(list1, list2[1:])

def MergeSortRecursive(l):
	"""
	Description: Sorts a list with the merge sort algorithm in a recursive
		fashion.

	Args:
		l (List type): The list which will be sorted.

	Examples:
	>>> l = [12, 32, 22, 21, 1, 75]
	>>> MergeSortRecursive(l)
	[1, 12, 21, 22, 32, 75]
	"""
	midPoint = len(l)/2
	firstHalf = l[:midPoint]
	secondHalf = l[midPoint:]
	if len(l) > 1:
		return Merge(MergeSortRecursive(firstHalf), MergeSortRecursive(secondHalf))
	else:
		return l

def MergeSortIterative(l):
	"""
	Description: Sorts a list with the merge sort algorithm in a iterative
		fashion.

	Args:
		l (list type): The list which will be sorted

	Examples:
	>>> l = RandomList(10, 0, 1000)
	[631, 597, 27, 505, 54, 648, 809, 650, 384, 717]
	>>> MergeSortIterative(l)
	[27, 54, 384, 505, 597, 631, 648, 650, 717, 809]
	"""
	queue = []
	for i in l:
		queue.append([i])
	while len(queue) > 1:
		tmp = Merge(queue[0],queue[1])
		queue = queue[2:]
		queue.append(tmp)
	return queue[0]

def RandomList(length, min, max):
	"""
	Description: Generates a list with the given length.

	Args:
		length (int Type): The length of the randomly generated list.
		min (int type): The minimum possible number.
		max (int type): The maximum possible number.

	Examples:
	>>> RandomList(5)
	[3, 4, 8, 1, 6]
	"""
	l = []
	for i in range(length):
		l.append(randint(min, max))
	return l