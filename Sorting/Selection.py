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
import numpy as np
from time import time
from random import choice
import matplotlib.pyplot as plt
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

def Histogram(listStep, testSize):
	""""""
	# Number of time each step is recalculated for average
	averagN = 10

	xAxis = []
	yAxis = []

	for i in range(testSize):
		elapsedList = []
		step = listStep * (i + 1)
		l = RandomList(step, 0, step)
		for j in range(averagN):
			# Start time
			start = time()
			# Run Selection
			Selection(l, choice(range(len(l))) + 1)
			# Calculate time
			elapsedList.append(time() - start)

		# Add time to results
		xAxis.append(step)
		# Get the average result
		yAxis.append(reduce(lambda x, y: x + y, elapsedList) / float(len(l)))

	pos = np.arange(len(xAxis))
	width = 1.0

	ax = plt.axes()
	ax.set_xticks(pos + (width / 2))
	ax.set_xticklabels(xAxis)

	plt.bar(pos, yAxis, width, color='r')
	plt.show()



