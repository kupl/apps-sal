from collections import Counter
from itertools import cycle, islice
RESPONSE_POS = 'positive'
WEEK_LEN = 7


def love_language(partner, weeks):

    def positive(response):
        return response == RESPONSE_POS
    queries = islice(cycle(LOVE_LANGUAGES), weeks * WEEK_LEN)
    tests = ((query, partner.response(query)) for query in queries)
    stats = Counter((query for (query, response) in tests if positive(response)))
    [(winner, count)] = stats.most_common(1)
    return winner
