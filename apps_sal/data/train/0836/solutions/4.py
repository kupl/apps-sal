t = int(input())

for e in range(t):

    n = int(input())
    l_str = input()
    r_str = input()

    l_str = l_str.strip().split(" ")
    r_str = r_str.strip().split(" ")

    max_p = 0
    for i in range(len(l_str)):
        if int(l_str[i]) * int(r_str[i]) > max_p:
            max_p = int(l_str[i]) * int(r_str[i])

    max_r = 0
    for i in range(len(l_str)):
        if int(l_str[i]) * int(r_str[i]) >= max_p:
            if int(r_str[i]) > max_r:
                max_r = int(r_str[i])

    for i in range(len(l_str)):
        if int(l_str[i]) * int(r_str[i]) >= max_p and int(r_str[i]) >= max_r:
            print(i + 1)
            break
