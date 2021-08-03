from functools import reduce
songs = [{'artist': 'Marillion', 'title': 'Keyleigh', 'playback': '03:36'}, {'artist': 'Pink Floyd', 'title': 'Time', 'playback': '06:48'}, {'artist': 'Rush', 'title': 'YYZ', 'playback': '04:27'}, {'artist': 'Bonobo', 'title': 'Days To Come', 'playback': '03:50'}, {'artist': 'Coldplay', 'title': 'Yellow', 'playback': '04:32'}, {'artist': 'Bloc Party', 'title': 'Like Eating Glass', 'playback': '04:22'}, {'artist': 'The Killers', 'title': 'For Reasons Unknown', 'playback': '03:30'}, {'artist': 'Arctic Monkeys', 'title': 'Teddy Picker', 'playback': '03:25'}, {'artist': 'Joe Satriani', 'title': 'Surfing With The Alien', 'playback': '04:34'}]


def seconds(song):
    p = song.get('playback', 0)
    return int(p[:2]) * 60 + int(p[3:])


def pick_if(acc, x, playback):
    sx = seconds(x)
    return x if sx > seconds(acc) and sx <= playback else acc


def longest_possible(playback):
    r = reduce(lambda acc, x: pick_if(acc, x, playback), songs, {'title': False, 'playback': '00:00'})
    return r['title']
