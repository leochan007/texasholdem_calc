#!/usr/bin/python3
# -*- coding:utf-8 -*-

import random

import csv

import time

import sys

def swap(a, b) :
    return b, a

def gen_cards(card_def, suitdef) :
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
    for i in range(n) :
        j = random.randint(i, n - 1)
        cards[i], cards[j] = swap(cards[i], cards[j])
        cards_str[i], cards_str[j] = swap(cards_str[i], cards_str[j])
    return cards, cards_str

if __name__ == '__main__' :
    n = 52
    card_def = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
    suit_def = ['s', 'h', 'c', 'd']

    csvfile = open('cards.csv', 'w', newline = '')
    writer = csv.writer(csvfile)
    count = 100000

    if len(sys.argv) > 1 :
        count = int(sys.argv[1])

    print ('num of card game:', count)
    data = list()
    t = time.time()
    for i in range(count) :
        cards, cards_str = gen_cards(card_def, suit_def)
        data.append(cards_str)

    print('time to gen data:', time.time() - t)
    t = time.time()
    writer.writerows(data)
    print('time to write:', time.time() - t)
    csvfile.close()
