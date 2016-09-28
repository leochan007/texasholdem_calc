#!/usr/bin/python3
# -*- coding:utf-8 -*-

import csv

import time

if __name__ == '__main__' :

    csvfile = open('cards.csv', 'r')
    reader = csv.reader(csvfile)
    countAA = 0
    countKK = 0
    total = 0
    n = 2
    for line in reader:
        total += 1
        if line[0].find('A') != -1 and line[n].find('A') != -1 :
            countAA += 1 
        if line[1].find('K') != -1 and line[1 + n].find('K') != -1 :
            countKK += 1 
    print('total:%d countAA:%d' %(total, countAA))
    print('total:%d countKK:%d' %(total, countKK))
    print('AA percentage: {p}%'.format(p = countAA * 100.0 / total))
    print('KK percentage: {p}%'.format(p = countKK * 100.0 / total))
    csvfile.close()