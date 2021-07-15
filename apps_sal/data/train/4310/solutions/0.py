def swap(st):
  tr = str.maketrans('aeiou', 'AEIOU')
  return st.translate(tr);
