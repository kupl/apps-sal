songs = [{'artist': 'Marillion', 'title': 'Keyleigh', 'playback': '03:36'}, {'artist': 'Pink Floyd', 'title': 'Time', 'playback': '06:48'}, {'artist': 'Rush', 'title': 'YYZ', 'playback': '04:27'}, {'artist': 'Bonobo', 'title': 'Days To Come', 'playback': '03:50'}, {'artist': 'Coldplay', 'title': 'Yellow', 'playback': '04:32'}, {'artist': 'Bloc Party', 'title': 'Like Eating Glass', 'playback': '04:22'}, {'artist': 'The Killers', 'title': 'For Reasons Unknown', 'playback': '03:30'}, {'artist': 'Arctic Monkeys', 'title': 'Teddy Picker', 'playback': '03:25'}, {'artist': 'Joe Satriani', 'title': 'Surfing With The Alien', 'playback': '04:34'}]
def longest_possible(playback):
  
  def to_seconds(t):
    mins, secs = t.split(':')
    return int(mins)*60 + int(secs)
  
  valids = [(song['title'], to_seconds(song['playback'])) for song in songs if to_seconds(song['playback']) <= playback]
  
  if len(valids) == 0:
    return False
  else:
    return max(valids, key=lambda p: p[1])[0]
