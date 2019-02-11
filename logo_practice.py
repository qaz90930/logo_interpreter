import matplotlib.pyplot as plt
import math
import sys

def interpret_logo(file_name):
    with open(file_name, 'r') as fh:
        separate_lines(fh)

def separate_lines(fh):
    paths = []
    for lines in fh.readlines():
        paths.append(lines)
    print(paths)
    instructions(paths)

def instructions(paths):
    degrees = 0
    coordinates = [0, 0]
    moves = []
    for path in paths:
        (command, variable) = path.split(' ')
        if command == 'forward':
            length = int(variable)
            x = length * math.sin(math.radians(degrees))
            y = -length * math.cos(math.radians(degrees))
            coordinates = [int(coordinates[0]+x), int(coordinates[1]+y)]
            moves.append(coordinates)
        elif command == "right":
            degrees += int(variable)
        elif command == 'left':
            degrees -= int(variable)
        else:
            print("wrong path")
    move_the_turtle(moves)
def move_the_turtle(moves):
    print(moves)
    plt.plot([move[0] for move in moves], [move[1] for move in moves])
    plt.plot([move[0] for move in moves], [move[1] for move in moves], 'ro')
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    interpret_logo(sys.argv[1])
