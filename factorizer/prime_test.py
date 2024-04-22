# Імовірнісний тест Міллера-Рабіна

import random
from utils import bits, horner_pow


def prime_test(num, k):
        if num == 2 or num == 3: return True
        if num < 5 or num % 2 == 0: return False
        # step 0
        d = num - 1
        s = 0

        while d % 2 == 0:
            d = d // 2
            s += 1

        for _ in range(k):
            # step 1
            a = random.randint(2, num - 1)
            b0 = horner_pow(a, d, num)
            c = d
            while c != num - 1:
                if b0 == 1 or b0 == num - 1: break;
                b = (b0 ** 2) % num
                if b == 1: return False
                b0 = b
                c = c * 2
            if c == num - 1: return False
        # step 3
        return True



if(__name__ == "__main__"):
    n = int(input("Enter number to test: "))
    print(prime_test(n,10))