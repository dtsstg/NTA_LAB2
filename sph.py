
from sympy.ntheory import factorint 
from utils import gcd

def get_r_table(factors,n,a):
    r = {}
    for key,value in factors.items():
        r[key] = []
        for j in range(key):
            power = n*j//key
            r[key].append(pow(a,power,n))
    return r

def find_x(factor,power, r_row,a,b,n):
    m = factor**power
    x_row = []
    x = 0
    for i in range(power):
        a_power = 0
        for j in range(i):
            a_power -= x_row[j]*(factor**j)
            a_power %= m
        b_power = n//(factor ** (i+1)) 
        
        v1 = pow(a,a_power,m)
        v = pow(b*v1,b_power,m)
        
        x_i = r_row.index(v)
        x_row.append(x_i)
        x += x_i * (factor ** i)
        x %= m
    
    return x


 
def solve_system(x, factors, n):            
    answer = 0
    if(len(x) == 1): return x[0]
    
    rs = [k**v for k,v in factors.items()]
    for i,v in enumerate(x):
        n_i = n //v
        _,inverse,_ = gcd(n_i,v)
        answer += rs[i]*n_i*inverse
        answer %= n
    return answer

def sph(a,b,n):
    factors = factorint(n)
    r = get_r_table(factors,n,a)
    
    x_row = []
    for f,p in factors.items():
        x_row.append(find_x(f,p,r[f],a,b,n))
    return solve_system(x_row,factors,n)
    
    
    
    
   