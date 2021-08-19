# cook your dish here
for test in range(int(input())):
    n = int(input())
    ar = list(map(int, input().split()))

    count = 0
    for item in ar:
        if bin(item)[-1] == '0':
            count += item

    print(count)
