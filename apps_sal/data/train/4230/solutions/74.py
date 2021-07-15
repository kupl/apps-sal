def reverse_letter(string):
    ans =[]
    for i in list(string):
        if i.isalpha():
            ans.append(i)
    a = "".join(ans)[::-1]
    return a
