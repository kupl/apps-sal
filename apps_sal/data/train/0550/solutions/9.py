try:
    def right_shift(x):
        temp = x + x
        return temp[len(x) - 1:2 * len(x) - 1]

    for i in range(int(input())):
        a, b = map(int, input().split(" "))
        a, b = bin(a)[2:], bin(b)[2:]

        if(len(a) < len(b)):
            diff = len(b) - len(a)
            a = "0" * diff + a
        elif(len(b) < len(a)):
            diff = len(a) - len(b)
            b = "0" * diff + b

        a = int(a, 2)
        maxi = a ^ int(b, 2)
        steps = 0

        for i in range(1, len(b)):
            b = right_shift(b)

            if(a ^ int(b, 2) > maxi):
                maxi = a ^ int(b, 2)
                steps = i

        print(steps, maxi)
except:
    pass
