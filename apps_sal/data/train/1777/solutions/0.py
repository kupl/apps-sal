'''
Challenge Fun 
https://www.codewars.com/kata/58bfa40c43fadb4edb0000b5/train/python

For a rectangular image given in run-length encoding (RLE) as
described below, return a RLE of the image processed by replacing
each pixel by the maximum absolute value of the difference between
it and each neighboring pixel (a simple form of edge detection).

For a RLE encoding string "7 15 4 100 15 25 2 ...",
    7      ----> image width
    15 4   ----> a pair(color value + pixel count)
    100 15 ----> a pair(color value + pixel count)
    25 2   ----> a pair(color value + pixel count)
    ...          ...
where the image width is > 0 and the sum of all the pixel counts
is a multiple of the width.

--------------------
Design of solution

Read the rle-encoded values into a buffer of rows of the given width,
with an important optimization trick. In the case of long runs of the
same value, where three or more rows would be filled with identical
data, store just three rows of data, and remember (using another data
structure) which is the middle of the three rows, and how many copies
of it (the "row count") were in the original image. For example,
suppose the image width is 10, and the image has a run of 73 copies
of the value 7, and the run starts with the last two values in row 34.
The buffer would look like this:

        ...
    34  [ some previous data ...  7, 7 ]
    35  [ 7, 7, 7, 7, 7, 7, 7, 7, 7, 7 ]
    36  [ 7, 7, 7, 7, 7, 7, 7, 7, 7, 7 ]
    37  [ 7, 7, 7, 7, 7, 7, 7, 7, 7, 7 ]
    38  [ 7, ... start of new data ... ]
        ...

and elsewhere a note is made that row 36 has a row count of 5.

With long runs arranged this way, the edge-detection transformation
can be run on the buffer without having to worry about row counts.
Row counts are used later, when encoding the transformed values back
into a run-length encoding.
'''
import itertools


def edge_detection(image):
    data = [int(datum) for datum in image.split(' ')]
    width = data.pop(0)

    (inbuf, rowcounts) = fill_buffer(width, data)
    outbuf = detect_edges(inbuf)

    outdata_list = encode(outbuf, rowcounts)
    outdata = [str(datum) for datum in outdata_list]
    return str(width) + ' ' + ' '.join(outdata)


def fill_buffer(width, data):
    buf = []
    rowcounts = dict()

    row, row_ndx = [], 0
    while data:
        val, runlen = data.pop(0), data.pop(0)
        if row == [] and runlen > 3 * width:
            buf += [[val] * width] * 3
            rowcounts[row_ndx + 1] = (runlen // width) - 2
            row_ndx += 3
            row = [val] * (runlen % width)
            continue

        take = min(runlen, width - len(row))
        runlen -= take
        row += [val] * take
        if len(row) < width:
            continue

        buf.append(row)
        row_ndx += 1
        row = []

        if row == [] and runlen > 3 * width:
            buf += [[val] * width] * 3
            rowcounts[row_ndx + 1] = (runlen // width) - 2
            row_ndx += 3
            row = [val] * (runlen % width)
            continue

        while runlen > 0:
            take = min(runlen, width - len(row))
            runlen -= take
            row += [val] * take
            if len(row) == width:
                buf.append(row)
                row_ndx += 1
                row = []

    return buf, rowcounts


def pairs_from(iterable, fillvalue=None):
    '''
    Yields iterable's elements in pairs. If iterable is exhausted after
    an odd number of elements, completes the last pair with fillvalue.
    '''
    args = [iter(iterable)] * 2
    return itertools.zip_longest(*args, fillvalue=fillvalue)


def detect_edges(inbuf):
    length = len(inbuf)
    width = len(inbuf[0])

    outbuf = [([-1] * width).copy() for _ in range(length)]

    if 1 == width == length:
        return [[0]]

    if 1 == length:
        outbuf[0][0] = abs(inbuf[0][0] - inbuf[0][1])
        outbuf[0][width - 1] = abs(inbuf[0][width - 2] - inbuf[0][width - 1])
        for col in range(1, width - 1):
            val = inbuf[0][col]
            outbuf[0][col] = max(abs(val - inbuf[0][col - 1]),
                                 abs(val - inbuf[0][col + 1]))
        return outbuf

    if 1 == width:
        outbuf[0][0] = abs(inbuf[0][0] - inbuf[1][0])
        outbuf[length - 1][0] = abs(inbuf[length - 2][0]
                                    - inbuf[length - 1][0])
        for row in range(1, length - 1):
            val - inbuf[row][0]
            outbuf[row][0] = max(abs(val - inbuf[row - 1][0]),
                                 abs(val - inbuf[row + 1][0]))
        return outbuf

    BOT = length - 1
    RT = width - 1

    top_lf, top_rt = inbuf[0][0], inbuf[0][RT]
    bot_lf, bot_rt = inbuf[BOT][0], inbuf[BOT][RT]
    outbuf[0][0] = max(abs(top_lf - inbuf[0][1]),
                       abs(top_lf - inbuf[1][0]),
                       abs(top_lf - inbuf[1][1]))
    outbuf[0][RT] = max(abs(top_rt - inbuf[0][RT - 1]),
                        abs(top_rt - inbuf[1][RT - 1]),
                        abs(top_rt - inbuf[1][RT]))
    outbuf[BOT][0] = max(abs(bot_lf - inbuf[BOT - 1][0]),
                         abs(bot_lf - inbuf[BOT - 1][1]),
                         abs(bot_lf - inbuf[BOT][1]))
    outbuf[BOT][RT] = max(abs(bot_rt - inbuf[BOT - 1][RT - 1]),
                          abs(bot_rt - inbuf[BOT - 1][RT]),
                          abs(bot_rt - inbuf[BOT][RT]))

    for col in range(1, RT):
        val = inbuf[0][col]
        outbuf[0][col] = max(abs(val - inbuf[0][col - 1]),
                             abs(val - inbuf[0][col + 1]),
                             abs(val - inbuf[1][col - 1]),
                             abs(val - inbuf[1][col]),
                             abs(val - inbuf[1][col + 1]))
        val = inbuf[BOT][col]
        outbuf[BOT][col] = max(abs(val - inbuf[BOT - 1][col - 1]),
                               abs(val - inbuf[BOT - 1][col]),
                               abs(val - inbuf[BOT - 1][col + 1]),
                               abs(val - inbuf[BOT][col - 1]),
                               abs(val - inbuf[BOT][col + 1]))

    for row in range(1, BOT):
        val = inbuf[row][0]
        outbuf[row][0] = max(abs(val - inbuf[row - 1][0]),
                             abs(val - inbuf[row - 1][1]),
                             abs(val - inbuf[row][1]),
                             abs(val - inbuf[row + 1][0]),
                             abs(val - inbuf[row + 1][1]))
        val = inbuf[row][RT]
        outbuf[row][RT] = max(abs(val - inbuf[row - 1][RT - 1]),
                              abs(val - inbuf[row - 1][RT]),
                              abs(val - inbuf[row][RT - 1]),
                              abs(val - inbuf[row + 1][RT - 1]),
                              abs(val - inbuf[row + 1][RT]))

    for row in range(1, BOT):
        for col in range(1, RT):
            val = inbuf[row][col]
            outbuf[row][col] = max(abs(val - inbuf[row - 1][col - 1]),
                                   abs(val - inbuf[row - 1][col]),
                                   abs(val - inbuf[row - 1][col + 1]),
                                   abs(val - inbuf[row][col - 1]),
                                   abs(val - inbuf[row][col + 1]),
                                   abs(val - inbuf[row + 1][col - 1]),
                                   abs(val - inbuf[row + 1][col]),
                                   abs(val - inbuf[row + 1][col + 1]),
                                   )
    return outbuf


def encode(buf, rowcounts):
    width = len(buf[0])

    val_rl = list()

    for row_ndx in range(len(buf)):
        encoded_row = [(val, len(list(grp))) for
                       (val, grp) in itertools.groupby(buf[row_ndx])]
        if row_ndx in rowcounts:
            val_rl.append((encoded_row[0][0], width * rowcounts[row_ndx]))
        else:
            for (val, count) in encoded_row:
                val_rl.append((val, count))

    encoding = list()
    (old_val, old_rl) = val_rl.pop(0)
    for (val, rl) in val_rl:
        if val == old_val:
            old_rl += rl
        else:
            encoding += (old_val, old_rl)
            (old_val, old_rl) = val, rl
    encoding += (old_val, old_rl)

    return encoding
