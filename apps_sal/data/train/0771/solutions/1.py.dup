t = eval(input())
while t:
    n = eval(input())
    m, f = list(map(int, input().split()))
    multan = 0
    total = 0
    fultan = 0
    s = list(map(int, input().split()))
    for i in s:
        if i == 0:
            continue
        if i % m == 0:
            multan += 1
            total += 1
        elif i % f == 0:
            fultan += 1
            total += 1
    if total - 0.7 * n >= 0.0:
        print("Yes")
        if multan > fultan:
            print("Multan")
        elif fultan > multan:
            print("Fultan")
        else:
            print("Both")
    else:
        print("No")
    # print total,multan,fultan
    t -= 1
