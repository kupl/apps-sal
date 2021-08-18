def omit_hashtag(message, hashtag):
    if hashtag in message:
        found_at = message.index(hashtag)
        return message[0:found_at] + message[found_at + len(hashtag):]
    else:
        return message
