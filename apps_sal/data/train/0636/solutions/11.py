# cook your dish here
inp = list(map(int, input().split()))
N = inp[0]
T = inp[1]
array = inp[2:]
array.sort()

sums = [0 for i in range(T)]
total = 0
for i in range(N):
    for forward in range(i + 1, N):
        sm = array[i] + array[forward]
        if sm < T:
            total += sums[T - sm]
    for backward in range(i):
        sm = array[i] + array[backward]
        if sm < T:
            sums[sm] += 1
print(total)
