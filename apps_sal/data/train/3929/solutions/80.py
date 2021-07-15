def reverse(st):
    words = st.split(' ')
    words = list(filter(lambda word: word != '', words))
    reversed = words[::-1]
    return ' '.join(reversed)
