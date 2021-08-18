def find_average(my_list):
    sum = 0
    count = 0

    for number in my_list:
        count = count + 1
        sum = sum + number

    average = sum / count

    return average
