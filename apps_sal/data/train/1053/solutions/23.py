# cook your dish here
testcases = int(input())
for x in range(testcases):
    N = int(input())
    A = list(map(int, input().split()))
    print(A.count(0))
