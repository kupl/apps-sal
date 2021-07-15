def move_zeros(array):
        new_array = []
        for check in array:
             if check!=0 or isinstance(check,bool):
                    new_array.append(check)
        for cnt in range(abs(len(new_array)-len(array))):
                    new_array.append(0)
        return new_array

