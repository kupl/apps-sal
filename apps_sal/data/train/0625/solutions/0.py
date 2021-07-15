def subCount(arr, n, k):

    mod = []
    for i in range(k + 1):
        mod.append(0)


    cumSum = 0
    for i in range(n):
        cumSum = cumSum + arr[i]

        # as the sum can be negative,
        # taking modulo twice
        mod[((cumSum % k) + k) % k] = mod[((cumSum % k) + k) % k] + 1

    result = 0  # Initialize result

    for i in range(k):


        if (mod[i] > 1):
            result = result + (mod[i] * (mod[i] - 1)) // 2


    result = result + mod[0]

    return result
t=int(input())
while t:
    t=t-1
    n=int(input())
    a=list(map(int,input().split()))
    for i in range(n):
        if a[i]==100000000:
            a[i]=1
        elif a[i]==900000000:
            a[i]=9
    s=10

    print(subCount(a,n,s))

