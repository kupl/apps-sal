testcases = int(input())
for i in range(testcases):
    n = input()
    if '2' in n or '4' in n or '6' in n or ('8' in n) or ('0' in n):
        print(1)
    else:
        print(0)
