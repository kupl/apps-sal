# cook your dish here
testcases = int(input())
for x in range(testcases):
    n = int(input())
    count = 1
    for x in range(n, 0, -1):
        for y in range(x, 0, -1):
            print(count, end="")
            count += 1
        print()
