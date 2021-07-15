def get_average(marks):
    result = 0
    counter = 0
    
    for item in marks:
        result += item
        counter += 1
    
    return int(result / counter)

