ones = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four',
        '5': 'five', '6': 'six','7': 'seven', '8': 'eight', '9': 'nine' }

teens = {'11': 'eleven', '12': 'twelve', '13': 'thirteen', '14': 'fourteen',
         '15': 'fifteen', '16': 'sixteen', '17': 'seventeen', 
         '18': 'eighteen', '19': 'nineteen' }

tens = { '1': 'ten', '2': 'twenty', '3': 'thirty', '4': 'forty', 
         '5': 'fifty', '6': 'sixty', '7': 'seventy', '8': 'eighty', 
         '9': 'ninety' }

hundreds = {'100' : 'one hundred', '200' : 'two hundred',
            '300' : 'three hundred', '400' : 'four hundred',
            '500' : 'five hundred', '600' : 'six hundred',
            '700' : 'seven hundred', '800' : 'eight hundred',
            '900' : 'nine hundred'}

def num_to_word(n):

    str_num = str(n)

    if n >= 100:
        first_digit = str_num[0] + '00'
        second_digit = str_num[1]
        third_digit = str_num[2]
    elif n > 9:
        first_digit = str_num[0]
        second_digit = str_num[1]
    else:
        return ones[str_num]


    if n > 99:
        if second_digit == '0' and third_digit != '0':
            return '{} {}'.format(hundreds[first_digit], ones[third_digit])
        elif second_digit != '0' and third_digit == '0':
            return '{} {}'.format(hundreds[first_digit], tens[second_digit])
        elif int(second_digit + third_digit) > 10 and int(second_digit + third_digit) < 20:
            return '{} {}'.format(hundreds[first_digit], teens[second_digit + third_digit])
        elif third_digit != '0':
            return '{} {}-{}'.format(hundreds[first_digit], tens[second_digit], ones[third_digit])
        else:
            return hundreds[str_num]
            
    else:
        if n > 10 and n < 20:
            return teens[str_num]
        elif second_digit != '0':
            return '{}-{}'.format(tens[first_digit], ones[second_digit])
        else:
            return tens[first_digit]

int_to_word = {_ : num_to_word(_) for _ in range(1000)}                             
word_to_int = {num_to_word(_) : _ for _ in range(1000)} 

def sort_by_name(arr):
    return [word_to_int[word] for word in sorted(int_to_word[num] for num in arr)]

