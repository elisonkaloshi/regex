import re
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-e', '--email', action='store_true',
                    help="Filter emails")

parser.add_argument('-i', '--ip', action='store_true',
                    help="Filter IP addresses")

parser.add_argument('-g', '--guid', action='store_true',
                    help="Filter GUID")

parser.add_argument('-t', '--timestamp', action='store_true',
                    help="Filter Timestamps")

parser.add_argument('-m', '--manual', action='store_true',
                    help="Manual regex")

args = parser.parse_args()

def filter_using_regex(regex_code):
    regex = re.compile(regex_code)
    print(regex)

    for line in open("top-secret-file.txt"):
        for match in re.finditer(regex, line):
            print(line)

if args.email:
    filter_using_regex("[A-Za-z0-9]+([-]?[._]?)+[A-Za-z0-9]+@[A-Za-z0-9]+\.(com|edu|net)")

if args.ip:
    filter_using_regex("(([01]?[0-9][0-9]?)\.){3}([01]?[0-9][0-9]?)")

if args.guid:
    filter_using_regex("([A-Za-z0-9]){8}-([A-Za-z0-9]){4}-([A-Za-z0-9]){4}-([A-Za-z0-9]){4}-([A-Za-z0-9]){12}")

if args.timestamp:
    filter_using_regex("([0-9]{4})-([0-9]{2})-([0-9]{2}(T|Z)[0-9]{2}):([0-9]{2}:[0-9]{2}.[0-9]{3})(T|Z)")

if args.manual:
    regex_manual = raw_input("Please give your regex: ")
    filter_using_regex(regex_manual)

