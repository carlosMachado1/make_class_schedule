#
# Make a regular expression to look for our subjects
#

import re


def read_data(dest_):
    # data = {}
    archive = open(file=dest_, mode="r")
    linhas = archive.readlines()
    print(len(linhas))


a = read_data("file_example.txt")
