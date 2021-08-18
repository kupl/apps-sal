def is_anagram(test, original):

    def to_list(string):
        listed = []
        for i in range(len(string)):
            listed.append(string[i])
        return listed

    return str(sorted(to_list(test.lower()))) == str(sorted(to_list(original.lower())))
