N = int(input())
while N:
    n = int(input())
    tax = 0
    if n <= 250000:
        tax = n * 0
    elif n > 250000 and n <= 500000:
        tax = (n - 250000) * 0.05
    elif n > 500000 and n <= 750000:
        tax = (n - 500000) * 0.1 + 12500
    elif n > 750000 and n <= 1000000:
        tax = (n - 750000) * 0.15 + 37500
    elif n > 1000000 and n <= 1250000:
        tax = (n - 1000000) * 0.2 + 75000
    elif n > 1250000 and n <= 1500000:
        tax = (n - 1250000) * 0.25 + 125000
    elif n > 1500000:
        tax = (n - 1500000) * 0.3 + 187500
    print(int(n - tax))
    N = N - 1
