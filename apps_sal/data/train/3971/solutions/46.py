def tidyNumber(n):
    previous_number = 0
    for number in str(n):
        if previous_number > int(number):
            return False
        previous_number = int(number)
    return True
