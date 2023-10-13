<<<<<<< HEAD

'''
Reviewed by :Stephan Spengler
Student: Emil Waldemar Petersson
date: 13.okt 2023
email: emil-waldemar.petersson.3310@student.uu.se
'''


=======
'''
Student: Emil Waldemar Petersson
email: emil-waldemar.petersson.3310@student.uu.se
Reviewed by: Stephan Spengler
Date: 13.okt 2023
'''



>>>>>>> da0744f13d75ab957d88b121dbe3d58c72950f3e
import math
import matplotlib.pyplot as plt
import random as rd
import os
import numpy as np
from time import perf_counter as pc
import concurrent.futures as futures



def approx_pi(n):
    
    
    lst_points = [(np.random.uniform(-1,1), np.random.uniform(-1,1)) for i in range(n)]
    colors = []
    points_in_circle = []
    number_of_points_in_circle = 0
   
    for point in lst_points:
        in_circle = point[0]**2 + point[1]**2 <= 1
        color = 'red' if in_circle else 'blue'
        if in_circle:
            points_in_circle.append(point)
        colors.append(color)
    
    for i in range(len(points_in_circle)):
        number_of_points_in_circle += 1
            
    my_pi = 4 * len(points_in_circle)/ n
    
    print(f"For n = {n}")
    print(f"Simulated pi: {my_pi}, pi: {round(math.pi, 5)}")
    print('===================================================')
    return
    plt.scatter(*zip(*lst_points),color=colors)
    plt.show()
   
    

def create_multidim_list(n,dim):
    lst = list(zip(*[np.random.uniform(-1,1,n) for i in range(dim)]))
    in_sphere = lambda x: sum([i**2 for i in x]) <= 1
    return [point for point in lst if in_sphere(point)]
    

"""
def point_is_in_sphere(lst):
    in_sphere = lambda x: sum([i**2 for i in x]) <= 1
    return [point for point in lst if in_sphere(point)]
 
"""

def approx_hyp(n,dim):
    lst_points = create_multidim_list(n,dim)
    
    #points_in_sphere = point_is_in_sphere(lst_points)
    
    V_approx = (2**dim) * (len(lst_points)/n)
    
    print(f"For n = {n} and dim = {dim}")
    print(f"Volume approximation = {V_approx},  Actual: {round((math.pi**(dim/2)) / (math.gamma((dim/2) + 1)), 5)}")
    print('===================================================')
    
def approx_hyp_parallell(args):
    n, dim, thread_nums = args
    
    with futures.ProcessPoolExecutor(max_workers=thread_nums) as executor:
        lst = executor.map(create_multidim_list, [n]*thread_nums, [dim]*thread_nums)
        lst = [point for sublist in lst for point in sublist]
        
    
    V_approx = (2**dim) * (len(lst)/n)
    print(f"For n = {n} and dim = {dim}")
    print(f"Volume approximation = {V_approx},  Actual: {round((math.pi**(dim/2)) / (math.gamma((dim/2) + 1)), 5)}")
    print('===================================================')
    

def main():
    os.system('clear')
    
    print("############## PI approxiamation ###############")
    print('')
    pi_tests = [1000, 10_000, 100_000]
    for num in pi_tests:
        approx_pi(num)

    print('\n\n')

    print("############## Hyper Sphere approxiamation ###############")
    print('')
    hyp_test = [(100_000,2), (100_000,11)]
    for n,dim in hyp_test:
        approx_hyp(n,dim)
    
    print('\n\n')
    
    print("############## Hyper with Parallel ###############")
    print('')
    start = pc()
    approx_hyp(10_000_000, 11)
    stop = pc()
    print(f'Time without parallell programming: {round(stop - start, 8)}s')
    print('===================================================')
    
    args = [1_000_000, 11, 10] 
    start_parallel = pc()
    approx_hyp_parallell(args)
    end_parallel = pc()
    print(f'Time with parallell programming: {round(end_parallel - start_parallel, 8)}s')
    print('\n\n')
    



if __name__ == "__main__":
    main() 

