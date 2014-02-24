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
def BinarySearch(l, k, lo=0, hi=None):
	"""
	Returns the key of the given value.

	Args:
	l: the list of elements
	k: the value which is searched
	lo: lower boundry for search
	hi: higher boundry for search
	Returns:
	The key of the requested value in list l

	Examples:
	>>> l = [1,2,6,7,9]
	>>> BinarySearch(l, 6)
	2

	>>> l = [0,4,5,8,9,11]
	>>> BinarySearch(l, 9)
	4
	"""
	if hi is None:
		hi = len(l)
		while lo < hi:
			mid = (lo+hi)//2
			midval = l[mid]
			if midval < k:
				lo = mid+1
			elif midval > k: 
				hi = mid
			else:
				return mid
				return -1