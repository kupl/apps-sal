def string_counter(string, char):
    count=0
    for i in range(0, len(string)):
        if string[i]==char:
            count=count+1
        else:
            pass

    return count

