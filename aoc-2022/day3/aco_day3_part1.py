
def priority(char):
    if (ord(char) >= ord('a') and ord(char) <= ord('z')):
        priority = ord(char) - 97 + 1
    elif ord(char) >= ord('A') and ord(char) <= ord('Z'):
        priority = ord(char) - 65 + 27
    else:
        exit("Error")
    return priority



f = open('input.txt')
line = f.readline()

total_priority = 0

while line:
    line = line[:-1]
    first_part = line[:len(line)//2]
    second_part = line[len(line)//2:]
    temp_dict = dict()
    for ch in list(first_part):
        temp_dict[ch] = 1
        
    for ch in list(second_part):
        if ch in temp_dict:
            break
   # breakpoint()
    total_priority += priority(ch)
    line = f.readline()

print(total_priority)
