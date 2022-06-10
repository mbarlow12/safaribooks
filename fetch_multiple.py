#! /usr/bin/env python3

from types import SimpleNamespace

from safaribooks import SafariBooks

id_list = []

with open('ids.txt', 'r') as id_file:
    id_list = id_file.read().split('\n')

if len(id_list):
    print('Fetching...\n')
    print(id_list)

for book_id in id_list:
    if not book_id:
        continue
    args = SimpleNamespace(bookid=book_id, cred=None, kindle=True, no_cookies=True, log=True)
    SafariBooks(args)
