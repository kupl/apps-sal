for i in range(int(input())):
    n = int(input())
    if(n <= 2 or n > 1000000007):
        print("0")
    else:
        prod = 1
        for i in range(2, n):
            prod *= i
            if(prod > 1000000007):
                prod = prod % 1000000007
        print(((prod) * (n * prod - 2)) % 1000000007)
