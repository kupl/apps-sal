def number(lines):
    ans =[]
    if len(lines)>0:
        for i in range(len(lines)):
            ans.append(str(i+1)+': '+ lines[i])
        return ans
    else:
        return ans
        

