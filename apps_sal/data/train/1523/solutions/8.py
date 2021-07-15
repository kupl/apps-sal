# cook your dish here

N = int(input().strip())
incomes = []
total_sum = 0
for i in input().strip().split(" "):
    incomes.append(int(i))
    total_sum += int(i)

stored_values = incomes[:3]
for i in range(3, N):
    stored_values.append(incomes[i] + min(stored_values[-1], stored_values[-2], stored_values[-3]))

print(total_sum - min(stored_values[-1], stored_values[-2], stored_values[-3]))

