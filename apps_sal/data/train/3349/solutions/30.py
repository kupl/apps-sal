def find_missing_number(sequence):
    if not sequence : return 0
    try : s=set(map(int,sequence.split(" ")))
    except ValueError : return 1
    for i in range(len(s)):
        if not i+1 in s : return i+1
    return 0        
