from operator import truediv


def time(distance, boat_speed, stream):
    stream, stream_speed = stream.split()
    stream_speed = int(stream_speed) * (-1 if stream == 'Upstream' else 1)
    return round(truediv(distance, (boat_speed + stream_speed)), 2)
