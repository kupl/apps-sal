def super_size(n):
    #your code here
    convert_to_str = str(n)
    lst = convert_to_str.split()
    for elem in convert_to_str:
        lst.append(elem)
    lst.pop(0)
    num_list = []
    for num in lst:
        num_list.append(int(num))
    srt = sorted(num_list, reverse = True)
    string = "".join(str(srt))
    rep1 = string.replace("[", "")
    rep2 = rep1.replace("]", "")
    rep3 = rep2.replace(",", "")
    rep4 = rep3.replace(" ", "")
    return int(rep4)
