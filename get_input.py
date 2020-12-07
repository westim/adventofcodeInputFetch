import os
import argparse
import datetime
import urllib.request

parser = argparse.ArgumentParser(description='Download Advent of Code input.')
parser.add_argument('year', type=int, help='year to download from')
parser.add_argument('day', type=int, help='day to download from')
args = parser.parse_args()

current_date = datetime.datetime.today()
if args.day < 0 or args.day > 31:
    exit(f'Day {args.day} is not valid')
if args.year < 2015 or args.year > current_date.year:
    exit(f'Year {args.year} is not valid')

cookie_file = None
for root, dirs, files in os.walk('./'):
    for f in files:
        if 'cookie' in f:
            cookie_file = f
            break

if cookie_file is None:
    exit('Cookie file not found')

cookie = None
with open(cookie_file, 'r') as f:
    cookie = f.readline().strip()

url = f'https://adventofcode.com/{args.year}/day/{args.day}/input'
headers = [('Cookie', f'session={cookie}')]

opener = urllib.request.build_opener()
opener.addheaders = headers

with opener.open(url) as f:
    content = f.read().decode('utf-8').strip()
    out = open(f'{args.year}day{args.day}.txt', 'w')
    out.write(content)
    out.close()
