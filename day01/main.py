"""
This module provides functionality for working with collections.
It imports the Counter class from the collections module to count occurrences of elements.
"""

from collections import Counter


def solve2():
    """Solution of part-2"""
    counter = Counter(input2)
    ans = 0
    for num in input1:
        ans += int(num) * counter[num]
    return ans


def solve1():
    """Solution of part-1"""
    ans = 0
    input1.sort()
    input2.sort()
    for num1, num2 in zip(input1, input2):
        ans += abs(int(num1) - int(num2))
    return ans


with open("./inputs.txt", "r", encoding="utf-8") as file:
    data = file.read().strip().split()
    input1 = data[0::2]
    input2 = data[1::2]

print(f"Solution of part-1: {solve1()}")
print(f"Solution of part-2: {solve2()}")
