for _ in range(int(input())):
    n = int(input())
    lst = []
    for i in range(n):
        original_price, quantity, discount = [*map(int, input().strip().split())]
        increased_price = original_price + ((discount / 100) * original_price)
        reduced_price = increased_price - ((discount / 100) * increased_price)
        lst.append((abs(original_price - reduced_price)) * quantity)
    print("{:.9f}".format(sum(lst)))
