def array(string):
    #your code here
    if string == "" or len(string.split(",")) <= 2:
        return None
    else:
        string = string.split(",")
        string = string[1:-1]
        
        return " ".join(string)

