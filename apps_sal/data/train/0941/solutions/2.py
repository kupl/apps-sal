T = int(input())
while T > 0:
    x, y = list(map(int, input().split()))
    c_e_a = 0
    c_e_b = 0
    c_o_a = 0
    c_o_b = 0
    if(x == 1 and y == 1):
        print(1)
        break
    for i in range(1, x + 1):
        if i & 1:
            c_o_a += 1
        else:
            c_e_a += 1
    for j in range(1, y + 1):
        if j & 1:
            c_o_b += 1
        else:
            c_e_b += 1
    print(c_e_a * c_e_b + c_o_a * c_o_b)
    T -= 1
