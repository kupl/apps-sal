def string_hash(s):
    ascii_sum = sum([ ord(i) for i in s ]) # Sums all the ascii values
    ascii_difference = sum([ ord(s[j + 1]) - ord(i) for j, i in enumerate(s[:-1])])
    shifted = (ascii_sum | ascii_difference) & (( ~ascii_sum) << 2)
    return shifted ^ (32 * (s.count(" ") + 1))
