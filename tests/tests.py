import unittest
from StringIO import StringIO

from codekata04.kata04_part_three import Kata04WeatherTable

weather_test_records = [
    ('   1  88    59    74          53.8       0.00 F       280  9.6 270  17  1.6  93 23 1004.5', (1, 88, 59)),
    ('   9  86    32*   59       6  61.5       0.00         240  7.6 220  12  6.0  78 46 1018.6', (9, 86, 32))
]


class TestKata04WeatherTable(unittest.TestCase):
    def test_record_creation(self):
        for test_record in weather_test_records:
            ds = StringIO(test_record[0])
            wt = Kata04WeatherTable(ds)
            self.assertEqual(len(wt.records), 1)
            self.assertEqual(wt.records[0][0], test_record[1][0])
            self.assertEqual(wt.records[0][1], test_record[1][1])
            self.assertEqual(wt.records[0][2], test_record[1][2])

    def test_min_diff(self):
        ds = StringIO('\n'.join([weather_test_record[0] for weather_test_record in weather_test_records]))
        wt = Kata04WeatherTable(ds)
        self.assertEqual(wt.min_diff()[0], 1)

if __name__ == '__main__':
    unittest.main()
