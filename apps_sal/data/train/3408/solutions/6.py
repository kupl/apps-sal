add_check_digit=lambda s:s+'0X987654321'[sum((i%6+2)*int(d)for i,d in enumerate(s[::-1]))%11]
