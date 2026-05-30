# Linux Commands Assignment

> Run on macOS (Darwin). Where a tool differs from Linux, it is noted.

## 1. Creating and Renaming Files/Directories
```bash
mkdir test_dir
touch test_dir/example.txt
mv test_dir/example.txt test_dir/renamed_example.txt
ls -l test_dir
```
**Explanation:** `mkdir` creates the directory, `touch` creates an empty file, and `mv` renames it (moving a file to a new name in the same directory = rename).

**Output:**
```
-rw-r--r--  1 user  staff  0  renamed_example.txt
```

## 2. Viewing File Contents
```bash
cat /etc/passwd          # full contents
head -5 /etc/passwd      # first 5 lines
tail -5 /etc/passwd      # last 5 lines
```
**Explanation:** `cat` dumps the whole file; `head -5`/`tail -5` show only the first/last 5 lines.

## 3. Searching for Patterns
```bash
grep root /etc/passwd
```
**Explanation:** `grep` prints every line containing the pattern "root".

**Output:**
```
root:*:0:0:System Administrator:/var/root:/bin/sh
daemon:*:1:1:System Services:/var/root:/usr/bin/false
_cvmsroot:*:212:212:CVMS Root:/var/empty:/usr/bin/false
```

## 4. Zipping and Unzipping
```bash
zip -r test_dir.zip test_dir
unzip -o test_dir.zip -d unzipped_dir
```
**Explanation:** `zip -r` compresses the directory recursively; `unzip -d` extracts into a chosen directory.

## 5. Downloading Files
```bash
wget https://example.com/sample.txt        # Linux
# macOS has no wget by default -> use curl, or install: brew install wget
curl -L -o sample.txt https://example.com/index.html
```
**Explanation:** `wget` downloads a file from a URL. On macOS `curl -o` is the built-in equivalent.

## 6. Changing Permissions
```bash
touch secure.txt
chmod 444 secure.txt
ls -l secure.txt
```
**Explanation:** `chmod 444` = read-only (`r--`) for owner, group, and others.

**Output:**
```
-r--r--r--  1 user  staff  0  secure.txt
```

## 7. Working with Environment Variables
```bash
export MY_VAR="Hello, Linux!"
echo $MY_VAR
```
**Explanation:** `export` defines an environment variable available to the shell and its child processes. Add to `~/.zshrc` (or `~/.bashrc`) to persist across sessions.

**Output:**
```
Hello, Linux!
```
