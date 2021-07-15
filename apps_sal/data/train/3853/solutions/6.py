def numeric_formatter(template, info='1234567890'):
    pos = 0
    answer = ''
        
    for char in template:
        if char.isalpha():
            answer += info[pos]
            pos += 1
            if pos >= len(info):
                pos = 0
        else:
            answer += char
            
    return answer
