from sph import sph
from bruteforce import discrete_log
from time import time
while True:
    a = int(input('a:')) #44
    b = int(input('b:')) #451
    n = int(input('n:')) #719

    start = time()
    p = sph(a,b,n)
    end = time()

    print("[*] SPH found the power:")
    print("     x =",p)
    print("     time:", end-start)

    # start = time()
    # p = discrete_log(a,b,n)
    # end = time()

    # print("[*] Bruteforce found the power:")
    # print("     x =",p)
    # print("     time:", end-start)