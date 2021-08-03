def disarium_number(number):
    num_list = list(str(number))
    return 'Disarium !!' if sum(int(num_list[i])**(i + 1) for i in range(len(num_list))) == number else 'Not !!'
