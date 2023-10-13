#!/usr/bin/env python3

from person import Person
from numba import njit
from time import perf_counter as pc
import matplotlib.pyplot as plt

def fib_py(n):
    if(n <= 1):
        return n
    else:
        return (fib_py(n-1) + fib_py(n-2))
    
@njit 
def numba_fib(n: int):
    if n <= 1:
        return n
    else: 
        return (numba_fib(n-1) + numba_fib(n-2))

def main():
	f = Person(5)
	print(f.get())
	f.set(7)
	print(f.get())
	
	test_set = list(range(20,31))
	py_fib = []
	nb_fib = []
	cpp_fib = []
	
	#print(numba_fib(47)) # --> 2971215073
	f = Person(47)  
	print(f.fib()) # -->  2971215073
	'''
	for i in test_set:
		start_py = pc()
		fib_py(i)
		end_py = pc()
		py_fib.append(round(end_py - start_py, 6))
		print(f"Time with just Python for fib({i}): {round(end_py - start_py, 6)}")
	'''
	'''
	for i in test_set:
		start_nb = pc()
		numba_fib(i)
		end_nb = pc()
		nb_fib.append(round(end_nb - start_nb,6))
		print(f'Time with Numba: {round(end_nb - start_nb, 6)}')
	'''

	'''
	for i in test_set:
		f = Person(i)
		start_cpp = pc()
		f.fib()
		end_cpp = pc()
		cpp_fib.append(round(end_cpp - start_cpp,6))
		print(f'Time with C++: {round(end_cpp - start_cpp, 6)}')	
	'''

	print('========== Python times ===========')
	print(py_fib)
	
	print('========== Numba times ===========')
	print(nb_fib)
 
	#print('========== C++ times ===========')
	#print(cpp_fib)
 
	'''
	# Plotting the data
	plt.figure(figsize=(10, 6))
	plt.plot(test_set, py_fib, marker='o', label='Python')
	plt.plot(test_set, nb_fib, marker='o', label='Numba')
	#plt.plot(test_set, cpp_fib, marker='o', label='C++')

	# Adding labels and title
	plt.xlabel('n')
	plt.ylabel('Time (seconds)')
	plt.title('Timing Comparisons between Python and Numba Implementations for Fibonacci Sequence')
	plt.legend()
	plt.grid(True)
	plt.yscale('log')  # Using a log scale due to the wide range of time values
	plt.xticks(test_set)  # Explicitly set x-ticks to ensure all n_values are labeled

	# Save the figure
	#plt.savefig('fibonacci_timing_comparison_numba_py.png')
	'''
 
if __name__ == '__main__':
	main()
