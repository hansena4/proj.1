"""Searches deep inside a directory structure, looking for most amount of duplicate files and the duplicates taking
up the most hard drive space. Duplicates aka copies have the same content, but not necessarily the same name. """
__author__ = "Amalie Hansen"
__email__ = "amaliebhansen@hotmail.com"
__version__ = "1.0"

# noinspection PyUnresolvedReferences
from os.path import getsize, join
from time import time

# noinspection PyUnresolvedReferences
from p1utils import all_files, compare

def search(file_list):
    lol = []
    while 0 < len(file_list):
        dups = []
        next = []
        for i in file_list:
            if compare(file_list[0], i):
                dups.append(i)
            else:
                next.append(i)
        if 1 < len(dups):
            lol.append(dups)
        file_list = next
    return lol


def faster_search(file_list):
    file_sizes = list(map(getsize, file_list))
    file_list = list(filter(lambda x: 1 < file_sizes.count(getsize(x)), file_list))
    lol = []
    while 0 < len(file_list):
        dups = [file_list.pop(0)]
        for i in range(len(file_list) - 1, -1, -1):
            if compare(dups[0], file_list[i]):
                dups.append(file_list.pop(i))
        if 1 < len(dups):
            lol.append(dups)
    return lol

def report(lol):
    if 0 < len(lol):
        print("== == Duplicate File Finder Report == ==")

        ll = max(lol, key=len)
        ll.sort()
        print(f"The file with the most duplicates is:\n {ll[0]}")
        print(f"Here are its {len(ll) - 1} copies:")
        for i in range(1,len(ll)):
            print(ll[i])

        ll = max(lol, key=lambda x: len(x) * getsize(x[0]))

        ll.sort()
        print(f"\nThe most disk space ({(len(ll) -1)* getsize(ll[0])}) could be recovered, by deleting copies of this file:\n {ll[0]}")
        print(f"here are its copies {len(ll)-1}")
        for i in range(1,len(ll)):
            print(ll[i])
    else:
        print("No duplicates found")



if __name__ == '__main__':
    path = join(".", "images")

    t0 = time()
    report(search(all_files(path)))
    print(f"Runtime: {time() - t0:.2f} seconds")

    print("\n\n .. and now w/ a faster search implementation:")

    t0 = time()
    report(faster_search(all_files(path)))
    print(f"Runtime: {time() - t0:.2f} seconds")

