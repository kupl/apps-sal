# cook your dish here
for _ in range(int(input())):
    n = int(input())
    t = 0
    for i in range(1, n + 1):
        j = 0
        k = t + i
        while j < i:
            print(k, end="")
            t += 1
            j += 1
            k -= 1
        print("")
