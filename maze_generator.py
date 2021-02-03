import enum
import random


class HowToFill(enum.Enum):
    OPEN = 1
    CLOSE = 2
    RANDOM = 3


def maze_generator(size=5, howToFill=HowToFill.RANDOM):
    maze = ''
    probably = 5  # in 10

    for i in range(2*size + 1):
        for j in range(2*size + 1):
            if i % 2 == 0:
                if j % 2 == 0:
                    maze += '+'
                else:
                    random_number = random.randint(1, 10)
                    maze += '-' if (i in [0, 2*size]
                                        ) or (howToFill == HowToFill.CLOSE
                                        ) or (random_number < probably and howToFill == HowToFill.RANDOM
                                        ) else ' '
            else:
                if j % 2 == 0:
                    random_number = random.randint(1, 10)
                    maze += '|' if (j in [0, 2*size]
                                        ) or (howToFill == HowToFill.CLOSE
                                        ) or (random_number < probably and howToFill == HowToFill.RANDOM
                                        ) else ' '
                else:
                    maze += '.'
        maze += '\n'

    return maze



def print_maze(maze):
    with open("maze.txt", "w") as maze_problem_file:
        maze_problem_file.write(maze)



def main():
    maze = maze_generator(size=9, howToFill=HowToFill.RANDOM)  # Generate maze string
    print_maze(maze)  # write maze string in maze.txt


if __name__ == '__main__':
    main()
