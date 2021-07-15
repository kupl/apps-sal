def mutate_my_strings(s1,s2):
    l=len(s2)
    return "\n".join(s2[:i]+s1[i:] for i in range(l+1) if i==l or s2[i]!=s1[i])+"\n"
