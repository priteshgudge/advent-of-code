f = open('input/aocday1.txt')

elf_calorie_list = []
calorie_count = 0

line = f.readline()

while line:
    if line == '\n':
        elf_calorie_list.append(calorie_count)
        calorie_count = 0
    else:
        calorie_count += int(line.strip())
    line = f.readline()

print(sum((sorted(elf_calorie_list)[-3:])))
