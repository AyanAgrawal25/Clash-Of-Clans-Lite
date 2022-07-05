# **Clash of Clans Lite**

### **To start the game :**

1. `cd` into the directory.
2. Run command `python3 game.py`.
3. Select your hero (Archer Queen or Barbarian King).

### **To watch the replay :**

1. Check the numbering of the replay file you want to watch, in the "replays" directory.
2. Run command `python3 replay.py file_name`.

### **Commands used in the game :**

1. King and Queen moves up/left/down/right with `w`, `a`, `s`, `d` respectively.
2. King and Queen attacks with `spacebar`.
3. Barbarians are spawned at 3 different locations shown by `b`,`n`,`m` on the map with same buttons.
4. Archers are spawned at 3 different locations shown by `x`,`c`,`v` on the map with same buttons.
5. Balloons are spawned at 3 different locations shown by `y`,`u`,`i` on the map with same buttons.
6. Heal spell can be applied on the troops and King using `h`.
7. Rage spell can be applied on the troops and King using `r`.
8. If you want to quit the game in between play, press `q`.
9. Similarly, if you want to quit the replay, press `q`.
10. King uses axe with `o`.
11. Queen uses Eagle arrow (bonus) with `o`.

### **Other features :**

1. The health bar shows King's/Queen's life.
2. Barbarians, Archers and Loons left in the game are shown below the map.
3. Cannons and Wizard towers emit sound when they fire.
4. You need to win one level to move to the next level. (3 levels are present)
5. Limits are set at each level on amount of spawning troops.

### **Assumptions taken other than the ones mentioned in the PDF :**

1. Range of the cannon is measured from the cannon's `top-left` co-ordinate.
2. The King's and Queen's health is `200`.
3. Barbarian's health is `100`.
4. Archer's health is `50`.
5. Balloon's health is `100`.
6. The King's speed is `1`.
7. The King's attack power is `30`.
8. The Queen's speed is `1`.
9. The Queen's attack power is `22.5`.
10. Barbarian's attack power is `20`.
11. Archer's attack power is `10`.
12. Balloon's attack power is `40`.
13. The cannon's damage is `25`.
14. The Wizard Tower's damage is `25`.
15. The cannon's, wiz tower's and hut's health is `100`.
16. The Town hall's health is `200`.

## **OOPS concepts exhibited in the game :**

1. **Inheritance** : 
    Cannon and Wizard Tower is the child class of Buildings.
2. **Polymorphism** :
    Barbarians and King have the method rage() and heal().
    Buildings and King class have render() method.
3. **Encapsulation** : 
    Have used class and object oriented programming concepts in the game.
4. **Abstraction** :
    Class Barbarian, Archer and Loons have method rage() , move() , heal().
