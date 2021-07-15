def camel_case(string):
    words=string.split()
    answer=""
    for capped in words:
        
        answer+=capped.capitalize()
    return answer
