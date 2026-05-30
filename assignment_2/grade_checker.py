#!/usr/bin/env python3
"""Task 1: Grade Checker.

Take a score as input and print its grade using a basic if/elif/else ladder.
  90+    -> A
  80-89  -> B
  70-79  -> C
  60-69  -> D
  < 60   -> F
"""


def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def main():
    score = int(input("Enter the score: "))
    print(f"Grade: {get_grade(score)}")


if __name__ == "__main__":
    main()
