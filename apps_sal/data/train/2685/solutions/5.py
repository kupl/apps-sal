def keyword_cipher(msg, keyword):
  abc = 'abcdefghijklmnopqrstuvwxyz'
  return msg.lower().translate(str.maketrans(abc, ''.join(dict.fromkeys(keyword)) + ''.join(c for c in abc if c not in keyword)))
