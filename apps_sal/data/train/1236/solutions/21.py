for _ in range(int(input())):
    lens = int(input())
    inps = input()
    stck = [inps[0]]
    need = 0
    for i in range(1, lens):
        if inps[i] == stck[-1]:
            need += 1
        else:
            stck.append(inps[i])
    print(need)
