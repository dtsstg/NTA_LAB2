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