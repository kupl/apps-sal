def palindrome(num):
        
    if not isinstance(num, int) or num < 0:
        return "Not valid"
    
    if num > 9 and str(num) == str(num)[::-1]:
        return num

    num_down = num
    num_up = num
    
    d = {}
    while not d:
        num_down -= 1
        num_up += 1

        if str(num_down) == str(num_down)[::-1] and num_down > 9:
            d['?'] = num_down
    
        if str(num_up) == str(num_up)[::-1] and num_up > 9:
            d['?'] = num_up

    return d.get('?', num)
