def min_sum(arr):
    john = str(sorted(arr)).replace(']', '').replace('[', '')
    juan = john.split(',')
    joe = 0
    while len(juan) > 0:
        joe += int(juan[0]) * int(juan[-1])
        juan.pop(0)
        juan.pop(-1)
    return joe
