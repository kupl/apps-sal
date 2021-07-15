def count_vowels(s = ''):
    count = 0
    if type(s) == str:
       for i in s:
           if i in ['a','e','i','o','u','A','E','I','O','U']:
               count += 1
       return count               
    else:
        return None
