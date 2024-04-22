# Метод пробних ділень 

from utils import bits, primes
import numpy as np

def __test_divisor(b_vector,m):
    r_vector = [1]
    for i in range(len(b_vector)-1):
        r_vector.append(r_vector[i]*2%m)
    r_vector = r_vector[::-1]
    return np.dot(b_vector,r_vector)%m == 0


def trial_division(n):
    
    max_prime = int(n**0.5)
    b_vector = bits(n)
    for prime in primes:
        if prime > max_prime: break;
        if __test_divisor(b_vector, prime): return True, [prime, n//prime]
        
    return False, [n]


if(__name__ == "__main__"):
    n = int(input("Enter number to factorize: "))
    factors = []
    f = True
    while f:
        (f,divisors) = trial_division(n)
        if(f): 
            factors.append(divisors[0])
            n = divisors[1]
        else:
            factors.append(n)
    print(factors)
        