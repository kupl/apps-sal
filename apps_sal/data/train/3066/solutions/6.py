def clean(string,to_clean=[("+-","-"),("-+","-"),("++","+"),("--","+")]):
    cleaned_string=string
    for i,j in to_clean:
        while i in cleaned_string:cleaned_string=cleaned_string.replace(i,j)
    print((cleaned_string,string))
    return clean(cleaned_string) if cleaned_string!=string else string
def solve(string):
    while "(" in string:
        counter=int()
        while counter<len(string):
            if string[counter]=="(":
                for x in range(counter+1,len(string)):
                    if string[x]==")":string,counter=string[:counter]+"".join(["+-"["-+".index(y)] if y in "-+" and string[counter-1]=="-" and string[counter+ind] not in "(-+" else y for ind,y in enumerate(string[counter+1:x])])+string[x+1:],counter-1
                    elif string[x]=="(":pass
                    else:continue
                    break
            counter+=1
            print(string)
    to_return=clean(string)
    return to_return[1:] if to_return[int()]=="+" else to_return


