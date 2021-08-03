arr = [0] * 6

arr[1] = 250000 * (0.05)
arr[2] = 250000 * (0.10)
arr[3] = 250000 * (0.15)
arr[4] = 250000 * (0.20)
arr[5] = 250000 * (0.25)

for _ in range(int(input())):
    n = int(input())

    tax = 0

    if n <= 250000:
        tax = 0

    elif 250000 < n <= 500000:
        tax = sum(arr[:1])

        rem = n - 250000

        tax += (rem) * (0.05)

    elif 500000 < n <= 750000:
        tax = sum(arr[:2])

        rem = n - 500000

        tax += (rem) * (0.10)

    elif 750000 < n <= 1000000:
        tax = sum(arr[:3])

        rem = n - 750000

        tax += (rem) * (0.15)

    elif 1000000 < n <= 1250000:
        tax = sum(arr[:4])

        rem = n - 1000000

        tax += (rem) * (0.20)

    elif 1250000 < n <= 1500000:
        tax = sum(arr[:5])

        rem = n - 1250000

        tax += (rem) * (0.25)

    elif n > 1500000:
        tax = sum(arr[:6])

        rem = n - 1500000

        tax += (rem) * (0.30)

    res = int(n - tax)

    print(res)
