def jumping_number(number):
    if number < 10:
        return 'Jumping!!'
    else:
        digits = []
        while number > 0:
            digit = number % 10
            number = number // 10
            digits.append(digit)
        i = 1
        jumping = True
        while i < len(digits):
            if abs(digits[i] - digits[i - 1]) != 1:
                jumping = False
                break
            i = i + 1
        if jumping == True:
            return 'Jumping!!'
        else:
            return 'Not!!'
