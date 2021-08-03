# cook your dish here
num_cases = int(input())
for nidx in range(num_cases):
    z = input().split()
    n = int(z[0])
    m = int(z[1])
    print(n + m - 1)
