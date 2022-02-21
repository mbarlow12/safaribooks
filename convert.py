#!/usr/bin/env python3

import os
import re

home = '/home/michael'
books_dir = home + '/books'

def extract_title(title_and_id):
    pattern = r"(?P<name>[^\(]+) \((?P<id>\d+)\)"
    m = re.compile(pattern).match(title_and_id)
    return m.group('name'), m.group('id')

if __name__ == '__main__':
    current = os.getcwd()
    base = os.path.basename(current)
    title, bookid = extract_title(base)
    inpath = current + "/" + bookid + ".epub"
    outpath = current + "/" + title + ".epub"
    command = "ebook-convert \"" + inpath + "\" \"" + outpath + "\""
    os.system(command)

    # for title_id in book_dirs:
    #     title, bookid = extract_title(title_id)
    #     book_dir = books_dir + "/" + title_id


