def tax(n):
    if(n <= 250000):
        return 0
    elif(n <= 500000):
        return (n - 250000) * 5 // 100
    elif(n <= 750000):
        return 2500 * 5 + (n - 500000) * 10 // 100
    elif(n <= 1000000):
        return 2500 * (5 + 10) + (n - 750000) * 15 // 100
    elif(n <= 1250000):
        return 2500 * (5 + 10 + 15) + (n - 1000000) * 20 // 100
    elif(n <= 1500000):
        return 2500 * (5 + 10 + 15 + 20) + (n - 1250000) * 25 // 100
    else:
        return 2500 * (5 + 10 + 15 + 20 + 25) + (n - 1500000) * 30 // 100


for T in range(int(input())):
    income = int(input())
    total_tax = tax(income)
    print(income - total_tax)
