def interpreter(tape, array):
    stepArray = 0
    stepTape = 0
    arr = list(array)

    while(stepArray < len(array)):
        if(tape[stepTape % len(tape)] == "1"):

            arr[stepArray] = "1" if arr[stepArray] == "0" else "0"
        else:
            stepArray += 1
        stepTape += 1

    return ''.join(arr)
