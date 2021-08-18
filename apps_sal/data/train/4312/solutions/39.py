def pick_peaks(arr):
    pos = []
    peaks = []
    plateau = []

    numbers = len(arr)
    print("length of array: " + str(numbers))
    print("list:")
    print(arr)

    for number in range(numbers):
        if number == 0 or number == (numbers - 1):
            pass
        else:
            candidate = arr[number]
            pre = arr[(number - 1)]
            post = arr[(number + 1)]
            if candidate > pre and candidate > post:
                pos.append(number)
                peaks.append(candidate)
            elif number == 1 or number == (numbers - 2):
                pass
            elif candidate > pre and candidate == post:
                if candidate >= arr[(number + 2)] and number != (number - 1) and candidate != arr[(numbers - 1)]:
                    pos.append(number)
                    peaks.append(candidate)
                else:
                    pass
    print("plateau:")
    print(plateau)
    answer = {}
    answer["pos"] = pos
    answer["peaks"] = peaks
    print(answer)
    return answer
