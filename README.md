# Cell Sim
## About
Cell Sim is the final project for my SWiFT camp 2023. The final project was to create a program using what we learned. I have a lot of experience, so I decided to make a complex program. It is a simple physics simulation using cellular automata to represent items. It uses pygame and the random library. My original version worked in the terminal, although I switched to pygame around an hour in.
## Cell Construction
The cell creation format is quite powerful, and can be used to make many different cells, each with unique properties The original version only had one rule that you could make, which was to make the cell move. Nothing else. The second version added the ability to change to another cell, along with removing the cell. The final, current version added states, which would be selected based on what has happened during a step of simulation. It allows for an alternative set of rules, depending on what happened last turn.  
To create a cell, it is quite easy. To start, choose the features from the first and second versions, as they are the easiest to add.
```
1 2 3
4 5 6
7 8 9
```
> Cell creation grid  
> This has been a useful tool in development, as it shows what to make the normal rule to get the type of cell you want. 
### Step 1
The cell starts at `5`, and goes to whichever number the step dictates relative to it. It is recommended to only use the number 5 as a dampener for other possibilities, as it will have a negative effect on the performance.  
Here's an example rule, for water: `8>79>46`. The arrows separate steps, where the first step is in the first segment, and the second in the second segment. For each step, a number is chosen randomly, and all options will be tried in that step before the program goes to the next step.
### Step 2
States are added in the following format: `"previous": "rule"`, where "previous" is whatever the cell previously did, and "rule" is the rule for when it is in this state. An important feature in the "previous" section is that if you do `.>something` or `something>.`, where something is another cell type, it will detect if it tried to move to some cell. An important feature in the "rule" section is the `/` character, which will reset the cell to its default state.
Here is the example states section for water: 
```json
"states": {
    "7": "8>7>4/",
    "4": "8>7>4/",
    "9": "8>9>6/",
    "6": "8>9>6/",
    "f>.": "a"
}
```
### Step 3
Overrides are additional features that didn't fit into other categories. They were added in v1.4.0, and there are 3 different types: `"destroy"`, `"swap"`, and `"push"`. Destroy removes the cell that the current cell is going into, swap switches the current cell and the other cell, and push first tries to push the cell in the same direction as the current cell, but if it can't, it switches to swap.  
Overrides are on a cell by cell basis, so the overrides section is another dict. Below is the overrides for the earth cell, meaning that water is replaced with it.
```json
"overrides": {
    "w": "swap"
}
```
### Step 4
After this, your cell is mostly done. You just have to format it. For example, here is the water cell, in its entirety:
```json
"w": {
    "color": "blue",
    "name": "Water",
    "rule": "8>79>46",
    "states": {
        "7": "8>7>4/",
        "4": "8>7>4/",
        "9": "8>9>6/",
        "6": "8>9>6/",
        "f>.": "a"
    },
    "overrides": {}
}
```
#### Breakdown
The character "w" is the identifier for the cell. Make sure it isn't a duplicate of any other cell. It can be multiple characters, but as of now that will stop other cells from turning into it.  
The item "color" is the color of the cell, which can either be a valid pygame color string or an RGB / RGBA tuple. A tuple in this example would be `(0,0,255)`.  
The item "name" is unused as of now, but is recommended to have for development purposes.  
The item "rule" is the rule, from stage 1 of the cell creation.  
The item "states" is the dictionary of states, from part 2.  
#### Addition
To add your cell to the game, add it to `cells.json`. Your cell will now be added to the game.