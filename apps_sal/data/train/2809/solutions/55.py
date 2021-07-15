def digitize(n):
    string_of_int = (str(n))
    final_array = [int(x) for x in string_of_int]
    return(final_array[::-1])
