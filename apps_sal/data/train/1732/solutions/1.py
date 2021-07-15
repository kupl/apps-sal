from fractions import Fraction
a=0
variable=[]
def solve(*equations):
    
    sq = [i for i in equations]
    print(sq)
    
    def extract_number(s):
        temp = ''
        variable = ''
        L=[]
        for i in range(len(s)):
            try:
                if s[i] in ['+','-'] and temp=='':
                    temp+=s[i];
                    if variable!='':L.append(variable);variable=''
                elif s[i] in ['+','-'] and temp!='':   #2x=2-4y
                    L.append(temp);temp=s[i]
                else:
                    temp+=str(int(s[i]))
            except:
                if s[i] not in ['+','-','=']:variable+=s[i]
                if len(L)==0 and temp=='':L.append('1')                      #x+5=9
                elif temp in ['+','-']:
                    L.append(temp+'1')                    #7+x=9
                elif temp!='' and s[i]!='=':L.append(temp);                  #7x+8y=9
                elif temp!='' and s[i]=='=':L.extend([temp,'='])             #7x+8=9
                elif temp=='' and s[i]=='=':
                    if variable!='': 
                        L.append(variable);variable=''
                    L.extend(['='])
                else:pass
                temp=''
    
        if temp!='':L.append(temp)
        if variable!='':L.append(variable)
        return L
    
    def refine(raw_matrix):
        refine_dict = dict({})
        flag=0
        num=0
        refine_dict['constant']=0
        for i in raw_matrix:
            try:
                if num!=0 and str(int(i))!='':refine_dict['constant']+=num
                if flag==0:
                    num=int(i)
                else:
                    num=-int(i)
            except:
                if i!='=':
                    if i not in refine_dict.keys():
                        refine_dict[i]=num
                    else:
                        refine_dict[i]+=num
                    num=0
                else:
                    flag=1
        if num!=0:
            refine_dict['constant']+=num
        else:
            refine_dict['constant']+=0
        return refine_dict
    
    def reduction(List_of_dict):
        L=[]
        max_number=0;max_dict=dict({})
        for findout in range(len(List_of_dict)):
            if len(List_of_dict[findout])>max_number:
                max_number=len(List_of_dict[findout])
                max_dict = List_of_dict[findout]
        nonlocal variable
        variable = [i for i in max_dict.keys()][::-1]
        insert = 0
        for i in List_of_dict:
            keys_list=[m for m in i.keys()]
            temp_list=[]
            for j in variable:
                try:
                    temp_list.append(i[j])
                    keys_list.remove(j)
                except:
                    temp_list.append(0)
            for k in keys_list:
                variable.insert(-1,k)
                temp_list.append(i[k])
            L.append(temp_list)          
        
        print(variable)
        
        for i in range(len(List_of_dict)):
            if L[i][i]==0:
                for j in range(i,len(List_of_dict)):
                    if L[j][i]!=0:
                        temp_list = L[i]
                        L[i] = L[j]
                        L[j] = temp_list
                        break
            a=L[i][i]
            if i==len(variable)-1 and a==0:return L
            if L[i][:i+1]==[0]*(i+1) and L[i][-1]!=0 :return None
            if L[i]==[0]*(len(L[i])) and i<len(variable)-1:return None
            L[i] = list(map(lambda x:Fraction(x,a),L[i]))
            K = [num for num in range(len(List_of_dict))]
            del K[i]
            for j in K:
                if i<len(variable)-1:
                    L[j]=[L[j][index]-L[i][index]*Fraction(L[j][i],L[i][i]) for index in range(len(L[j]))]
                else:
                    if a!=0:
                        return None
        return L
    
    
    def sol(equation):
        L=[]
        for s in equation:
            L.append(refine(extract_number(s)))
        Ans = reduction(L)
        if Ans!=None:
            show = dict({})
            keys = [i for i in variable]
            nonlocal a
            a=len(keys)
            for i in Ans:
                for j in range(len(i)):
                    if i[j]==1:
                        show[keys[j]]=float(-i[-1])
                        break
            return show
        else:
            return None
        

    solution = sol(sq)        
    
    if len(variable)-1>len(sq):return None

    return solution
