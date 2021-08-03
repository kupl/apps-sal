def remove_punc(words):
    if "'" in words:
        temp_2 = words.partition("'")
        words = temp_2[0] + temp_2[-1]

        words = remove_punc(words)

    if "." in words:
        temp_2 = words.partition(".")
        words = temp_2[0] + temp_2[-1]

        words = remove_punc(words)

    if "," in words:
        temp_2 = words.partition(",")
        words = temp_2[0] + temp_2[-1]

        words = remove_punc(words)

    return words


def transw(words, old, new):
    temp_words = words.lower().replace(old, " " * len(old))
    result = ""
    threshold = 0
    for i in range(0, len(temp_words)):
        if temp_words[i] != " ":
            result = result + words[i]
        else:
            threshold += 1
            if threshold == len(old):
                result = result + new
                threshold = 0
    return result


def n00bify(text):
    temp = text.split()
    result = ""
    for i in temp:

        i = transw(i, 'too', '2')
        i = transw(i, 'to', '2')
        i = transw(i, 'fore', '4')
        i = transw(i, 'for', '4')
        i = transw(i, 'oo', '00')
        i = transw(i, 'be', 'b')
        i = transw(i, 'you', 'u')
        i = transw(i, 'are', 'r')
        i = transw(i, 'please', 'plz')
        i = transw(i, 'people', 'ppl')
        i = transw(i, 'really', 'rly')
        i = transw(i, 'have', 'haz')
        i = transw(i, 'know', 'no')
        i = transw(i, 's', 'z')

        i = remove_punc(i)

        if len(result) == 0:
            result = result + i
        else:
            result = result + " " + i

    if result[0] == "w" or result[0] == "W":
        result = "LOL" + " " + result
    if result[0] == "h" or result[0] == "H":
        result = result.upper()

    t_result = result.split()

    count = 0
    for m in t_result:
        for n in m:
            if n == "!":
                break

            elif n.isalnum():
                count += 1

    count = count + len(t_result) - 1

    if count >= 32:
        if t_result[0] == "LOL":
            t_result = ["OMG"] + t_result
            t_result[0] = "LOL"
            t_result[1] = "OMG"
        else:
            t_result = ["OMG"] + t_result

    for k in range(0, len(t_result)):
        if "?" in t_result[k]:
            t_result[k] = t_result[k][:t_result[k].index("?")] + "?" * (len(t_result) - 1) + t_result[k][t_result[k].index("?"):]

        if "!" in t_result[k]:
            add_in = ""
            for l in range(0, len(t_result)):
                if l % 2 == 0:
                    add_in = add_in + "!"
                else:
                    add_in = add_in + "1"

            t_result[k] = t_result[k][:t_result[k].index("!")] + add_in + t_result[k][t_result[k].index("!") + 1:]

    for i in range(0, len(t_result)):
        if i % 2 != 0:
            t_result[i] = t_result[i].upper()

    return " ".join(t_result)
