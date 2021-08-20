def anagrams(word, words):
    l = [letter for letter in word]
    anagram_list = []
    for item in words:
        l_item = [letter for letter in item]
        if sorted(l) == sorted(l_item):
            temp_list = [i for i in l + l_item if i not in l_item]
            if len(temp_list) == 0:
                anagram_list.append(item)
        else:
            continue
    return anagram_list
