T = int(input())
for j in range(0, T):
    line1, line2 = input(), input()
    seq = line2.split()
    current_min = 1000001
    current_max = 0
    max_spread = 0
    for i in range(0, len(seq)):
        current_value = int(seq[i])
        if current_min > current_value:
            current_min = current_value
            current_max = current_value
        elif current_max < current_value:
            current_max = current_value
            if max_spread < (current_max - current_min):
                max_spread = current_max - current_min
    if max_spread > 0:
        print(max_spread)
    else:
        print("UNFIT")
