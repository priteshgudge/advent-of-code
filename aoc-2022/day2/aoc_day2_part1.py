map_points = {
    "A_X": 4,
    "B_X": 1,
    "C_X": 7, 
    "A_Y": 8,
    "B_Y": 5,
    "C_Y": 2,
    "A_Z": 3,
    "B_Z": 9,
    "C_Z": 6
}
f = open('input.txt')
line = f.readline()
total = 0
while line:
    total += map_points['_'.join(line.split())]
    line = f.readline()
print(total)
