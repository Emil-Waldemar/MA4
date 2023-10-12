#!/usr/bin/env python3

from person import Person
from numba import njit
from time import perf_counter as pc

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
 
 
	start_py = pc()
	print(fib_py(4))
	end_py = pc()
	print(f"Time with python: {round(end_py - start_py, 6)} s")
	start_numba = pc()
	print(numba_fib(47))
	end_numba = pc()
	print(f"Time with numba: {round(end_numba - start_numba, 6)} s")
	
	start_c = pc()
	fib = f.fib(47)
	end_c = pc()
	print(f"Time with c++: {end_c - start_c}")
 
	a = 1
	
 

if __name__ == '__main__':
	main()
