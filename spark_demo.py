#!/usr/bin/python3
# -*- coding:utf-8 -*-
from pyspark import SparkContext

import numpy as np
import csv
import sys
import time
import random

def swap(a, b) :
    return b, a

def init_cards(card_def, suitdef):
    cards = list()
    cards_str = list()
    a = 0
    b = 1
    sa = 0
    sb = -1
    for i in range(n) :
        if i % 13 == 0 :
            sa = 0
            sb += 1
            a += 100
            b = 1
        cards.append('%d.jpg' % (a + b))
        cards_str.append('%s%s' % (card_def[sa], suit_def[sb]))
        sa += 1
        b += 1
    return cards, cards_str

def add_to_res(cards_str):
    data.append(cards_str)    

def gen_cards2(cards) :
    n = 52
    for i in range(n) :
        j = random.randint(i, n - 1)
        cards[0][i], cards[0][j] = swap(cards[0][i], cards[0][j])
        cards[1][i], cards[1][j] = swap(cards[1][i], cards[1][j])
    return cards[0], cards[1]

if __name__ == '__main__' :

    logFile = "README.md"  # Should be some file on your system
    sc = SparkContext("local", "texas hold'em calc")

    n = 52
    card_def = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
    suit_def = ['s', 'h', 'c', 'd']

    csvfile = open('cards.csv', 'w')
    writer = csv.writer(csvfile)
    count = 100000

    if len(sys.argv) > 1 :
        count = int(sys.argv[1])

    print ('num of card game:', count)
    data = list()
    t = time.time()
    cards, cards_str = init_cards(card_def, suit_def)
    
    lst = [[cards, cards_str] for n in range(count)]
    distData = sc.parallelize(lst)

    ori_data = distData.map(gen_cards2)
    data = ori_data.map(lambda a: a[1]).collect()

    print('time to gen data:', time.time() - t)
    t = time.time()
    print('len of data:', len(data))
    writer.writerows(data)
    print('time to write:', time.time() - t)
    csvfile.close()

    sc.stop()
    