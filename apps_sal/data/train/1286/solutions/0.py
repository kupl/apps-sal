import math


def main():
    IN = '11 6 5'
    z = IN.split()
    z = input().split()
    i = int(z[0])
    k = int(z[1])
    s = int(z[2])
    IN = '4 5'
    z = IN.split()
    z = input().split()
    a_i = int(z[0])
    b_i = int(z[1])
    x = math.sqrt(2)
    y = math.sqrt(3)
    if i <= k:
        diff = k - i
        if (k - i) % 2 == 0:
            ans = (a_i + b_i) * math.pow(2, 2 * (k - i) - s)
        else:
            ans = (2 * x * a_i + 2 * x * y * b_i) * math.pow(2, 2 * (k - (i + 1)) - s)
            diff = int(diff / 2)
            ans = (2 * x * a_i + 2 * x * y * b_i) * math.pow(2, 4 * diff - s)
    else:
        diff = i - k
        if (i - k) % 2 == 0:
            ans = (a_i + b_i) / math.pow(2, 2 * (i - k) + s)
        else:
            ans = (2 * x * a_i + 2 * x * y * b_i) / math.pow(2, 2 * (i + 1 - k) + s)
            diff = int(diff / 2)
            ans = (2 * x * a_i + 2 * x * y * b_i) / math.pow(2, 4 * diff + 4 + s)
    print(ans)


main()
