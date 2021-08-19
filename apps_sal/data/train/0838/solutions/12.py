# cook your dish here
t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))

    temp, speed = l[0], l[0]

    for i in range(1, n):

        if temp < l[i]:

            speed += l[i] - temp
            temp = speed - i - 1

        else:
            temp -= 1

    print(speed)
