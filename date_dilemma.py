#A script to parse YMD and MDY dates into an ISO 8601 (YYYY-MM-DD) formatted date.

import sys
from string import ascii_letters

def get_date(d):
    for i in d:
        if i in ascii_letters:
            sys.exit("Wrong Input, terminating")
    try:
        if d[:4].isnumeric(): ymd=1
        elif d[:2].isnumeric(): ymd=11
        else: ymd=10
        if ymd==1:
            d=d.split(d[4])
            if len(d[1])==1:
                d[1]='0'+d[1]
            if len(d[2])==1:
                d[2]='0'+d[2]
            return d
        elif ymd==10:
            d=d.split(d[1])
            d[0]='0'+d[0]
        else: d=d.split(d[2]);
        if len(d[1])==1:
            d[1]='0'+d[1]
        if len(d[2])==2:
            d[2]='20'+d[2]
        return [d[2], d[0], d[1]]
    except IndexError:
        sys.exit("Wrong Input, terminating")
if __name__ == '__main__':
    while True:
        print('-'.join(get_date(input())))
