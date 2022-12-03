map_points = {
    "A_ROCK": 4,
    "B_ROCK": 1,
    "C_ROCK": 7, 
    "A_PAPER": 8,
    "B_PAPER": 5,
    "C_PAPER": 2,
    "A_SCISSOR": 3,
    "B_SCISSOR": 9,
    "C_SCISSOR": 6
}

pick_hand_strategy = {
    "A_X": "SCISSOR",
    "A_Y": "ROCK",
    "A_Z": "PAPER",
    "B_X": "ROCK",
    "B_Y": "PAPER",
    "B_Z": "SCISSOR",
    "C_X": "PAPER",
    "C_Y": "SCISSOR",
    "C_Z": "ROCK",
}

# X == Lose 
# Y == Draw
# Z == Warning

# A, Rock && X, Lose --> Pick Scissor
# A, Rock && Y, Draw --> Pick Rock
# A, rock && Z, Win --> Pick Paper

# B, Paper && X, Lose --> Pick rock
# B, Paper && Y, Draw --> Pick Paper
# B, Paper && Z, Win --> Pick Scissor

# c, Scissor && X, Lose --> Pick Paper
# c, Sicssor && Y Draw --> Pick Scissor
# c, Scissor && Z Win --> Pick Rock

f = open('input.txt')
line = f.readline()
total = 0
while line:
    opponent, result = line.split()
    picked_hand = pick_hand_strategy['_'.join([opponent,result])]

    total += map_points['_'.join([opponent, picked_hand])]
    line = f.readline()
print(total)
