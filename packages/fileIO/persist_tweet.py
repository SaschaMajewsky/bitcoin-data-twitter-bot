import os
import platform


def persist_tweet_in_file(tweet_content, filename):
    if platform.system() == 'Windows':
        file = open(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))) + "/resources/" +
                    filename, "w")
    elif platform.system() == 'Linux':
        file = open(os.path.normpath(os.getcwd() + os.sep + os.pardir + os.sep + os.pardir + "/resources/" +
                                     filename), "w")
    file.write(str(tweet_content))
    file.close()
