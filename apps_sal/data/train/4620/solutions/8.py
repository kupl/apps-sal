def string_letter_count(s):
    answer = ''
    for i in sorted(set(s.lower())):
        if i.isalpha():
            answer += f'{s.lower().count(i)}{i}'
    return answer
