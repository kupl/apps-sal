# cook your dish here
for test in range(int(input())):
    s = input().strip()

    if not len(s) % 2:
        mid = len(s) // 2
        first = s[:mid]
        second = s[mid:]
    else:
        mid = len(s) // 2
        first = s[:mid]
        second = s[mid + 1:]

    second = second[::-1]

    cost = 0
    for i in range(len(first)):
        cost += abs(ord(first[i]) - ord(second[i]))

    print(cost)
