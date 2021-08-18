def spinning_rings(inner_max, outer_max):

    outer_ring = 0
    count = 1
    if inner_max > outer_max:
        while True:
            count += (inner_max - outer_max)
            inner_ring = outer_max
            outer_ring += ((count) % (outer_max + 1))

            if (inner_ring - outer_ring) % 2 == 0:
                count += (inner_ring - outer_ring) // 2
                return count
            else:
                count += (outer_max - outer_ring) + 1
                inner_ring -= (outer_ring)
                if inner_ring % 2 == 0:
                    count += (inner_ring // 2)
                    return count
                else:
                    dist = (inner_max + 1) // (outer_max + 1)
                    steps = dist * (outer_max + 1)
                    if inner_max % 2 == outer_max % 2:
                        inner_ring = (inner_max - steps)
                        count = steps + (inner_ring) // 2
                        return count + 1
                    elif(inner_max - steps - 1) % 2 == 0:
                        inner_ring = (inner_max - steps)
                        count = steps + inner_ring // 2
                        return count + 1
                    else:

                        count = inner_max + (inner_max - outer_max) + 1
                        outer_ring = count % (outer_max + 1)
                        count += (outer_max - outer_ring) // 2
                return count + 1

    elif outer_max > inner_max:
        inner_ring = inner_max
        count = 1
        outer_ring = 1
        while True:
            if (inner_ring - outer_ring) % 2 == 0:
                count += (inner_ring - outer_ring) // 2
                return count
            else:
                count = (outer_max)
                outer_ring = 0
                inner_ring -= count % (inner_max + 1)
                count += 1
                if inner_ring % 2 == 0:
                    count += inner_ring // 2
                    return count
                else:
                    count += inner_ring + 1
                    outer_ring += inner_ring + 1
                    inner_ring = inner_max
                    count += (inner_ring - outer_ring) // 2
                return count
    else:
        if(outer_max - 1) % 2 == 0:
            return count + outer_max // 2
