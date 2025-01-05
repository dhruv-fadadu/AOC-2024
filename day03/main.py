"""
This module provides functionality for working with regex.
"""

import re


def solve2():
    """Solution of part-2"""
    ans = 0
    regex_to_match = r"do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\)"
    matches = re.findall(regex_to_match, data)
    enables = True
    for match in matches:
        if match == "do()":
            enables = True
            continue
        elif match == "don't()":
            enables = False
            continue
        if enables:
            regex_to_find_num = r"(\d{1,3})"
            num1, num2 = re.findall(regex_to_find_num, match)
            ans += int(num1) * int(num2)
    return ans


def solve1():
    """Solution of part-1"""
    ans = 0
    regex_to_match = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(regex_to_match, data)
    for match in matches:
        ans += int(match[0]) * int(match[1])
    return ans


with open("./inputs.txt", "r", encoding="utf-8") as file:
    data = file.read().strip()

print(f"Solution of part-1: {solve1()}")
print(f"Solution of part-2: {solve2()}")
