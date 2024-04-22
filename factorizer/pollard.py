from utils import gcd

def __f(x,m):
    return ( x**2 + 1) % m


def __iteration(x,y,m):
    x = __f(x,m)
    y = __f(__f(y,m),m)
    d,_,_ = gcd(x-y,m)
    return x,y,d


def pollard(n, x_0=1):
    x,y,d = __iteration(x_0,x_0,n)
    
    while d == 1 and x != y:
        x,y,d = __iteration(x,y,n)
        
        
    if x == y: return False, [n]
    return True, [d,n//d]
        
        
if(__name__ == "__main__"):
    n = int(input("Enter number to factorize: "))
    print(pollard(n))
    