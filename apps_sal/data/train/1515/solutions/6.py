# cooking dish here

from collections import Counter

for testcase in range(int(input())):
    string = input()
    letter_count = Counter(string)
    
    letter_value = lambda x: ord(x) - 97
    base_value   = (letter_value(string[0])+1) * 100
    
    net_sum = 0
    
    for letter in range(97, 97+26):
        net_sum += ( (base_value+letter_value(chr(letter)))*letter_count[chr(letter)] ) % int(1e9+7)
    
    print(net_sum%int(1e9+7))
