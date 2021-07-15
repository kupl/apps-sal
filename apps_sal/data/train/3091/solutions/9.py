# Return the message, but with the first occurrence (if any) of the
# specified hashtag removed from the message
def omit_hashtag(message, hashtag):
    if hashtag in message:
        found_at = message.index(hashtag)
        return message[0:found_at] + message[found_at + len(hashtag):]
    else:
        return message
