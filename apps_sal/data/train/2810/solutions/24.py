def solve(arr):
    master_list = []
    for s in arr:
        count = 0
        for idx, char in enumerate(s):
            if idx == ord(char.lower()) - 97:
                count += 1
        master_list.append(count)
    return master_list
