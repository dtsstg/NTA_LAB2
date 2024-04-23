from sph import sph
from time import time

a = int(input('a:')) #44
b = int(input('b:')) #451
n = int(input('n:')) #719

start = time()
p = sph(a,b,n)
end = time()

print("[*] SPH found the power:")
print("     x =",p)
print("     time:", end-start)