import os

fs = open("id.csv", "r+")
fd = open("registry.csv", "w+")

for lines in fs:
    lines=lines.split(',')
    fd.write(lines[0]+",\n")

