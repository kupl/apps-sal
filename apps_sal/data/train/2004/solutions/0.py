x = input ()

flag = 0
s = 0

for each_item in x:
    if each_item == '0':
        if flag == 0:
            flag = 1;
            continue
        else:
            print (each_item, end = '')
    else:
        if (s == len (x) - 1 and flag == 0) :
            continue
        print (each_item, end = '')
    s = s + 1

