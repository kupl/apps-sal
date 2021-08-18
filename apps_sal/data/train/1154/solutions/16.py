n = int(input())
n_numbers = list(map(int, input().split()))
n1_numbers = list(map(int, input().split()))
sum1 = 0
sum2 = 0
sum3 = 0
for i in range(len(n_numbers)):
    sum1 = sum1 + n_numbers[i]
for j in range(len(n1_numbers)):
    sum2 = sum2 + n1_numbers[j]
sum3 = sum2 - sum1
print(sum3)
