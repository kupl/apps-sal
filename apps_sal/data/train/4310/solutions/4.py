def swap(st):
    translation = st.maketrans('aeiou', 'AEIOU')
    return st.translate(translation)
