def valid_parentheses(string):
    times=0
    count=0
    for i in string:
        if string[times]=='(':
                count+=1
        elif string[times]==')':
                count-=1
        print(count, i, times)
        times+=1
        if count <0:
            return False    
    if count==0:
        return True
    else:
        return False
