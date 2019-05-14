import os


def persist_tweet_in_file(tweet_content, filename):
    file = open(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))) + "/resources/" +
                filename, "w")
    file.write(str(tweet_content))
    file.close()
