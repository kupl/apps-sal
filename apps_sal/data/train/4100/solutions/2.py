def reverse_alternate(string):
    if string == "":
        return ""
    else:
        new_list = []
        for i in range(len(string.split())):
            if i % 2 != 0:
                new_list.append(string.split()[i][::-1])
            else:
                new_list.append(string.split()[i])
        return " ".join(new_list)
