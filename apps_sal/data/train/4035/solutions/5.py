def substring_test(str1, str2):
    str1,str2 = str1.lower(),str2.lower()
    s1 = [str1[i:i+2] for i in range(len(str1)-1)]
    s2 = [str2[i:i+2] for i in range(len(str2)-1)]
    return len(set(s1).intersection(s2))>0
