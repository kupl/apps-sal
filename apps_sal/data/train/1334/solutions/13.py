# cook your dish here

N = int(input().strip())
activity_choices = [int(i) for i in input().strip().split(" ")]
stored_values = activity_choices[:3]
for i in range(3, N):
    stored_values.append(activity_choices[i] + min(stored_values[-1], stored_values[-2], stored_values[-3]))
print(min(stored_values[-1], stored_values[-2], stored_values[-3]))
