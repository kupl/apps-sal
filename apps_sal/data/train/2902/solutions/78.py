def opposite(number):
    string = str(number)                    #transform to a string to perform operations
    if string[0] == "-":                    #return values and convert back to float
        return float(string[1:])
    else:
        return float("".join(["-",string]))
  # your solution here

