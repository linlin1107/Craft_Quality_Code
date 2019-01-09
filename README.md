# Craft Quality Code  

* ### __final assignment:__ files in this repository
   * a2 - rat and maze
   * mazeapp - GUI and link to a2
   * main() - initialize the whole application
* ### __thought process:__ 
## <span style="color:green">RatRace</span>
### <span style="color:purple">logics: </span>
- three entities: rat (track location and eat sprout); maze (symobls, rules for symbols, rules of move, link rat location to maze)  
- decouple rat from maze as if rat floats above maze  


### <span style="color:purple">Classes invovled</span>  
__Rat__  
- constant: symbols to represent rat  
```python  
RAT_1_CHAR = 'J'
```  
- __initialize__ with vertical location (int), horizontal location (int), number of sprouts eatern (int)
- set rat's location  
```python 
set_location(rat,int,int)  
```  
- add one to num_sprouts_eaten 
```python 
eat_sprout(rat) 
```
- string for the RAT :  
-- rat symbol at(row,col) ate num_sprouts_eaten sprouts.    



__Maze__  
- string for different symbols, e.g.  
```python  
WALL = '#'
```  
- __initialize__ with maze (string of string), vertical move (int), horiontal move (int), total number of sprout left (int) 
- rules for movement: 
```python  
move(Maze,Rat,int,int)
```  
-- move by horizontal or vertical 1 step at a time, e.g. (1,0) for up one step
-- get character for the next move  
method defined seperatly in the class for calling  
```python  
get_character(Maze,int,int)
```  
-- define the rules for eating sprout  
let rat eat sprout:  
```python 
rat.num_sprouts_eaten +=1
```
replace sprouts with hallway: change the symboles in the input string of strings  
```python 
res[i][j]= hallway
```
Decrease number of sprout left by 1: 
```python 
num_sprouts_left -=1
```
-- set rat location  
change the value 
```python 
rat.set_location()  
```

__Maze(App) -> GUI__  
- setup the frame  

- Link key stroke with rat move and rat score: method rat_1_keystroke(self, event)  
-- call method move() in class maze  
-- update rat_1_score_var from maze.rat_1.num_sprouts_eaten  
-- call method redraw() in class mazeapp()  

- make labels for each symbol and display: call method get_character() in class Maze  

- display scores: based on rat_1_score_var
  


### <span style="color:purple">main() to implement  </span>
- call for reader inputs for maze: with open() as: 
- convert reader inputs to list of list of strings: read_maze()  
- call method find_rats_replace_hallway() to create two instants of rats:
-- only once to process user inputs: decouple rat from the maze_list (replace rat symbols with hallway)  
-- user mazelist and class rat()
- create one instance of class Maze   
```python 
the_maze = a2.Maze(maze_list, rat_1, rat_2)
```
-- rat_1 and rat_2 from method find_rats_replace_hallway() 
-- create instance for mazeapp (implement GUI)
```python 
app = MazeApp(root, the_maze)
```
-- run GUI 
```python 
app.mainloop()
```
