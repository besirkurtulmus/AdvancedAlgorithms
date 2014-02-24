# @auther Besir Kurtulmus
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

def MergeSort(l):
	"""
	Description:

	Args:

	Examples:
	>>>
	"""
	if len(l) > 1:
		return Merge(MergeSort(l[:(len(l)/2)]), MergeSort(l[(len(l)/2):]))
	else:
		return l