def two_decimal_places(n):
    return round(n * 100) / 100

#My solution. It's ugly :(
#def two_decimal_places(n):
#    if isinstance(n, float):
#        if n > 0:
#            int_n = int(n)
#            three_last_digits = int((n - (int_n)) * 1000)
#            last_digit = int(str(three_last_digits)[-1])
#            result = float()
#
#            if last_digit >= 5:
#                return float(int_n) + ((three_last_digits-last_digit)+10)/1000
#            else:
#                return float(int_n) + (three_last_digits-last_digit)/1000
#        else:
#            int_n = int(n)
#            three_last_digits = int((n - (int_n)) * 1000)
#            last_digit = int(str(three_last_digits)[-1])
#            result = float()
#
#            if last_digit >= 5:
#                return float(int_n) + ((three_last_digits+last_digit)-10)/1000
#            else:
#                return float(int_n) + (three_last_digits+last_digit)/1000
#    return float()

