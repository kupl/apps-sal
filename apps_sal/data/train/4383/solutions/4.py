def artificial_rain(garden):
    max_sections = 1
    curr_sections = 1
    flat_sections = 1
    previous = garden[0]
    slope = 'downhill'
    for section in garden[1:]:
        if slope == 'downhill' and section > previous:
            if curr_sections > max_sections:
                max_sections = curr_sections
            curr_sections = flat_sections + 1
            flat_sections = 1
            slope = 'uphill'
        elif slope == 'uphill' and section < previous:
            curr_sections += 1
            flat_sections = 1
            slope = 'downhill'
        else:
            curr_sections += 1
            if section == previous:
                flat_sections += 1
            else:
                flat_sections = 1
        previous = section
    if curr_sections > max_sections:
        max_sections = curr_sections
    return max_sections
