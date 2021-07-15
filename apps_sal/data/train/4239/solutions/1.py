def filter_even_length_words(words):
    even_words_array=[]
    for i in words:
      if len(i)%2==0:
        even_words_array.append(i)
    return even_words_array

