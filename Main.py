# encoding: utf-8

import Structure as st

tree = st.SuffixTree()

with open('t2.txt') as file:
    while True:
        line = file.readline()

        if line == '':
            break
        else:
            line = line.split()[0]
            treeno, line = line.split(':')
            line = line.split(',')

        l = len(line)

        for i in range(-1, -l-1, -1):
            tree.insert(line[i:], treeno)

while True:
    x = input('\nPlease enter pattern to search: ')
    x = x.split()

    if x == []:
        print('end program')
        break
    else:
        tree.search(x)



