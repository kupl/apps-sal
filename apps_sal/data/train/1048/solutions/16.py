for i in range(int(input())):
    a, K = list(map(int, input().split()))
    x = list(map(int, input().split()))
    x.sort()
    if((x[2] - K) - (x[0] + K) >= a):
        print("{0:.2f}".format(float(0.0)))
    else:
        if((x[2] - K) - (x[0] + K) <= 0):
            area = a * a
            print("{0:.2f}".format(float(area)))
        else:
            area = abs(x[0] - x[2] + 2 * K + a) * a
            print("{0:.2f}".format(float(area)))
