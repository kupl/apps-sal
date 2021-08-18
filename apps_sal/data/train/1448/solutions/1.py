try:
    for i in range(int(input())):
        inp = list(map(int, input().split()))

        for i in range(2, inp[3] + 1):
            if inp[3] == 1:
                break
            inp[0] += inp[1]
            if int(i % inp[2]) == 0:
                inp[1] += inp[4]

        print(inp[0])
except:
    pass
