# cook your dish here
for test in range(0, int(input())):
    A, B = map(int, input().split())
    diff = abs(A - B)
    count = 0
    if not(A ^ B):
        print(-1)
    else:
        for i in range(1, int(diff**(1 / 2)) + 1):
            if diff % i == 0:
                if diff / i == i:
                    count += 1
                else:
                    count += 2
        print(count)
