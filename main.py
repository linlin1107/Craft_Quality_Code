```python  

import tkinter.filedialog
import tkinter.font
import a2
import MazeApp

# True if you want the maze to be printed as well as shown in the window.
PRINT_MAZE = True

# The font for the rat race.
FONT = ('Courier New', 18, 'bold')

# Up, down, left, right for player 1.
RAT_1_KEYS = {
    'w': (a2.UP, a2.NO_CHANGE),
    'a': (a2.NO_CHANGE, a2.LEFT),
    's': (a2.DOWN, a2.NO_CHANGE),
    'd': (a2.NO_CHANGE, a2.RIGHT)
}

# Up, down, left, right for player 2.
RAT_2_KEYS = {
    'i': (a2.UP, a2.NO_CHANGE),
    'j': (a2.NO_CHANGE, a2.LEFT),
    'k': (a2.DOWN, a2.NO_CHANGE),
    'l': (a2.NO_CHANGE, a2.RIGHT)
}


def read_maze(maze_file):
    """ (file open for reading) -> list of list of str

    Return the contents of maze_file in a list of list of str,
    where each character is a separate entry in the list.
    """

    res = []
    for line in maze_file:
        maze_row = [ch for ch in line.strip()]
        res.append(maze_row)

    return res

def find_rats_replace_hallway(maze_list):
    """ (list of list of str) -> (Rat, Rat) tuple

    Return the two Rats in a list.  Also modify maze_list so that the rat
    chars are replaced with HALL chars.
    """

    for r in range(len(maze_list)):
        for c in range(len(maze_list[r])):

            if maze_list[r][c] == a2.RAT_1_CHAR:
                rat_1 = a2.Rat(a2.RAT_1_CHAR, r, c)
                maze_list[r][c] = a2.HALL
            elif maze_list[r][c] == a2.RAT_2_CHAR:
                rat_2 = a2.Rat(a2.RAT_2_CHAR, r, c)
                maze_list[r][c] = a2.HALL

    return (rat_1, rat_2)


def main():
    """ Prompt for a maze file, read the maze, and start the game. """

    root = tkinter.Tk()

    maze_filename = tkinter.filedialog.askopenfilename()
    with open(maze_filename, 'r') as maze_file:
        maze_list = read_maze(maze_file)

    rat_1, rat_2 = find_rats_replace_hallway(maze_list)

    the_maze = a2.Maze(maze_list, rat_1, rat_2)
    app = MazeApp.MazeApp(root, the_maze)
    app.mainloop()
```
