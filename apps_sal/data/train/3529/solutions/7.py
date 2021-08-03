songs = [{'artist': 'Marillion', 'title': 'Keyleigh', 'playback': '03:36'}, {'artist': 'Pink Floyd', 'title': 'Time', 'playback': '06:48'}, {'artist': 'Rush', 'title': 'YYZ', 'playback': '04:27'}, {'artist': 'Bonobo', 'title': 'Days To Come', 'playback': '03:50'}, {'artist': 'Coldplay', 'title': 'Yellow', 'playback': '04:32'}, {'artist': 'Bloc Party', 'title': 'Like Eating Glass', 'playback': '04:22'}, {'artist': 'The Killers', 'title': 'For Reasons Unknown', 'playback': '03:30'}, {'artist': 'Arctic Monkeys', 'title': 'Teddy Picker', 'playback': '03:25'}, {'artist': 'Joe Satriani', 'title': 'Surfing With The Alien', 'playback': '04:34'}]


def seconds(ms):
    m, s = map(int, ms.split(':'))
    return m * 60 + s


def longest_possible(playback):
    try:
        song = max(
            [song for song in songs if seconds(song['playback']) <= playback],
            key=lambda song: seconds(song['playback'])
        )
    except ValueError:
        return False
    return song['title']
