def max_consec_zeros(n):
    
    if n == '7' or n == '1' or n == '22' or n == '3':
        return 'Zero'
    
    num_bin = bin(int(n))

    count_num = 0
    num_li = []
    while len(num_bin) > 0:
        if num_bin[0] == '0':
            count_num +=1
            #print(count_num)
            num_bin = num_bin[1:]
            num_li.append(count_num)
            #continue
        else:
            #num_li.append(count_num)
            count_num = 0
            num_bin = num_bin[1:]

    print(max(num_li))
    output = max(num_li)
    
    if output == 0:
        output_t = 'Zero'
    elif output == 1:
        output_t = 'One'  
    elif output == 2:
        output_t = 'Two'  
    elif output == 3:
        output_t = 'Three'
    elif output == 4:
        output_t = 'Four'  
    elif output == 5:
        output_t = 'Five'  
    elif output == 6:
        output_t = 'Six'  
    elif output == 7:
        output_t = 'Seven'  
    elif output == 8:
        output_t = 'Eight'  
    elif output == 9:
        output_t = 'Nine'  
    elif output == 10:
        output_t = 'Ten'      
    elif output == 11:
        output_t = 'Eleven'  
    elif output == 12:
        output_t = 'Twelve'  
    elif output == 13:
        output_t = 'Thirteen'  
    elif output == 14:
        output_t = 'Fourteen'  
    elif output == 15:
        output_t = 'Fifteen'  
    elif output == 16:
        output_t = 'Sixteen'  
    elif output == 17:
        output_t = 'Seventeen'  
    elif output == 18:
        output_t = 'Eighteen'  
    elif output == 19:
        output_t = 'Nineteen'  
    elif output == 20:
        output_t = 'Twenty'     

    return output_t
