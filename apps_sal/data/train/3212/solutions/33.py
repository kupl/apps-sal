def generate_hashtag(s):
      smod = ''.join([word.capitalize() for word in s.split()])
      return '#' + smod if s != '' and len(smod) <= 140 else False
