f = open('input/aocday1.txt')

calorie_count = 0
max_calorie_count = -1000000

line = f.readline()

while line:
    if line == '\n':
        if calorie_count > max_calorie_count:
            max_calorie_count = calorie_count
            
        calorie_count = 0
    else:
        calorie_count += int(line.strip())
    line = f.readline()

print(max_calorie_count)
