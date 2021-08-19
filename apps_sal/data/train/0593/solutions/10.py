# cook your dish here
t = int(input())
for _ in range(t):
    price = list(map(int, input().split()))
    string = set(input())
    letters = []
    cost = 0
    for i in range(97, 123):
        if chr(i) not in string:
            cost += price[i - 97]
    print(cost)
