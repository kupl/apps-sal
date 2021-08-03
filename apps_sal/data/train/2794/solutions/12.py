def calculate_age(yob, cy):
    return ['You will be born in %s %s.' % (yob - cy, ['years', 'year'][(yob - cy) < 2]),
            'You are %s %s old.' % (cy - yob, ['years', 'year'][(cy - yob) < 2])][cy - yob > 0] if (cy - yob) != 0 \
        else "You were born this very year!"
