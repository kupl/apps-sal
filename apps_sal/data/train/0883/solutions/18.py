t = int(input())
for i in range(t):
    number_of_students = int(input())
    list_of_numbers = list(map(int, input().split(' ')))
    max_number = max(list_of_numbers)
    min_number = min(list_of_numbers)
    if max_number < number_of_students and min_number > -1 and (abs(max_number - min_number) <= 1):
        sum_of_values = sum(list_of_numbers)
        if number_of_students == 1:
            print(-1)
        elif sum_of_values % (number_of_students - 1) != 0:
            print(-1)
        else:
            print(number_of_students - sum_of_values // (number_of_students - 1))
    else:
        print(-1)
