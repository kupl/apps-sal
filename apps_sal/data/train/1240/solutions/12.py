# cook your dish here
testcases = int(input())
for x in range(testcases):
    size = int(input())
    li = list(map(int, input().split()))
    li2 = [n - (6 * (n // 6)) if n % 6 != 0 else 6 for n in li]
    print(sum(li2))
