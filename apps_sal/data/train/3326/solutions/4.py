def reverse_in_parentheses(string):
    counter = 0
    res = [""]
    
    for i in string:
        
        if i == "(":
            res.append("")
            counter += 1
            
        elif i == ")":
            counter -= 1
            
            if counter % 2 == 0:
                res[counter] += "(" + res.pop() + ")"
            else:
                res[counter] = "(" + res.pop() + ")" + res[counter]            
        
        elif counter % 2 == 0:
            res[counter] += i
            
        else:
            res[counter] = i + res[counter]
            
    return res[0]
