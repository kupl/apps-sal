
def calc_x(y, num):
    return (num - 4 * y) / 7.0


num_test_cases = int(input())


for i in range(num_test_cases):
    num = int(input())
    current_y = 0
    result_x = 0
    while result_x >= 0:
        result_x = calc_x(current_y, num)
        if result_x % 1 == 0:
            break
        current_y += 1
    if result_x < 0 and current_y > 0:
        print(-1)
    else:
        print(int(result_x * 7))
