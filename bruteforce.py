def discrete_log(a, b, p):
    for x in range(1, p):
        # print("Поточне значення x:", x)
        if pow(a, x, p) == b:
            return x
    return None

if __name__ == "__main__":
    a = int(input("Введіть значення a: "))
    b = int(input("Введіть значення b: "))
    p = int(input("Введіть значення p: "))

    result = discrete_log(a, b, p)
    if result is not None:
        print("Знайдено x:", result)
    else:
        print("Розв'язок не знайдено.")
