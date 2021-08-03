# cook your code here
test_cases = int(input())
for case in range(test_cases):
    copies = int(input())
    line = input().split()
    speeds = [int(s_car) for s_car in line]
    count = 0
    for loop in range(1, copies + 1):
        if (speeds[loop] > speeds[0]):
            count = count + 1
    print(count)
