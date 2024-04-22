from prime_test import prime_test
from  trial_division import trial_division
from pollard import pollard
from bm_method import bm_factorize
import time



def full_factorize(n):
    factors = []

    if prime_test(n,5): 
        factors.append(n)
        return factors
        
    found, divisors = trial_division(n)
    if found:
        print('trial divisor: ', divisors[0])
        n = divisors[1]
        factors.append(divisors[0])

        
    found,divisors = pollard(n)
    if(found):
        n = divisors[1]
        factors.append(divisors[0])
        print('pollard: ',divisors[0])

            
        if prime_test(n,5): 
            factors.append(n)
            return factors
        
    while n != 1:
        factor = bm_factorize(n)
        
        if factor == 1:
            print('BM method gave me 1')
            return factors
        
        factors.append(factor)
        n = n//factor
        print('BM: ', factor)
        
        if prime_test(n,5): 
            factors.append(n)
            return factors
    

# task 3
n = int(input('Enter number to factorize: '))
start = time.time()
factors = full_factorize(n)
end = time.time()

print("Factorizing number: ",n,"\nExecution Time: ",end-start,"\nFactorized number: ",factors,"\n\n\n")


# task 6

# numbers_list = [3009182572376191, 1021514194991569, 4000852962116741, 15196946347083, 499664789704823, 269322119833303, 679321846483919, 96267366284849, 61333127792637, 2485021628404193]  

# for number in numbers_list:
#     x_0 = 1
#     start = time.time()
#     while True:
#         res, divisors = pollard(number,x_0)
#         if res: break
#         x_0 += 1
#     end = time.time()
#     print("Factorizing number: ",number,"\nMethod name: Pollard","\nExecution Time: ",end-start,"\nDivisor found: ",divisors[0],"\n\n\n")
    
#     a=(2**0.5)/2
#     start = time.time()
#     while True:
#         res = bm_factorize(number,a)
#         if res == 1:
#             a+=0.01
#         else:break
        
#     end = time.time()
#     print("Factorizing number: ",number,"\nMethod name: BM","\nExecution Time: ",end-start,"\nDivisor found: ",res,"\n\n\n")
