songs = [{'artist': 'Marillion', 'title': 'Keyleigh', 'playback': '03:36'}, {'artist': 'Pink Floyd', 'title': 'Time', 'playback': '06:48'}, {'artist': 'Rush', 'title': 'YYZ', 'playback': '04:27'}, {'artist': 'Bonobo', 'title': 'Days To Come', 'playback': '03:50'}, {'artist': 'Coldplay', 'title': 'Yellow', 'playback': '04:32'}, {'artist': 'Bloc Party', 'title': 'Like Eating Glass', 'playback': '04:22'}, {'artist': 'The Killers', 'title': 'For Reasons Unknown', 'playback': '03:30'}, {'artist': 'Arctic Monkeys', 'title': 'Teddy Picker', 'playback': '03:25'}, {'artist': 'Joe Satriani', 'title': 'Surfing With The Alien', 'playback': '04:34'}]


def to_seconds(time):
    minutes, seconds = list(map(int, time.split(':')))
    return minutes * 60 + seconds


def longest_possible(playback):
    longest_song = 0
    song_title = ''
    for song in songs:
        song_length = to_seconds(song['playback'])
        if longest_song < song_length <= playback:
            longest_song = song_length
            song_title = song['title']
    return song_title or False
