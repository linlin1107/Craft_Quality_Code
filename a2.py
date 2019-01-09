``` python  
# coding: utf-8

# In[1]:


# Do not import any modules. If you do, the tester may reject your submission.

# Constants for the contents of the maze.

# The visual representation of a wall.
WALL = '#'

# The visual representation of a hallway.
HALL = '.'

# The visual representation of a brussels sprout.
SPROUT = '@'

# Constants for the directions. Use these to make Rats move.

# The left direction.
LEFT = -1

# The right direction.
RIGHT = 1

# No change in direction.
NO_CHANGE = 0

# The up direction.
UP = -1

# The down direction.
DOWN = 1

# The letters for rat_1 and rat_2 in the maze.
RAT_1_CHAR = 'J'
RAT_2_CHAR = 'P'


class Rat:
    def __init__ (self,symbol,row,col):
        ''' (strin,int,int) -> NoneType
        initialize with rat locations
        number of sprouts eaten by the rat
        '''
        self.symbol=symbol
        self.row=row
        self.col=col
        self.num_sprouts_eaten=0
    def set_location (self,nexti,nextj):
        ''' (int,int) -> NoneType
        set rat's location; will be used to set location in rat move
        '''
        self.row=nexti
        self.col=nextj
    def eat_sprout(self):
        ''' (self) -> NoneType
        count number of sprout eatern for the rat. 
        A rat can only eat one sprout at a time!
        '''
        self.num_sprouts_eaten+=1
    def __str__ (self):
        ''' (rat) -> str
        reture a string with rat's location and number of sprout eaten
        >>> rat.__string__()
        J at (4,3) ate 2 sprouts.’
        '''
        return '{0} at ({1},{2}) ate {3} sprouts.'.format(self.symbol,self.row,self.col,self.num_sprouts_eaten)

class Maze:
    """ A 2D maze. """
    def __init__(self,maze,rat_1,rat_2):
        '''  (list of list of strings, instance 1 of class rat, instance 2 of class rat) -> NoneTrpe
         convert maze list to maze (enforce maze rules); 
         creact interaction between maze and rat
         record total number of sprouts left
        '''
        self.maze=maze
        self.rat_1=rat_1
        self.rat_2=rat_2
        self.num_sprouts_left=0
        for i in range(len(self.maze)):
            for j in range(len(self.maze[i])):
                if self.maze[i][j] == SPROUT:
                    self.num_sprouts_left+=1                 
    def is_wall(self,h,v):
        '''()->boolean
        return true if the symbol is wall
        '''
        return self.maze[h][v]==WALL
    def get_character(self,grow,gcol):
        '''(maze,int,int)->string
        create a method to fetch symboles from maze
        if the rat is on a hallway location,return a rat..not hallway
        '''
        if grow==self.rat_1.row and gcol==self.rat_1.col: 
            return self.rat_1.symbol
        elif grow==self.rat_2.row and gcol==self.rat_2.col:
            return self.rat_2.symbol
        else:
            return self.maze[grow][gcol]
    def move(self,rat,imove,jmove):
        '''(instance of class rat,int,int)->NoneType
        get_character for next move
        action the maze rules based on character
        update sprouts for each rat
        update total sprouts left
        '''
        char=self.get_character(rat.row+imove,rat.col+jmove)
        if self.is_wall(rat.row+imove,rat.col+jmove):
            rat.set_location(rat.row,rat.col)
        elif char==SPROUT:
            rat.eat_sprout()
            self.num_sprouts_left-=1
            self.maze[rat.row+imove][rat.col+jmove]=HALL
            rat.set_location(rat.row+imove,rat.col+jmove)
            return char!=WALL
        elif char==HALL or char==self.rat_1.symbol or char==self.rat_2.symbol:
            rat.set_location(rat.row+imove,rat.col+jmove) 
            return char!=WALL
    def __str__(self):
        '''(self)->string
        return a string representation of the maze       
        '''
        self.maze_string=[]
        for row in range(len(self.maze)):
            for column in range(len(self.maze[row])):
                self.maze_string.append(self.get_character(row,column))
        return 'maze string is {0}'.format(self.maze_string)
```
