def reverse_words(text):
    array = text.split(' ')
    new_array = [ word[::-1] for word in array]
    return ' '.join(new_array)
  

