for _ in range(int(input())):
    temp = list(input().split())
    n = int(temp[0])
    s = temp[1]
    du, de = 0, 0
    for _ in range(n):
        mc = input()
        if mc[0] == '1':
            du += mc.count('1')
        else:
            de += mc.count('0')
    if de > du:
        print("Dee")
    elif de < du:
        print("Dum")
    else:
        if s == "Dee":
            print("Dum")
        else:
            print("Dee")
