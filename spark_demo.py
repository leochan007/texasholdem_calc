#!/usr/bin/python3
# -*- coding:utf-8 -*-
from pyspark import SparkContext

if __name__ == '__main__' :

    logFile = "README.md"  # Should be some file on your system
    sc = SparkContext("local", "Simple App")
    logData = sc.textFile(logFile).cache()

    numAs = logData.filter(lambda s: 'a' in s).count()
    numBs = logData.filter(lambda s: 'q' in s).count()

    print("Lines with a: %i, lines with q: %i" % (numAs, numBs))

    sc.stop()
    