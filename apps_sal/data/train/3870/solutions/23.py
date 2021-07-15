def solve(s):
    string = s
    string = string.split()
    string = ''.join(string)
    string = string[::-1]
    
    space_list = []
    for i, char in enumerate(s):
        if char == ' ':
            space_list.append(i)
    
    for space in space_list:
        first_chunk = string[0:space]
        first_chunk += ' '
        string = first_chunk + string[space:] 
    return string

