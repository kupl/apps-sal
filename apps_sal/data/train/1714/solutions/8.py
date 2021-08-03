import numpy as np
import itertools as it


def convertToPolar(points, refpoint):
    """Converts a list-like of 2D points to polar coordinates, first column containing the radii, second column containing the angles from [2, 2*pi]"""
    points = np.asarray(points)
    refpoint = np.asarray(refpoint)
    points_c = points - refpoint

    rads = np.linalg.norm(points_c, axis=1)
    angles = np.angle(np.apply_along_axis(lambda args: [complex(*args)], 1, points_c)) % (2 * np.pi)
    return np.column_stack((rads, angles))


def getSorted(points):
    """Converts a list of 2D points to polar coordinates and then lexsorts the result list first by angle, then by radius."""
    points = np.asarray(points)
    midpoint = sum(points) / len(points)
    points_polar = convertToPolar(points, midpoint)
    lexsortindices = np.lexsort((points_polar[:, 0], points_polar[:, 1]))
    points_polar_sorted = points_polar[lexsortindices]
    points_sorted = points[lexsortindices]

    _, idx_start, count = np.unique(points_polar_sorted[:, 1], return_counts=True, return_index=True)
    points_polar_sorted_oneperangle = points_polar_sorted[idx_start + count - 1]
    points_sorted_oneperangle = points_sorted[idx_start + count - 1]
    outmostidx = np.argmax(points_polar_sorted_oneperangle[:, 0])

    return np.roll(points_sorted_oneperangle, -outmostidx, axis=0)


def areCollinear(point1, point2, point3):
    point1, point2, point3 = np.asarray(point1), np.asarray(point2), np.asarray(point3)
    return np.linalg.det(np.column_stack((point1 - point2, point2 - point3))) == 0


def hull_method(pointlist):
    points = getSorted(pointlist)
    outlist = [points[0].tolist()]
    previous_idx, previous = 0, points[0]

    for current_idx, current in enumerate(points[1:], 1):

        # check that all other points are in the left halfplane specified by previous_point, current_point:
        hyperplanevector = current - previous
        normalvector = np.array([-hyperplanevector[1], hyperplanevector[0]])

        # check whether all points are in the left halfspace of the hyperplane (= line) defined by the point "previous" and the vector "hyperplanevector"
        halfspace_check = True
        for vec in it.chain(points[current_idx + 1:, :], points[:previous_idx, :], points[previous_idx + 1: current_idx, :]):
            vec_c = vec - previous
            if np.dot(vec_c, normalvector) < 0:
                halfspace_check = False
                break

        if halfspace_check:
            # remove previous point if collinearity or duplicate would arise
            if len(outlist) >= 2:
                if areCollinear(current, outlist[-1], outlist[-2]):
                    outlist.pop(-1)

            # add current point
            outlist.append(current.tolist())
            previous_idx, previous = current_idx, current

    # remove collinearities from last three outlist points or from connecting outlist points to a closed curve
    if len(outlist) >= 3:
        for i in (-2, -1, 0):
            if areCollinear(outlist[i - 1], outlist[i], outlist[i + 1]):
                outlist.pop(i)

    return outlist
