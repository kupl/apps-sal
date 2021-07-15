def binary_simulation(bits, seq):
    arr = [0 for _ in range(len(bits) + 1)]
    display = []
    for grp in seq:
        if grp[0] == 'I':
            arr[grp[1] - 1] += 1
            arr[grp[2]] += -1
        else:
            display.append('01'[sum(arr[:grp[1]]) + int(bits[grp[1] - 1]) & 1])
    return display
