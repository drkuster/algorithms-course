def karatsuba(x, y, n, a = 0, b = 0, c = 0, d = 0, step = 0):
    if (step == 0):
        a = x // (10 ** (n // 2))
        c = y // (10 ** (n // 2))
        return ((10 ** n) * a * c) + karatsuba(x, y, n, a, 0, c, 0, 1)
    elif (step == 1):
        b = x % (10 ** (n // 2))
        d = y % (10 ** (n // 2))
        return (b * d) + karatsuba(x, y, n, a, b, c, d, 2)
    elif (step == 2):
        last = ((a + b) * (c + d)) - (a * c) - (b * d)
        return ((10 ** (n // 2)) * last)

print(karatsuba(12345, 67890, 4))