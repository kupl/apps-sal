import itertools

def from_list_to_string(A):
    st = ''
    for x in A:
        st += str(x)
    return st

def from_list_to_string_with_comma(A):
    st = ''
    for x in A:
        st = st + str(x) + ', '
    return st[:-2]

def rearranger(k, *args):
    min = float("inf")
    index = None
    list_of_permutations = list(itertools.permutations(args))
    for i in range(len(list_of_permutations)):
        tmp = int(from_list_to_string(list_of_permutations[i]))
        if tmp % k == 0 and tmp < min:
            min = tmp
            index = i
    if index == None:
        return "There is no possible rearrangement"
    else:
        return "Rearrangement: " + str(from_list_to_string_with_comma(list_of_permutations[index])) + " generates: " + str(min) + " divisible by " + str(k)
