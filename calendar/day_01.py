import re
from typing import Dict, List

class Day01:
    extra_string_int: Dict[str, int] = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
    }

    @staticmethod
    def calculate_line(s: str):
        extra_string = '|'.join(list(Day01.extra_string_int))
        # https://stackoverflow.com/questions/11430863/how-to-find-overlapping-matches-with-a-regexp
        all = re.findall(rf"(?=({extra_string}|\d))", s)  # all = re.findall(r"\d", s)
        digits = Day01.convert_digit(all[0]) + Day01.convert_digit(all[-1])
        print(f'{digits} : {s}')
        return int(digits)
    
    @staticmethod
    def calculate_total(data: List[str]):
        total = 0
        for s in data:
            total += Day01.calculate_line(s)
        return total

    @staticmethod
    def convert_digit(s: str):
        if s in Day01.extra_string_int:
            return str(Day01.extra_string_int[s])
        
        return s


if __name__ == "__main__":
    with open('inputs/input_01.csv', 'r', encoding='utf-8') as puzzleinput:
        data = puzzleinput.read().splitlines()
        print(Day01.calculate_total(data))
