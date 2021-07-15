def capitalize_word(word):
    res = []
    res[:] = word
    print(res)
    newarry = []
    for i in range(0, len(res)):
        print((res[i]))
        if(res[i] == res[0]):
            newarry.append(res[0].upper())
        else:
            newarry.append(res[i])
    print(("".join(newarry)))
    answer = "".join(newarry)
    return answer

