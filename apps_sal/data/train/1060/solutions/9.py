for t in range(int(input())):
    def csbstr(str, n, a, b):
        tot, c = 0, 0
        for i in range(n):
            if(str[i] == a):
                c += 1
            if(str[i] == b):
                tot += c
        return tot

    n = int(input())
    str = input()
    count1 = csbstr(str, n, "1", "0")
    count2 = csbstr(str, n, "0", "1")
    print(count1 + count2)
