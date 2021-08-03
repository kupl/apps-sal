T = int(input())
for t in range(T):
    conf = input()
    if len(conf) % 2 == 0:
        print("Aleksa")
    else:
        if conf.find('W') == (len(conf) - 1) / 2:
            print("Chef")
        else:
            print("Aleksa")
