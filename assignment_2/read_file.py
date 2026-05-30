#!/usr/bin/env python3
"""Task 4: Read from a File.

Open a text file in read mode and print its contents using file.read().
"""


def main():
    with open("sample_output.txt", "r") as f:
        content = f.read()
    print("--- File contents ---")
    print(content)


if __name__ == "__main__":
    main()
