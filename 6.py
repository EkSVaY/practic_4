score_f, score_s = map(int, input("Введите счёт команд: ").split(":"))

if score_f > score_s:
    print("1")
elif score_f < score_s:
    print("2")
else:
    print("0")
