#Problem 19 (dailycodingproblem.com)
#This problem was asked by Facebook.
#A builder is looking to build a row of N houses that can be of K different colors. 
#He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.
#Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color, 
#return the minimum cost which achieves this goal.


import numpy as np

def get_min(matrix):

	a = np.asarray(matrix)
	cost = 0
	max_of_a = np.amax(a) # max value in whole matrix
	copy_of_a = a # this will help in returning the changed matrix to its original values 
	
	for n in range(a.shape[0]):  # n is row index. selecting one row after another
		cost = cost + np.amin(a[n])	
		min_elem_index = np.where(a[n]==np.amin(a[n])) 	# index of smallest element. 
														
		if n+1 < a.shape[0]:                           #this will ensure that no two neighboring houses are of the same colors
			a[n+1 ,min_elem_index[0]] = max_of_a
	a = copy_of_a			# returning original matrix

	return cost


x= [ [7, 3, 8, 6, 1, 2],
     [5, 6, 7, 2, 4, 3],
     [10, 1, 4, 9, 7, 6],
     [10, 1, 4, 9, 7, 6]]
 
min_x = get_min(x)

assert min_x == 8

