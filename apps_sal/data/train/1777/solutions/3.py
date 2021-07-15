from itertools import chain


def parse_ascii(image_ascii):
    """ Parses the input string

    Returns a 3-tuple:
        - :width: - the width in pixels of the image
        - :height: - the height in pixels of the image
        - List of pairs (pixel_value, run_length)
            run_length is the number of successive pixels with the same value when scanning
            the row, including the following rows

    Assumes with no check:
        :run_length: > 0 for all cases
        Successive pairs have different :pixel_value:
        The sum of all pixels is a multiple of :width:

    >>> parse_ascii("3 43 4 24 2")
    (3, 2, [(43, 4), (24, 2)])
    """
    values = [int(v) for v in image_ascii.split()]
    width = values[0]
    pixel_runs = list(zip(values[1::2], values[2::2]))
    height = sum(values[2::2]) // width
    return width, height, pixel_runs


def get_intervals(pixel_runs):
    """ Denominates the pixel runs with an absolute position

    Given the pairs (pixel_value, run_length), returns triplets (start, end, pixel_value)

    The pixel positions are numbered successively starting with the first row from left
    to right and then the following rows. :start: and :end: are given as such positions.
    :start: points to the first pixel of the run with :pixel_value:
    :end: points to the position after the the pixel ending the run

    >>> list(get_intervals([(34,4),(98,5),(12,40)]))
    [(0, 4, 34), (4, 9, 98), (9, 49, 12)]
    """
    pos = 0
    for (pixel_value, run_length) in pixel_runs:
        yield (pos, pos + run_length, pixel_value)
        pos += run_length


def get_shifted_intervals(intervals, offset, width, height):
    """ Shifts the intervals, and corrects for end of row

    Returns the intervals (start, end, pixel_value) with the variables :start: and :end:
    shifted :offset: positions.

    If :offset: is positive, fills the first positions with a new (0, :offset:, None) interval,
    and removes the intervals and interval parts correspoding to the last :offset: positions.
    Conversely for negative :offset:.

    If :offset: is positive, all endings and beginnings of interval falling in the first column
    past the end of a row are back-shifted one position, extending or contracting the interval as
    necessary. This is so to prevent an offset pixel to be neighbour of a pixel in a different row,
    as the use for this will be to assess neighbouring pixels. Conversely for negative :offset: and
    interval boundaries falling in the last column of a row.

    >>> list(get_shifted_intervals([(0, 3, 55), (3, 5, 78), (5, 11, 23), (11, 15, 99)], 6, 5, 3))
    [(0, 5, None), (5, 9, 55), (9, 10, 78), (10, 15, 23)]
    >>> list(get_shifted_intervals([(0, 3, 55), (3, 5, 78), (5, 11, 23), (11, 15, 99)], -6, 5, 3))
    [(0, 5, 23), (5, 10, 99), (10, 15, None)]
    """
    # Add empty interval at the beginning if shifted right
    if offset > 0:
        if offset % width == 1:
            yield (0, offset - 1, None)
        elif offset % width == width - 1:
            yield (0, offset + 1, None)
        else:
            yield (0, offset, None)

    for (start, end, pixel_value) in intervals:
        start += offset
        end += offset

        # Remove or contract an interval if shifted past the beginning
        if end <= 0:
            continue
        if start < 0:
            start = 0

        # Remove or contract and interval if shifted past the end
        if start >= width * height:
            continue
        if end > width * height:
            end = width * height

        # Correct for proximity of a row jump
        if offset % width == 1 and start % width == 1:
            start -= 1
        if offset % width == 1 and end % width == 1:
            end -= 1
        if offset % width == width - 1 and start % width == width - 1:
            start += 1
        if offset % width == width - 1 and end % width == width - 1:
            end += 1

        # Remove if because of a contraction the length of the interval is zero
        if start == end:
            continue

        yield (start, end, pixel_value)

    # Add empty interval at the end if shifted left
    if offset < 0:
        if (width * height + offset) % width == width - 1:
            yield (width * height + offset + 1, width * height, None)
        elif (width * height - offset) % width == 1:
            yield (width * height + offset - 1, width * height, None)
        else:
            yield (width * height + offset, width * height, None)


def intersect_intervals(interval_lists, width, height):
    """ Fuse many lists of intervals into one

    Given many lists of intervals, returns a single list of intersected intervals.
    The intervals of the output list are of the form
    (start, end, [pixel_value_1, pixel_value_2, ...])
    Pixel values containing None are not included.

    >>> list(intersect_intervals([
    ...     [(0,4,23),(4,6,14),(6,25,88),(25,45,99)],
    ...     [(0,3,66),(3,9,33),(9,10,77),(10,25,43),(25,45,None)]
    ...     ], 9, 5))
    [(0, 3, [23, 66]), (3, 4, [23, 33]), (4, 6, [14, 33]), (6, 9, [88, 33]), (9, 10, [88, 77]), (10, 25, [88, 43]), (25, 45, [99])]
    """
    # List of pairs [iterator, interval], each iterator yields from a list of intervals
    # and the interval will be updated as the algorithm runs
    ilists = [[iter(ilist), (0, 0, None)] for ilist in interval_lists]
    pos = 0
    while pos < width * height:
        # Advance the iterators so that the associated interval contains :pos:
        for ilist in ilists:
            iterator, current_interval = ilist
            _, end, _ = current_interval
            while end <= pos:
                ilist[1] = next(iterator)
                _, end, _ = ilist[1]

        # Take the interval from :pos: to the closest end
        min_end = min(end for _, (_, end, _) in ilists)
        values = [value for _, (_, _, value) in ilists if value is not None]

        yield (pos, min_end, values)
        pos = min_end


def compose_intervals(intervals):
    """ Merge successive intervals if they have the same value

    Input and output are lists of intervals (start, end, value)

    >>> list(compose_intervals([(0, 3, 7), (3, 5, 7), (5, 8, 7), (8, 9, 12), (9, 13, 7)]))
    [(0, 8, 7), (8, 9, 12), (9, 13, 7)]
    """
    cur_value = None
    cur_start = None
    cur_end = None
    for (start, end, value) in intervals:
        if value == cur_value:
            cur_end = end
            continue
        if cur_end is not None:
            yield (cur_start, cur_end, cur_value)
        cur_start, cur_end, cur_value = (start, end, value)
    yield (cur_start, cur_end, cur_value)


def get_lengths(intervals):
    """ Converts intervals to (value, length) format """
    return ((value, end - start) for (start, end, value) in intervals)


def generate_ascii(pairs, width):
    """ Converts to the required output format as a string """
    return " ".join(str(n) for n in chain([width], *pairs))


def edge_detection(image):
    width, height, pixel_runs = parse_ascii(image)
    intervals = list(get_intervals(pixel_runs))
    offsets = [-width - 1, -width, -width + 1, -1, 1, width - 1, width, width + 1]
    neighbours = [get_shifted_intervals(intervals, offset, width, height) for offset in offsets]
    intersected_neighbours = intersect_intervals(neighbours, width, height)
    intersected_all = intersect_intervals([intervals, intersected_neighbours], width, height)

    result = []
    for (start, end, (base_cell, neighbour_cells)) in intersected_all:
        result_cell = max(abs(base_cell - n) for n in neighbour_cells)
        result.append((start, end, result_cell))

    out_intervals = compose_intervals(result)
    out_lengths = get_lengths(out_intervals)
    return generate_ascii(out_lengths, width)

