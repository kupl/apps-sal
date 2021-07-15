def number_of_carries(a, b):
    i=1
    carry_over=0
    counter=0
    length1=len(str(a))
    length2=len(str(b))
    if length1>length2:
        while length2-i>=0:
            if int(str(a)[length1-i])+int(str(b)[length2-i])+carry_over>=10:
                counter+=1
                carry_over=1
                i+=1
            else:
                carry_over=0
                i+=1
        while length1-i>=0:
            if int(str(a)[length1-i])+carry_over>=10:
                counter+=1
                carry_over=1
                i+=1
            else:
                carry_over=0
                i+=1
    elif length2>length1:
        while length1-i>=0:
            if int(str(a)[length1-i])+int(str(b)[length2-i])+carry_over>=10:
                counter+=1
                carry_over=1
                i+=1
            else:
                carry_over=0
                i+=1
        while length2-i>=0:
            if int(str(b)[length2-i])+carry_over>=10:
                counter+=1
                carry_over=1
                i+=1
            else:
                carry_over=0
                i+=1
    elif length2==length1:
        while length1-i>=0:
            if int(str(a)[length1-i])+int(str(b)[length2-i])+carry_over>=10:
                counter+=1
                carry_over=1
                i+=1
            else:
                carry_over=0
                i+=1
    return counter
    

