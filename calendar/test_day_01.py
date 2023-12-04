from unittest import TestCase
from day_01 import Day01


class TestLoaders(TestCase):
    input_1 = [
        '1abc2',
        'pqr3stu8vwx',
        'a1b2c3d4e5f',
        'treb7uchet'
    ]
    input_2 = [
        'two1nine',
        'eightwothree',
        'abcone2threexyz',
        'xtwone3four',
        '4nineeightseven2',
        'zoneight234',
        '7pqrstsixteen'
    ]

    def test_calculate_line_1(self):
        self.assertEqual(Day01.calculate_line(self.input_1[0]), 12)
        self.assertEqual(Day01.calculate_line(self.input_1[1]), 38)
        self.assertEqual(Day01.calculate_line(self.input_1[2]), 15)
        self.assertEqual(Day01.calculate_line(self.input_1[3]), 77)

    def test_calculate_total_1(self):
        self.assertEqual(Day01.calculate_total(self.input_1), 142)

    def test_calculate_line_2(self):
        self.assertEqual(Day01.calculate_line(self.input_2[0]), 29)
        self.assertEqual(Day01.calculate_line(self.input_2[1]), 83)
        self.assertEqual(Day01.calculate_line(self.input_2[2]), 13)
        self.assertEqual(Day01.calculate_line(self.input_2[3]), 24)
        self.assertEqual(Day01.calculate_line(self.input_2[4]), 42)
        self.assertEqual(Day01.calculate_line(self.input_2[5]), 14)
        self.assertEqual(Day01.calculate_line(self.input_2[6]), 76)
        self.assertEqual(Day01.calculate_line(self.input_2[6]), 76)
    
    def test_calculate_line_overlap(self):
        self.assertEqual(Day01.calculate_line('oneight'), 18)
        
    def test_calculate_total_2(self):
        self.assertEqual(Day01.calculate_total(self.input_2), 281)
