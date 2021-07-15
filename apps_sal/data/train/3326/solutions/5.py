def reverse_in_parentheses(string):
    for i in range(len(string)):
        if string[i]=="(":
            finder,depth=i,1
            while depth>int():depth,finder=depth+")(".index(string[finder+1])-1+")(".index(string[finder+1]) if string[finder+1] in "()" else depth,finder+1
            string=string[:i+1]+"".join(["()"[")(".index(y)] if y in "()" else y for y in list(reversed(string[i+1:finder]))])+string[finder:]
    return string
