for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    if l[0] == 1 and l[-1] == 1 and n % 2 != 0 and l[n // 2] == max(l):
        for i in range(n // 2):
            if abs(l[i + 1] - l[i]) != 1:
                print("no")
                break
        else:
            print("yes")
    else:
        print("no")
