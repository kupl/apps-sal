string = input()
max_no = 0
for i in range(len(string)):
    var_occur = 0
    check_no = str()
    j = i
    while(j < len(string) and var_occur < 2):
        if(string[j].isalpha()):
            if(var_occur == 0):
                check_no += '9'
                var_occur += 1
            else:
                var_occur += 1
        else:
            check_no += string[j]
        j += 1
    # print(check_no)
    max_no = max(max_no, int(check_no))
print(max_no)
