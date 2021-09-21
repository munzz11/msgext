#!/usr/bin/env python3

import rosbag
import sys
import argparse

def main():

    original_stdout = sys.stdout
    my_parser = argparse.ArgumentParser(
                    prog='myls',
                    usage='%(prog)s [options] path',
                    description='List the message types in a bag')

    my_parser.add_argument(
                    'Path to bag',
                    metavar='path',
                    type=str,
                    help='The bag file to proccess')

    args = my_parser.parse_args()
    input_path = args.Path

    types = {}

    for bagname in sys.argv[1:]:
        bag = rosbag.Bag(bagname)
        for topic, msg, t in bag.read_messages():
            types[msg._type] = msg._full_text 

    with open(bagname + '_msg_types.txt', 'w') as f:
        sys.stdout = f
        for t in types:
            print ("Message type:", t)
            print ("Message text:")
            print (types[t])
        sys.stdout = original_stdout
