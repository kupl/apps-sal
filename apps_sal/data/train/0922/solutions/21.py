# cook your dish here
testcases = int(input())
for x in range(testcases):
    n, m = map(int, input().split())
    fb = list(map(int, input().split()))
    sb = list(map(int, input().split()))
    print(*sorted(list(set(fb) ^ set(sb))))
