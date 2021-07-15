def solve(s):
    # s= i love codewars
    rev=s[::-1]
    rev2=""
    f=""
    for i in rev:
        if i==" ":
            continue;
        rev2+=i
    j=0
    for i in s:
        if i==" ":
            f+=(" ")
            continue
        f+=(rev2[j])
        j+=1
    return f
print((solve("i love codewars")))

