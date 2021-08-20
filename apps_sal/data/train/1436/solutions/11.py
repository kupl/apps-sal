t = int(input())
while t:
    h = input()
    if len(h) % 2:
        if h[:int(len(h) / 2)] == h[int(len(h) / 2) + 1:][::-1]:
            print(1)
        else:
            print(2)
    elif h[:int(len(h) / 2)] == h[int(len(h) / 2):][::-1]:
        print(1)
    else:
        print(2)
    t -= 1
