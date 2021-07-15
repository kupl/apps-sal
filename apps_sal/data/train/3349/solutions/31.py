def find_missing_number(sequence):
    #if string is empty return 0
    if sequence == "":
        return 0
    
    #if string contains any letters or non numbers return 1
    if not sequence.isdigit or any(c.isalpha() for c in sequence) or "_" in sequence:
        return 1

    #create list of acsending numbers from string
    s = sorted(int(num) for num in sequence.split(' '))
    
    #if the elements in list form a perfect sequence from 1 return 0
    if s[-1] == len(s) and s[0] ==1:
        return 0

    #compare the list s to a newly created list starting from 1
    #if number is not in s, return number
    for i in range(len(s)):
        if s[i] != i+1:
            return i+1
            

