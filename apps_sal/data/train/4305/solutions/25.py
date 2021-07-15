def order_weight(strng):
    if strng=="":
        return strng
    else:
        lss=strng.split()
        new_ls=[]
        dic={}
        value=""    
        for elements in lss:
            new=sum(float(element) for element in elements) 
            if new in new_ls:
                  while new in new_ls:
                      new=float(new)
                      new+=0.001
                  new_ls.append(new)
                  dic[new]=elements
            else:
                new_ls.append(new)
                dic[new]=elements
            new_ls.sort() 
        sl=[dic.get(new_ls[m]) for m in range(len(new_ls))]
        for m in range(len(new_ls)):
            for n in range(len(new_ls)):
                if int(new_ls[m])==int(new_ls[n]) and m!=n:
                    if dic.get(new_ls[m])<dic.get(new_ls[n]) and m>n:
                        t=new_ls[m]
                        new_ls[m]=new_ls[n]
                        new_ls[n]=t        
        for i in range(len(new_ls)-1):
            value+="".join(dic.get(new_ls[i]))
            value+=" "
        value+="".join(dic.get(new_ls[-1]))
        return value
