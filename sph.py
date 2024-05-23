
from sympy.ntheory import factorint 
from functools import reduce


def get_r_table(factors,n,a):
    r = {}
    for key,value in factors.items():
        r[key] = []
        for j in range(key):
            power = (n-1)*j//key
            r[key].append(pow(a,power,n))
    return r

def find_x(factor,power, r_row,a,b,n):
    m = pow(factor,power,n)
    x_row = []
    x = 0
    for i in range(power):
        a_power = 0
        for j in range(i):
            a_power -= x_row[j]*(factor**j)
            a_power %= m
        b_power = (n-1)//(factor ** (i+1)) 
        
        v1 = pow(a,a_power,n)
        v = pow(b*v1,b_power,n)
        x_i = r_row.index(v)
        x_row.append(x_i)
        x += x_i * (factor ** i)
        x %= m
    
    return x


 
def solve_system(x, factors):            
    m = []
    for k in factors:
        m.append(k**factors[k])
    sum = 0
    prod = reduce(lambda acc, b: acc*b, m)
    for n_i, a_i in zip(m, x):
        p = prod // n_i
        sum += a_i * pow(p,-1,n_i) * p
    return sum % prod
 
   
   

def sph(a,b,n):
    factors = factorint(n-1)
    r = get_r_table(factors,n,a)

    x_row = []
    for f,p in factors.items():
        x_row.append(find_x(f,p,r[f],a,b,n))
    return solve_system(x_row,factors)
    
    
    
    
   