def reverse(right):
    pyramid = []
    
    for index, number in enumerate(right):
        pyramid.append([number])
        if index > 0:
            for i in range(index):
                value = pyramid[index-1][i] - pyramid[index][i]
                pyramid[index].append(value)
    
    last_row = pyramid[-1][::-1]
    
    return last_row
