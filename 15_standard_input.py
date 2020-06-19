import fileinput

for line in fileinput.input():
    print(line, end='')
    if line == "end\n":
        break

