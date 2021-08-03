def who_is_paying(name):
    var = []  # declaring empty list
    if len(name) <= 2:  # if the lenght of name (len(name)) is <= to 2
        var.append(name)  # we will add the content of the name variable to the list
        return var  # and return it as a result
    # if not
    var.append(name)  # we will add the full person name from the variable "name"
    var.append(name[0] + name[1])  # then add the first and second character
    return var  # and return the result
