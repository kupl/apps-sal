import sys
# cook your dish here
T = int(input())
system = [0, 1]
new_multiplier = 1
while(len(system) < 110000):
    new_multiplier *= 6
    new_list = list(int(x + new_multiplier) for x in system)
    system += new_list
for t in range(T):
    N = int(input())
    print(system[N])
