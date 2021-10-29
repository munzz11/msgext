#!/usr/bin/env python3

import rosbag
import sys
import argparse
import os

def main():

    base_path = 'pkg'
    os.mkdir(base_path) 
    types = {}

    for bagname in sys.argv[1:]:
        bag = rosbag.Bag(bagname)
        for topic, msg, t in bag.read_messages():
            types[msg._type] = msg._full_text 
    with open(bagname + '_msg_types.txt', 'w') as f:
        # sys.stdout = f
        for t in types:
            direct = base_path
            direct_arr = t.split('/')
            #print (direct_arr)
            for i in direct_arr:
                direct = (direct + '/' + i)
                try:
                    os.mkdir(direct)
                except FileExistsError:
                    print()
                


            # print ("Message type:", t)
            # print ("Message text:")
            # print (types[t])
            # print ()
