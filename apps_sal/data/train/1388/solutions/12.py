for _ in range(int(input())):
    n = int(input())
    tax = 0
    if n <= 250000:
        tax = n / 100 * 0 - 0
    elif n <= 500000:
        tax = (n - 250000) / 100 * 5 - 0
    elif n <= 750000:
        tax = (n - 500000) / 100 * 10 + 12500
    elif n <= 1000000:
        tax = (n - 750000) / 100 * 15 + 37500
    elif n <= 1250000:
        tax = (n - 1000000) / 100 * 20 + 75000
    elif n <= 1500000:
        tax = (n - 1250000) / 100 * 25 + 125000
    elif n > 1500000:
        tax = (n - 1500000) / 100 * 30 + 187500
    print(int(n - tax))
