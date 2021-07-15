def find_missing_number(sequence):
    if sequence=='':
        return 0
    else:
        se=sequence.split()
        for j in se:
            if j.isdigit():
                continue
            else:
                return 1
            
        for i in range(1,len(se)+1):
            if str(i) not in se:
                return i
        return 0    
        

