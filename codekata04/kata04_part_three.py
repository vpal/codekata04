import sys
import re


class Kata04Table(object):
    record_pattern = '^(\s*\d+)'

    def __init__(self, filename):
        self.filename = filename
        self.records = None
        self.read()

    def min_diff(self):
        return min(self.records, key=lambda r: abs(r[1] - r[2]))

    def read(self):
        with open(self.filename, 'r') as tablefile:
            lines = tablefile.readlines()

        table_lines = filter(lambda l: re.search(self.record_pattern, l), lines)
        self.records = [self.read_record(table_line.strip()) for table_line in table_lines]

    def read_record(self, line):
        raise NotImplementedError()


class Kata04WeatherTable(Kata04Table):
    def read_record(self, line):
        return [int(field.rstrip('*')) for field in line.split()[:3]]


class Kata04FootballTable(Kata04Table):
    def read_record(self, line):
        fields = line.split()
        return fields[1], int(fields[6]), int(fields[8])


def main():
    if 'weather' in sys.argv[1]:
        dt = Kata04WeatherTable(sys.argv[1])
    elif 'football' in sys.argv[1]:
        dt = Kata04FootballTable(sys.argv[1])

    min_diff_rec = dt.min_diff()
    print(min_diff_rec[0])


if __name__ == '__main__':
    main()