# AIPI 590: Intelligent Agents: Hotel Delivery Robot Pathfinder
### **Author**: Matana Pornluanprasert

This hotel delivery robot pathfinder application aims to find the optimal path for a hotel delivery robot to deliver items to guest rooms in a hotel, using forward search algorithm with defined actions, initial state, and goal state, with the STRIPS representation.<br>

***
# Domain Description

**Objects in the domain:**<br>
- Items: Coffee, Water<br>
- Locations: Lobby, Elevator_F1, Elevator_F2, Kitchen, Hallway_F1, Hallway_F2, Room101, Room102, Room201, Room202<br>
- Elevator floors: F1, F2<br>

**What the robot is trying to achieve:**<br>

Deliver specified items to specified rooms by picking up items from the kitchen or the lobby, moving through the hotel, using the elevator when necessary, and dropping off items at the guest rooms.<br>


**Why planning is needed:**<br>
The hotel environment is dynamic and complex, with multiple locations, items, and constraints. The robot needs to plan its actions to efficiently navigate the hotel, pick up items, and deliver them to the correct rooms.<br>
<br>

***
# STRIPS Formalization: State Description

| Fluent | Description |
|------|------------|
| RobotAt(`location_name`) | The robot is at location `location_name` |
| ItemAt(`item_name`, `location_name`) | The item `item_name` is at location `location_name` |
| Connected(`location_name_1`, `location_name_2`) | Location `location_name_1` is connected to location `location_name_2` |
| ContainerEmpty | The robot has an empty container (no item inside) |
| Carrying(`item_name`) | The robot is carrying the item `item_name` |
| Delivered(`item_name`, `location_name`) | The item `item_name` has been delivered to location `location_name` |
| ElevatorAt(`floor_no`) | The elevator is at floor `floor_no` |
| InElevator | The robot is inside the elevator |
| ElevatorEmpty | The elevator is empty (no robot inside) |
| DoorClosed(`location_name`) | The door at guest room `location_name` is closed |
| Waiting(`location_name`) | The robot is waiting for the hotel guest to open the door at `location_name` |
| DoorOpen(`location_name`) | The door at guest room `location_name` is open |

<br>


***
# STRIPS Formalization: Action Schema

### Action: Move(from,to)
**Preconditions**
- RobotAt(from)
- Connected(from,to)

**Add Effects**
- RobotAt(to)

**Delete Effects**
- RobotAt(from)
***

### Action: PickUp(item,location)
**Preconditions**   
- RobotAt(location)
- ItemAt(item,location)
- ContainerEmpty

**Add Effects**
- Carrying(item)

**Delete Effects**
- ContainerEmpty
- ItemAt(item,location)
***

### Action: EnterElevator(floor)
**Preconditions**
- RobotAt(Elevator_F1) or RobotAt(Elevator_F2)
- ElevatorAt(floor)
- ElevatorEmpty

**Add Effects**
- InElevator

**Delete Effects**
- RobotAt(Elevator_F1) or RobotAt(Elevator_F2)
- ElevatorEmpty
***

### Action: GoToFloor(from_floor,to_floor)
**Preconditions**
- InElevator
- ElevatorAt(from_floor)

**Add Effects**
- ElevatorAt(to_floor)

**Delete Effects**
- ElevatorAt(from_floor)
***

### Action: ExitElevator(floor)
**Preconditions**   
- InElevator
- ElevatorAt(floor)

**Add Effects**
- RobotAt(Elevator_F1) or RobotAt(Elevator_F2)
- ElevatorEmpty

**Delete Effects**
- InElevator
***

### Action: WaitingForGuest(location)
**Preconditions**   
- RobotAt(location)
- DoorClosed(location)

**Add Effects**
- Waiting(location)

**Delete Effects**
- (none)
***

### Action: GuestOpensDoor(location)
**Preconditions**
- RobotAt(location)
- DoorClosed(location)
- Waiting(location)

**Add Effects**
- DoorOpen(location)

**Delete Effects**
- DoorClosed(location)
- Waiting(location)
***

### Action: HandOverItem(item,location)
**Preconditions**
- RobotAt(location)
- DoorOpen(location)
- Carrying(item)

**Add Effects**
- Delivered(item,location)
- ItemAt(item,location)
- ContainerEmpty

**Delete Effects**
- Carrying(item)
- DoorOpen(location)
***
<br>

# Example Problem Instance:

With the defined actions above, here is an example problem instance with the initial state and goal state.
```
# The initial state
initial_state = {
    'RobotAt(Lobby)',
    'ItemAt(Coffee,Kitchen)',
    'ItemAt(Water,Lobby)',
    'ContainerEmpty',
    'ElevatorEmpty',
    'ElevatorAt(F1)',
    'Connected(Lobby,Kitchen)',
    'Connected(Lobby,Elevator_F1)',
    'Connected(Lobby,Hallway_F1)',
    'Connected(Hallway_F1,Room101)',
    'Connected(Hallway_F1,Room102)',  
    'Connected(Hallway_F2,Elevator_F2)',
    'Connected(Hallway_F2,Room201)',
    'Connected(Hallway_F2,Room202)' 
}

# The goal state
goal = {
    'Delivered(Coffee,Room201)', 
    'RobotAt(Lobby)'
}
```

Based on the above definitions, the following code performs a forward search to find a plan for the robot to achieve the goal state from the initial state.
```
# Perform forward search to find a plan
plan, explored, final_state = forward_search(initial_state, goal, actions)

# Print the results
print_search_results(plan, explored, final_state)
```

Here is the resulting plan found by the forward search algorithm:
```
FORWARD SEARCH RESULT
------------------------------------------------------------
Plan found (18 steps):

  01. Move(Lobby,Kitchen)
  02. PickUp(Coffee,Kitchen)
  03. Move(Kitchen,Lobby)
  04. Move(Lobby,Elevator_F1)
  05. EnterElevator(F1)
  06. GoToFloor(F2)
  07. ExitElevator(F2)
  08. Move(Elevator_F2,Hallway_F2)
  09. Move(Hallway_F2,Room201)
  10. WaitingForGuest(Room201)
  11. GuestOpensDoor(Room201)
  12. HandOverItem(Coffee,Room201)
  13. Move(Room201,Hallway_F2)
  14. Move(Hallway_F2,Elevator_F2)
  15. EnterElevator(F2)
  16. GoToFloor(F1)
  17. ExitElevator(F1)
  18. Move(Elevator_F1,Lobby)

------------------------------------------------------------
States explored: 5074
------------------------------------------------------------
Final State:
  - Connected(Hallway_F1,Room101)
  - Connected(Hallway_F1,Room102)
  - Connected(Hallway_F2,Elevator_F2)
  - Connected(Hallway_F2,Room201)
  - Connected(Hallway_F2,Room202)
  - Connected(Lobby,Elevator_F1)
  - Connected(Lobby,Hallway_F1)
  - Connected(Lobby,Kitchen)
  - ContainerEmpty
  - Delivered(Coffee,Room201)
  - ElevatorAt(F1)
  - ElevatorEmpty
  - ItemAt(Coffee,Room201)
  - ItemAt(Water,Lobby)
  - RobotAt(Lobby)
```


### How to run the example problem instance
***
Type the followings in the terminal<br>

On Windows:<br>

```
py main.py
```

On other systems:<br>

```
python main.py
```

<br>