def f(x):
    a = []
    i = 0
    f = 1
    while x % 10 > 0:
        k = x % 10
        x = x // 10
        a.append(k)
        if a[i] % 2 == 0:
            f *= 1
        else:
            f *= 0
        i += 1

    print(a)
    if f == 1:
        return False  # четное
    else:
        return True  # нечетное


f(13579)
