def solution(str, end):
    str = str[::-1]
    end = end[::-1]
    end_length = len(end)
    str_length = len(str)
    result = 0
    
    if(end_length > str_length):
        return False
    else:
        for i in range(end_length):
            if(str[i] == end[i]):
                result +=1
    
    if(result == end_length):
        return True
    else:
        return False 
    

