import os


def get_consumer_key():
    return read_line()[0]


def get_consumer_secret():
    return read_line()[1]


def get_access_key():
    return read_line()[2]


def get_access_secret():
    return read_line()[3]


def read_line():
    file = open(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))) + "/resources/api_keys.txt")
    lines = file.readlines()
    file.close()
    return [lines[4].split("\n")[0], lines[6].split("\n")[0], lines[8].split("\n")[0], lines[10].split("\n")[0]]
