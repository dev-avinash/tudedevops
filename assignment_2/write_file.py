#!/usr/bin/env python3
"""Task 3: Write to a File.

Create a text file and write some content to it using open() in write mode.
"""


def main():
    with open("sample_output.txt", "w") as f:
        f.write("Hello, this is line 1.\n")
        f.write("This content was written by write_file.py.\n")
        f.write("Python file handling is easy!\n")
    print("Content written to sample_output.txt")


if __name__ == "__main__":
    main()
