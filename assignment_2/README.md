# Assignment 2 — Python and Bash

Four small Python programs covering conditionals, dictionaries, and file I/O.

## Task 1 — Grade Checker (`grade_checker.py`)
Takes a score as input and prints a grade using a basic `if/elif/else` ladder.

| Score | Grade |
|-------|-------|
| 90+   | A |
| 80–89 | B |
| 70–79 | C |
| 60–69 | D |
| < 60  | F |

```bash
echo "85" | python3 grade_checker.py   # -> Grade: B
echo "55" | python3 grade_checker.py   # -> Grade: F
```
**Explanation:** `int(input(...))` reads the score, then the `if/elif/else` chain checks the highest threshold first and returns the matching letter.

## Task 2 — Student Grades (`student_grades.py`)
A dictionary maps student names (keys) → grades (values), with a menu loop to:
- **Add** a new student and grade
- **Update** an existing student's grade
- **Print** all student grades

```bash
# Demo: add Alice=A, add Bob=C, update Bob->B, print, exit
printf "1\nAlice\nA\n1\nBob\nC\n2\nBob\nB\n3\n4\n" | python3 student_grades.py
```
**Output:**
```
--- Student Grades ---
Alice: A
Bob: B
```
**Explanation:** `students[name] = grade` adds/updates an entry; `if name in students` decides between add and update; a `for name, grade in students.items()` loop prints them all.

## Task 3 — Write to a File (`write_file.py`)
Creates `sample_output.txt` and writes three lines using `open(..., "w")` and `f.write()`.

```bash
python3 write_file.py   # -> Content written to sample_output.txt
```
**Explanation:** `open(path, "w")` opens the file in write mode (creating/overwriting it); `with` auto-closes it. `\n` ends each line.

## Task 4 — Read from a File (`read_file.py`)
Opens the file in read mode and prints its contents with `file.read()`.

```bash
python3 read_file.py
```
**Output:**
```
Hello, this is line 1.
This content was written by write_file.py.
Python file handling is easy!
```
**Explanation:** `open(path, "r")` opens in read mode; `f.read()` returns the whole file as one string, which we print.

## Run all
```bash
python3 grade_checker.py
python3 student_grades.py
python3 write_file.py
python3 read_file.py
```
