will_do = 0
for _ in range(int(input())):
 will_do += sum([int(x) for x in input().split()]) >= 2
print(will_do)

