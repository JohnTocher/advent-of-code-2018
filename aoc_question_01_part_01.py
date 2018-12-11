#!/usr/bin/env python

""" Advent of Code 2018 - Question 1

    Solution by John Tocher

"""

import os

INPUT_FILE = "aoc_q01_input.txt"

def solve_the_puzzle():
    """ Code for the Advent code qestion """
    input_file = os.path.join(INPUT_FILE)

    with open(input_file, "r") as puzzle_input:
        line_count = 0
        counter = 0
        for each_line in puzzle_input.readlines():
            line_count += 1
            counter += int(each_line.strip())

        print(f"Read {line_count} lines. Result was {counter}")

if __name__ == "__main__":
    solve_the_puzzle()
