def find_average(my_list):
    sum = 0
    count = 0
    
    for number in my_list:
        count = count + 1
        # count += 1
        sum = sum + number
        # sum += number
        
    average = sum / count
        
    return average

# sum = 5, 13, 15
# count = 1, 2, 3

