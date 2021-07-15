def complexSum(arr):
    real_sum = 0
    imag_sum = 0
    for string in arr:
        val = ''
        for char in string:
            if char == '-':
                if len(val) > 0:
                    real_sum += int(val)
                val = '-'
            elif char == '+':
                real_sum += int(val)
                val = ''
            elif char == 'i':
                if val == '':
                    val = 1
                elif val[0] == '-':
                    if len(val) != 1:
                        val = -1 * int(val[1::])
                    else: val = -1
                imag_sum += int(val)
                val = 0
            else:   
                val += char
        real_sum += int(val)
    fin_string = ''
    if imag_sum == 1:
        fin_string = 'i'
    elif imag_sum == 0:
        fin_string = ''
    elif imag_sum == -1:
        fin_string = '-i'  
    else:
        if imag_sum > 1 and real_sum != 0:
            fin_string = '+'+str(imag_sum)+'i'
        else: 
            fin_string = str(imag_sum)+'i'
    if real_sum == 0 and imag_sum != 0:
        return fin_string
    return (str(real_sum)+fin_string) if (real_sum+imag_sum !=0) else '0'
