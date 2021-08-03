def reverse_list(l):
    output = []
    for i in l:
        output = [i] + output
    return output
