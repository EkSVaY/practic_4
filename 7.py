k, a, s = map(int, input("Введите счёт команд: ").split(" "))

if k > a and k > s:
    print(k)
elif a > k and a > s:
    print(a)
elif s > k and s > a:
    print(s)
