def jumping_number(number:int) -> str:
    num_str = str(number)
    for i,v in enumerate(num_str[:-1]):
        if abs(int(v) - int(num_str[i+1])) != 1:
            return "Not!!"
    else: # 'for-else' https://book.pythontips.com/en/latest/for_-_else.html#else-clause
        return "Jumping!!"
