# cook your dish here
testcases = int(input())
for x in range(testcases):
    N = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    print(A.count(0))
