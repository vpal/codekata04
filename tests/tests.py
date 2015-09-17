import unittest
from StringIO import StringIO

from codekata04.kata04_part_three import (
    Kata04WeatherTable,
    Kata04FootballTable
)


class Kata04Tests(unittest.TestCase):
    def common_test_record_creation(self):
        for test_item in self.test_items:
            ds = StringIO(test_item[0])
            t = self.target_class(ds)
            self.assertEqual(len(t.records), 1)
            self.assertEqual(t.records[0][0], test_item[1][0])
            self.assertEqual(t.records[0][1], test_item[1][1])
            self.assertEqual(t.records[0][2], test_item[1][2])

    def common_test_min_diff(self):
        ds = StringIO('\n'.join([test_item[0] for test_item in self.test_items]))
        t = self.target_class(ds)
        self.assertEqual(t.min_diff()[0], self.min_value)


class TestKata04WeatherTable(Kata04Tests):
    target_class = Kata04WeatherTable
    test_items = [
        ('   1  88    59    74          53.8       0.00 F       280  9.6 270  17  1.6  93 23 1004.5', (1, 88, 59)),
        ('   9  86    32*   59       6  61.5       0.00         240  7.6 220  12  6.0  78 46 1018.6', (9, 86, 32))
    ]
    min_value = 1

    def test_record_creation(self):
        super(TestKata04WeatherTable, self).common_test_record_creation()

    def test_min_diff(self):
        super(TestKata04WeatherTable, self).common_test_min_diff()


class TestKata04FootballTable(Kata04Tests):
    target_class = Kata04FootballTable
    test_items = [
        ('    6. Chelsea         38    17  13   8    66  -  38    64', ('Chelsea', 66, 38)),
        ('   12. Middlesbrough   38    12   9  17    35  -  47    45', ('Middlesbrough', 35, 47))
    ]
    min_value = 'Middlesbrough'

    def test_record_creation(self):
        super(TestKata04FootballTable, self).common_test_record_creation()

    def test_min_diff(self):
        super(TestKata04FootballTable, self).common_test_min_diff()


if __name__ == '__main__':
    unittest.main()
