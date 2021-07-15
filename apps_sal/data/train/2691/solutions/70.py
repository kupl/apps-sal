def solve(s):
    longest_number = "0"
    number_sequence = "0"
    for x in s:
        if x.isalpha() is False:
            number_sequence = number_sequence + x
            if int(number_sequence) > int(longest_number):
                longest_number = number_sequence
        else:
            number_sequence = ""
    return(int(longest_number))
        

