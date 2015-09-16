import sys
import re


def main():
    day = None
    min_t = None
    max_t = None
    min_spread = None
    with open(sys.argv[1]) as tablefile:
        lines = tablefile.readlines()

    for line in lines:
        if re.search('^(\s*\d+)', line):
            rec = [int(field.rstrip('*')) for field in line.split()[:3]]
            diff = rec[1] - rec[2]

            if min_spread is None or diff < min_spread:
                min_spread = diff
                day, max_t, min_t = rec

    print(day)


if __name__ == '__main__':
    main()
