def array(string):
    #print(string)
    str_slice = string.split(",")[1:-1]  #Split the string with , and get the list of all chars except first and last
    #print(str_slice)
    return ' '.join(str_slice) if str_slice else None  #if the string is not empty,
                                                      # return string else return None

