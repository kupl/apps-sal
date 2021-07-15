def multiple_of_index(arr):
    output = []
    for index_, value in enumerate(arr):
        try: 
            if value % index_ == 0:
                output.append(value)
        except ZeroDivisionError:
            continue
    return output
