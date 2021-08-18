test_cases = int(input())
for i in range(0, test_cases):
    num_digits = int(input())
    input_str = input()
    digits_old = input_str.split()
    digits = []
    num_zero = 0
    for num in digits_old:
        if num == '0':
            num_zero += 1
        digits.append(int(num))
    if num_zero == 0:
        print(-1)
    else:
        digits.sort(reverse=True)
        flag = 1
        que0 = []
        que1 = []
        que2 = []
        sum_digits = 0
        for num in digits:
            if num % 3 == 0:
                que0.append(num)
            if num % 3 == 1:
                que1.append(num)
            if num % 3 == 2:
                que2.append(num)
            sum_digits += num
        if sum_digits % 3 == 0:
            number = 0
        elif sum_digits % 3 == 1:
            if len(que1) > 0:
                digits.remove(que1[len(que1) - 1])
            elif len(que2) > 1:
                digits.remove(que2[len(que2) - 1])
                digits.remove(que2[len(que2) - 2])
            else:
                print(-1)
                flag = 0
        else:
            if len(que2) > 0:
                digits.remove(que2[len(que2) - 1])
            elif len(que1) > 1:
                digits.remove(que1[len(que1) - 1])
                digits.remove(que1[len(que1) - 2])
            else:
                print(-1)
                flag = 0
        if flag == 1:
            number = 0
            for num in digits:
                number = number * 10 + num
            print(number)
