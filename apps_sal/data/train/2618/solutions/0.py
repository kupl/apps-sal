import re
n = int(input())
upper_check = '.*([A-Z].*){2,}'
digit_check = '.*([0-9].*){3,}'
alphanumeric_and_length_check = '([A-Za-z0-9]){10}$'
repeat_check = '.*(.).*\\1'
for i in range(n):
    uid_string = input().strip()
    upper_check_result = bool(re.match(upper_check, uid_string))
    digit_check_result = bool(re.match(digit_check, uid_string))
    alphanumeric_and_length_check_result = bool(re.match(alphanumeric_and_length_check, uid_string))
    repeat_check_result = bool(re.match(repeat_check, uid_string))
    if upper_check_result and digit_check_result and alphanumeric_and_length_check_result and (not repeat_check_result):
        print('Valid')
    else:
        print('Invalid')
