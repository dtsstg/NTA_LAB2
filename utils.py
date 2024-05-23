def gcd(a, b):
        u = 0
        u_ = 1
        v = 1
        v_ = 0
        r = b
        r_ = a

        while r != 0:
            q = r_ // r
            r_, r = r, r_ - q * r
            u_, u = u, u_ - q * u
            v_, v = v, v_ - q * v
        return r_, u_, v_
    
def horner_pow(a, b, m):
        b_bits = bits(b)
        y = 1
        for bit in b_bits:
            y = (y ** 2) % m
            y = y * (a ** bit) % m

        return y
    
def bits(n):
    return [int(digit) for digit in bin(int(n))[2:]]