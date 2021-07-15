def gimme(input_array):
    if input_array[2] > input_array[0] and input_array[2] > input_array[1]:
        if input_array[0] > input_array[1]:
            return 0
        else:
            return 1
    elif input_array[0] > input_array[1] and input_array[0] > input_array[2]:
          if input_array[1] > input_array[2]:
            return 1
          else:
            return 2
    elif input_array[2] > input_array[0]:
        return 2
    else:
        return 0

