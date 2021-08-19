t = int(input())
for i in range(t):
    nums = [int(x) for x in input().strip().split(' ')]
    stairs = 2 ** 0.5 * nums[0] / nums[1]
    elevator = 2 * nums[0] / nums[2]
    if stairs <= elevator:
        print('Stairs')
    else:
        print('Elevator')
