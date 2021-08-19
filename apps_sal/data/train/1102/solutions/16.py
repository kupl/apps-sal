# cook your dish here
constant = (10**9) + 7
try:
    testCases = int(input().strip())
    for _ in range(testCases):
        total = 1
        ip = list(input().strip())
        for i in ip:
            if i in ['7', '9']:
                total *= 4
            else:
                total *= 3
        print(total % constant)
except EOFError:
    pass
