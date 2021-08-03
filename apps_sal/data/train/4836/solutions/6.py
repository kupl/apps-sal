import datetime
import time


def elapsed_seconds(start, end):
    start = datetime.datetime.timetuple(start)
    end = datetime.datetime.timetuple(end)
    start = time.mktime(start)
    end = time.mktime(end)
    return int(end - start)
