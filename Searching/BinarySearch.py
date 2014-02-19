# @auther Besir Kurtulmus
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