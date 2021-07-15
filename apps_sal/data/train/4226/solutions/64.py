def remove_smallest(numbers):
    if len(numbers)!=0:
        m=numbers[0]
        d=[]
        for x in numbers:
            m=min(m,x)
        for x in numbers:
            if m!=x:
                d.append(x)
            else:
                m=None
                continue
        return d
    else:
        return numbers
