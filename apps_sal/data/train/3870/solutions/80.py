def solve(x):

    # remove all spaces:

    w = x.replace(" ", "")

    # reverse the w string:

    new_string = ""
    for i in range(1, len(w) + 1):
        new_string += w[-i]

    # convert the old string into a list to simplify adjustments and name it new_list:

    new_list = [f for f in x]

    # capture the sapce indicies in the original string (x) to add them to the neww revrsed string (new_string) :
    start_at = 0
    spaces = []
    for val in new_list:
        if val == " ":
            spaces.append(new_list.index(val, start_at))
            start_at = new_list.index(val, start_at) + 1

    # add the spaces to the new reversed string:

    for i in spaces:
        new_string = new_string[:i] + " " + new_string[i:]
    # return the new adjsuted result:

    return new_string
