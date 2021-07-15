def encrypt(text,key):
    final_list=[]
    if text=="":
        return ""
    alpha_dict={}
    num_lst_1=[]
    alphabet="abcdefghijklmnopqrstuvwxyz"
    for i in range(0,26):
        alpha_dict[alphabet[i]]=i
    for letter in text.lower():
        if letter in alphabet:
            num_lst_1.append(alpha_dict[letter])
    if len(num_lst_1)%2==1:
        num_lst_1.append(25)
    num_lst_2=[]
    for char in key.lower():
        num_lst_2.append(alpha_dict[char])
    sum_row_1=0
    sum_row_2=0
    for x in range(0,len(num_lst_1),2):
        sum_row_1=num_lst_2[0]*num_lst_1[x]+num_lst_2[1]*num_lst_1[x+1]
        sum_row_2=num_lst_2[2]*num_lst_1[x]+num_lst_2[3]*num_lst_1[x+1]
        final_list.append(sum_row_1%26)
        final_list.append(sum_row_2%26)
    enpt=""
    for num in final_list:
        enpt+=alphabet[num]
    return enpt.upper()

