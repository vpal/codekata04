import sys
import re


def main():
    team = None
    sc_for = None
    sc_against = None
    min_diff = None
    with open(sys.argv[1]) as tablefile:
        lines = tablefile.readlines()

    for line in lines:
        if re.search('^(\s*\d+)', line):
            fields = line.split()
            rec = fields[1], int(fields[6]), int(fields[8])
            diff = abs(rec[1] - rec[2])

            if min_diff is None or diff < min_diff:
                min_diff = diff
                team, sc_for, sc_against = rec

    print(team)


if __name__ == '__main__':
    main()
