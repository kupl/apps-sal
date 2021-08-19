from datetime import date


def unlucky_days(year):
    # Only need to check the 13th of each month
    day = 13

    # Counter for unlucky days
    unlucky_days_count = 0

    # Loop through the months (1 to 12)
    for x in range(1, 13):
        # Create date object for each month
        date_obj = date(year=year, month=x, day=day)

        # Check if the 13th of current month is Friday
        # Weekdays range from 0 (Monday) to 6 (Sunday)
        if date_obj.weekday() == 4:
            # Increment unlucky days counter if current 13th is Friday
            unlucky_days_count += 1

    # Return the unlucky days counter
    return unlucky_days_count
