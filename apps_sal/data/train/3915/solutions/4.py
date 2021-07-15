def solve(string):
    operations=[]
    for line in string.split("\n"):
        num1,num2=line[::-1].split()
        carries,carry=0,0
        for v1,v2 in zip(num1,num2):
            v1,v2=int(v1),int(v2)
            v3=v1+v2+carry
            v4=v3%10
            if carry:carries+=v4<=max(v1,v2)
            else:carries+=v4<max(v1,v2)
            carry=int(v3>9)
        if carries:operations.append(f"{carries} carry operations")
        else:operations.append("No carry operation")
    return "\n".join(operations)
