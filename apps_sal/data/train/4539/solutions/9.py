def hop_across(lst):
    going = 0
    coming = 0
    output = 0
    while going < len(lst):
        output += 1
        going += lst[going]
    lst = lst[::-1]
    while coming < len(lst):
        output += 1
        coming += lst[coming]
    return output
