test_case = int(input())
for i in range(test_case):
    (apple, orange, coin) = map(int, input().split())
    k = abs(apple - orange)
    if k >= coin:
        print(k - coin)
    else:
        print(0)
