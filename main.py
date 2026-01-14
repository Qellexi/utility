import os
import re

def analyze_file(path):
    total = 0
    empty = 0
    comments = 0
    logical = 0
    cyclomatic = 1

    in_multiline_comment = False

    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            total += 1
            stripped = line.strip()

            # empty lines
            if stripped == "":
                empty += 1
                continue

            # multiline comment
            if in_multiline_comment:
                comments += 1
                if "*/" in stripped:
                    in_multiline_comment = False
                continue
            
            if "/*" in stripped:
                comments += 1
                if "*/" not in stripped:
                    in_multiline_comment = True
                continue


            # single-line comment
            if stripped.startswith("//") or stripped.startswith("#"):
                comments += 1
                continue

            # logical lines (count ; or statements)
            logical += 1

            # cyclomatic complexity (count decision points)
            cyclomatic += len(re.findall(r"\b(if|elif|else|for|while|case|catch)\b", stripped))
            

    return total, empty, comments, logical, cyclomatic


def analyze_directory(path):
    total = empty = comments = logical = cyclomatic = 0

    for root, _, files in os.walk(path):
        for file in files:
            if file.endswith((".py", ".c", ".cpp", ".java", ".js")):
                file_path = os.path.join(root, file)
                t, e, c, l, cy = analyze_file(file_path)

                total += t
                empty += e
                comments += c
                logical += l
                cyclomatic += cy

    return total, empty, comments, logical, cyclomatic


# ---------------------------
# RUN
# ---------------------------
path = input("Enter path to project: ")

total, empty, comments, logical, cyclomatic = analyze_directory(path)

print("Total lines:", total)
print("Empty lines:", empty)
print("Logical lines:", logical)
print("Comment lines:", comments)
print("Comment level:", round(comments / total * 100, 2), "%")
print("Cyclomatic complexity:", cyclomatic)
