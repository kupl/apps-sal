import math


def lcm(s, s1):
    mul = s * s1
    gcd = math.gcd(s, s1)
    lcm = mul // gcd
    return lcm

# Driver Code


def __starting_point():

    t = int(input())  # take the size
    while(t > 0):
        t = t - 1
        N = int(input())  # take the size
        num_array = list(map(int, input().split(' ')[:N]))
        # for i in range(N):
        #n = int(input())
        #num_array[i] = n
        l = num_array[0]
        for i in range(1, N):
            l = lcm(l, num_array[i])
        r = int(input())
        print(l + int(r))


__starting_point()
