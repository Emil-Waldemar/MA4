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

if __name__ == '__main__':
	main()
