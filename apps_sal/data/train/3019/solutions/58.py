def str_count(strng, letter):
    answer=0
    x=0
    length=len(strng)
    while x<length:
        if strng[x]==letter:
            answer=answer+1
        x=x+1
    return answer

