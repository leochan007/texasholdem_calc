#!/usr/bin/python3
# -*- coding:utf-8 -*-

import csv

import time

import sys

if __name__ == '__main__' :

    csvfile = open('cards.csv', 'r')
    reader = csv.reader(csvfile)
    total = 0
    n = 2

    if len(sys.argv) > 1 :
        n = int(sys.argv[1])
    
    print ('num of players:', n)

    count = dict()
    card_def = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
    for card in card_def :
        count[card] = 0

    for line in reader:
        total += 1
        if line[0][0] == line[n][0] :
            count[line[0][0]] += 1 
            
    for card in card_def :
        print('total:%d count[%s]:%d %s' % (total, card, count[card], 
        "{c}{c}: {p}%".format(c =card, p = count[card] * 100.0 / total)))
    csvfile.close()