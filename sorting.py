""" sortingLibrary.py
	Implements various common sorting algorithms and compares their
	running times using the time module. Included algorithms:
	
	- Bubble sort
	- Insertion sort
	- Merge sort
	- Quick sort
	
"""

import random
import time

def bubbleSort(arr):
	a = arr	# Copy the array so that we aren't just modifying in-place
	# Implements the bubble sort algorithm
	for i in range(len(a)):
		for j in range(i + 1, len(a)):
			if a[i] > a[j]:
				a[i], a[j] = a[j], a[i]
			
	return arr
	
def insertionSort(arr):
	# Implements the insertion sort algorithm
	sorted_arr = [arr[0]]
	
	for a in arr:
		insertion_index = 0
		# Can be substantially accelerated by using binary search here
		while insertion_index < len(sorted_arr) and a > sorted_arr[insertion_index]:
			insertion_index += 1
			
		sorted_arr = sorted_arr[:insertion_index] + [a] + sorted_arr[insertion_index:]
	return sorted_arr
	
def mergeSort(arr):
	# Implements the merge sort algorithm
	def merge(a, b):
		# Merge two presorted arrays and return
		# Preallocate c to be long enough
		
		c = [0]*(len(a) + len(b))
		a_ptr = 0
		b_ptr = 0
		while a_ptr < len(a) and b_ptr < len(b):
			if a[a_ptr] <= b[b_ptr]:
				c[a_ptr + b_ptr] = a[a_ptr]
				a_ptr += 1
			else:
				c[a_ptr + b_ptr] = b[b_ptr]
				b_ptr += 1
		
		# Handle any leftovers
		if a_ptr == len(a):
			while b_ptr < len(b):
				c[a_ptr + b_ptr] = b[b_ptr]
				b_ptr += 1
		
		if b_ptr == len(b):
			while a_ptr < len(a):
				c[a_ptr + b_ptr] = a[a_ptr]
				a_ptr += 1
				
		return c
		
	# Implement the merge sort algorithm
	if len(arr) == 1:
		return arr
		
	# Recurse		
	return merge(mergeSort(arr[0:len(arr) // 2]), mergeSort(arr[len(arr)//2:]))
		
def quickSort(arr):
	# Implement the quicksort algorithm
	
	if len(arr) < 2:
		return arr
	
	# Choose pivot to be the middle element in the array
	# Avoids issues with pre-sorted lists
	
	pivot = arr[len(arr) // 2]
	
	# Partition the rest of the array to form high, low
	high = list(filter(lambda x : x > pivot, arr[1:]))
	low = list(filter(lambda x : x <= pivot, arr[1:]))
	
	# Recurse
	return quickSort(low) + [pivot] + quickSort(high)
	
def test(algorithm, arr):
	# Run the specified sorting algorithm on the given array
	# Return the execution time in milliseconds
	start = time.perf_counter_ns()
	algorithm(arr)
	end = time.perf_counter_ns()
	
	return (end - start) // 10**6
			
if __name__ == '__main__':
	
	# Generate a random array to test
	# Default length: 10,000 entries
	array_length = 10**4
	arr = [random.random() for _ in range(array_length)]
	
	# Report how long it takes to execute each
	algorithms = [bubbleSort, insertionSort, mergeSort, quickSort]
	#algorithms = [mergeSort, quickSort]
	print(f'Testing a randomly generated array with {array_length} entries:')
	
	for a in algorithms:
		print(f'Using {a.__name__}: {test(a, arr)} milliseconds')