from utils import legendre_validation, primes_extended, gcd
import numpy as np
import math

def bm_factorize(num, a=(2**0.5)/2):
    B = __get_B(num,a)
    solvers = __find_solvers(num,B)
    
    matrix = [x[2] for x in solvers]
    matrix = list(map(lambda x: list(map(lambda y: y%2,x)), matrix))
                    
    dependecies = __find_dependency(matrix) 
    return find_factor(solvers,dependecies,num, B)



def find_factor(solvers,dependecies, num, B):
    factor = 1
    for dependency in dependecies:
        X =  1
        for i in dependency:
            X = (X * solvers[i][0]) % num
        summarized_pow = [0]*(len(B) + 1)
        for i in dependency:
            for j in range(len(summarized_pow)):
                summarized_pow[j] += solvers[i][2][j]
        Y = 1
        for i in range(len(summarized_pow[1:])):
            Y = (Y * B[i]**(summarized_pow[i+1]//2)) % num
        for i in [1,-1]:
            res, _ ,_ = gcd(X + (Y * i), num)
            if res != 1 and res < num: return res
            
            
        
    return factor
        

def __find_dependency(matrix):
    m = len(matrix)
    n = len(matrix[0])
    
    pivot = [False]*m
    found = False
    
    map_pivot = {}  #column to row
    
    for j in range(n):
        found = False
        for i in range(m):
            if(matrix[i][j] == 1):
              pivot[i] = True
              map_pivot[j]=i
              found = True
              break
          
        if (found == True):
            for k in range(n):
                if(k == j):
                    continue
                if (matrix[i][k] == 1):
                    for row_index in range(m):
                        matrix[row_index][k] = (matrix[row_index][j] + matrix[row_index][k])%2
    
    solution = []
    for i in range(m):
        if (pivot[i] == False):
            dep_row = matrix[i]
            dependency = [i]
            for j,val in enumerate(dep_row):
                if (val==1):
                    dependency.append(map_pivot[j])
            solution.append(dependency)
    return solution
            

def __find_solvers(num,B):
    solvers = []
    a_vector = [0,0]
    b_vector = [0,1]
    b_sq_vector = [0,1]
    
    # 0 step
    alpha_0 = math.sqrt(num)
    a_0 = math.floor(alpha_0)
    v_0 = 1
    u_0 = a_0
    
    a_vector.append(a_0)
    b_vector.append(a_0)
    b_sq = pow(a_0,2,num)
    b_sq_vector.append(b_sq)
    
    flag,  vector = __is_solver(B,b_sq, num)
    if flag:
        solvers.append((a_0,b_sq,vector))
   
    
    while True:
        a,u_0,v_0 = __get_сontinued_fraction_coef(num,alpha_0,v_0,u_0)
        a_vector.append(a)
        b = (a * b_vector[-1] + b_vector[-2]) % num
        b_vector.append(b)
        b_sq = pow(b,2,num)
        b_sq_vector.append(b_sq)
        
        flag,  vector = __is_solver(B,b_sq, num)
        if flag:
            solvers.append((b,b_sq,vector))
            
        if(len(solvers) > len(B)+1): break
    
    return solvers


def __is_solver(B,n , f_n):
    vector = []
    i=0
    t = 0
    if(n > f_n //2): 
        n =  f_n-n
        vector.append(1)
    else: vector.append(0)
    
    while True:
        # print(B,n,i,t,vector)
        if i >= len(B): break
        if n % B[i] == 0:
            n = n//B[i]
            t += 1
        else:
            vector.append(t)
            t = 0
            i += 1
            
    if(len(vector) != len(B) + 1): vector.append(t)
    return n==1,vector

            
def __get_сontinued_fraction_coef(n,sqrt_n, v_0, u_0):
    v = (n-u_0**2)/v_0
    alpha = (sqrt_n + u_0)/(v)
    a = math.floor(alpha)
    u = a*v-u_0
    
    return a,u,v
    
def __get_B(n, a):
    B = []
    L = np.exp((np.log(n)*np.log(np.log(n)))**0.5) ** a
    for prime in primes_extended:
        if prime > L: break
        if legendre_validation(n,prime): B.append(prime)
    
    return B



if(__name__ == "__main__"):
    n = 1495056764861639599
    print(bm_factorize(n))
        