abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def insert_missing_letters(st):
  return ''.join(c + ''.join(x for x in abc[abc.index(c.upper())+1:] if x.lower() not in st) if st.index(c) == i else c for i, c in enumerate(st))
