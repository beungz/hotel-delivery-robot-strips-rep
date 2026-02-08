actions = [
    # PickUp actions
    {'name': 'PickUp(Coffee,Kitchen)', 
        'preconditions': {'ItemAt(Coffee,Kitchen)', 'RobotAt(Kitchen)', 'ContainerEmpty'}, 
        'add_list': {'Carrying(Coffee)'}, 
        'delete_list': {'ContainerEmpty', 'ItemAt(Coffee,Kitchen)'} 
    },
    {'name': 'PickUp(Water,Kitchen)', 
        'preconditions': {'ItemAt(Water,Kitchen)', 'RobotAt(Kitchen)', 'ContainerEmpty'}, 
        'add_list': {'Carrying(Water)'}, 
        'delete_list': {'ContainerEmpty', 'ItemAt(Water,Kitchen)'} 
    },
    {'name': 'PickUp(Coffee,Lobby)', 
        'preconditions': {'ItemAt(Coffee,Lobby)', 'RobotAt(Lobby)', 'ContainerEmpty'}, 
        'add_list': {'Carrying(Coffee)'}, 
        'delete_list': {'ContainerEmpty', 'ItemAt(Coffee,Lobby)'} 
    },
    {'name': 'PickUp(Water,Lobby)', 
        'preconditions': {'ItemAt(Water,Lobby)', 'RobotAt(Lobby)', 'ContainerEmpty'}, 
        'add_list': {'Carrying(Water)'},    
        'delete_list': {'ContainerEmpty', 'ItemAt(Water,Lobby)'} 
    },

    # Move actions
    {'name': 'Move(Lobby,Kitchen)', 
        'preconditions': {'RobotAt(Lobby)', 'Connected(Lobby,Kitchen)'}, 
        'add_list': {'RobotAt(Kitchen)'}, 
        'delete_list': {'RobotAt(Lobby)'} 
    },
    {'name': 'Move(Kitchen,Lobby)', 
        'preconditions': {'RobotAt(Kitchen)', 'Connected(Lobby,Kitchen)'}, 
        'add_list': {'RobotAt(Lobby)'}, 
        'delete_list': {'RobotAt(Kitchen)'} 
    },
    {'name': 'Move(Lobby,Hallway_F1)', 
        'preconditions': {'RobotAt(Lobby)', 'Connected(Lobby,Hallway_F1)'}, 
        'add_list': {'RobotAt(Hallway_F1)'}, 
        'delete_list': {'RobotAt(Lobby)'} 
    },
    {'name': 'Move(Hallway_F1,Lobby)', 
        'preconditions': {'RobotAt(Hallway_F1)', 'Connected(Lobby,Hallway_F1)'}, 
        'add_list': {'RobotAt(Lobby)'}, 
        'delete_list': {'RobotAt(Hallway_F1)'} 
    },  
    {'name': 'Move(Hallway_F1,Room101)', 
        'preconditions': {'RobotAt(Hallway_F1)', 'Connected(Hallway_F1,Room101)'}, 
        'add_list': {'RobotAt(Room101)', 'DoorClosed(Room101)'},   
        'delete_list': {'RobotAt(Hallway_F1)'}
    },
    {'name': 'Move(Room101,Hallway_F1)', 
        'preconditions': {'RobotAt(Room101)', 'Connected(Hallway_F1,Room101)'}, 
        'add_list': {'RobotAt(Hallway_F1)'},   
        'delete_list': {'RobotAt(Room101)'}
    },
    {'name': 'Move(Hallway_F1,Room102)', 
        'preconditions': {'RobotAt(Hallway_F1)', 'Connected(Hallway_F1,Room102)'}, 
        'add_list': {'RobotAt(Room102)', 'DoorClosed(Room102)'},   
        'delete_list': {'RobotAt(Hallway_F1)'}
    },
    {'name': 'Move(Room102,Hallway_F1)', 
        'preconditions': {'RobotAt(Room102)', 'Connected(Hallway_F1,Room102)'}, 
        'add_list': {'RobotAt(Hallway_F1)'},   
        'delete_list': {'RobotAt(Room102)'}
    },
    {'name': 'Move(Lobby,Elevator_F1)', 
        'preconditions': {'RobotAt(Lobby)', 'Connected(Lobby,Elevator_F1)'}, 
        'add_list': {'RobotAt(Elevator_F1)'}, 
        'delete_list': {'RobotAt(Lobby)'}
    },
    {'name': 'Move(Elevator_F1,Lobby)', 
        'preconditions': {'RobotAt(Elevator_F1)', 'Connected(Lobby,Elevator_F1)'}, 
        'add_list': {'RobotAt(Lobby)'}, 
        'delete_list': {'RobotAt(Elevator_F1)'}
    },
    {'name': 'Move(Hallway_F2,Room201)', 
        'preconditions': {'RobotAt(Hallway_F2)', 'Connected(Hallway_F2,Room201)'}, 
        'add_list': {'RobotAt(Room201)', 'DoorClosed(Room201)'}, 
        'delete_list': {'RobotAt(Hallway_F2)'}
    },
    {'name': 'Move(Room201,Hallway_F2)', 
        'preconditions': {'RobotAt(Room201)', 'Connected(Hallway_F2,Room201)'}, 
        'add_list': {'RobotAt(Hallway_F2)'}, 
        'delete_list': {'RobotAt(Room201)'}
    },
    {'name': 'Move(Hallway_F2,Room202)', 
        'preconditions': {'RobotAt(Hallway_F2)', 'Connected(Hallway_F2,Room202)'}, 
        'add_list': {'RobotAt(Room202)', 'DoorClosed(Room202)'}, 
        'delete_list': {'RobotAt(Hallway_F2)'}
    },
    {'name': 'Move(Room202,Hallway_F2)', 
        'preconditions': {'RobotAt(Room202)', 'Connected(Hallway_F2,Room202)'}, 
        'add_list': {'RobotAt(Hallway_F2)'}, 
        'delete_list': {'RobotAt(Room202)'}
    },
    {'name': 'Move(Elevator_F2,Hallway_F2)', 
        'preconditions': {'RobotAt(Elevator_F2)', 'Connected(Hallway_F2,Elevator_F2)'}, 
        'add_list': {'RobotAt(Hallway_F2)'}, 
        'delete_list': {'RobotAt(Elevator_F2)'}
    },
    {'name': 'Move(Hallway_F2,Elevator_F2)', 
        'preconditions': {'RobotAt(Hallway_F2)', 'Connected(Hallway_F2,Elevator_F2)'}, 
        'add_list': {'RobotAt(Elevator_F2)'}, 
        'delete_list': {'RobotAt(Hallway_F2)'}
    },

    # Elevator actions
    {'name': 'EnterElevator(F1)', 
        'preconditions': {'RobotAt(Elevator_F1)', 'ElevatorAt(F1)', 'ElevatorEmpty'}, 
        'add_list': {'InElevator'}, 
        'delete_list': {'RobotAt(Elevator_F1)', 'ElevatorEmpty'}
    },
    {'name': 'EnterElevator(F2)', 
        'preconditions': {'RobotAt(Elevator_F2)', 'ElevatorAt(F2)', 'ElevatorEmpty'}, 
        'add_list': {'InElevator'}, 
        'delete_list': {'RobotAt(Elevator_F2)', 'ElevatorEmpty'}
    },
    {'name': 'ExitElevator(F1)', 
        'preconditions': {'InElevator', 'ElevatorAt(F1)'}, 
        'add_list': {'RobotAt(Elevator_F1)', 'ElevatorEmpty'}, 
        'delete_list': {'InElevator'}
    },
    {'name': 'ExitElevator(F2)', 
        'preconditions': {'InElevator', 'ElevatorAt(F2)'}, 
        'add_list': {'RobotAt(Elevator_F2)', 'ElevatorEmpty'}, 
        'delete_list': {'InElevator'}
    },
    {'name': 'GoToFloor(F2)', 
        'preconditions': {'InElevator', 'ElevatorAt(F1)'}, 
        'add_list': {'ElevatorAt(F2)'}, 
        'delete_list': {'ElevatorAt(F1)'}
    },
    {'name': 'GoToFloor(F1)', 
        'preconditions': {'InElevator', 'ElevatorAt(F2)'}, 
        'add_list': {'ElevatorAt(F1)'}, 
        'delete_list': {'ElevatorAt(F2)'}
    },

    # Delivery actions
    {'name': 'WaitingForGuest(Room101)', 
        'preconditions': {'RobotAt(Room101)', 'DoorClosed(Room101)'}, 
        'add_list': {'Waiting(Room101)'}, 
        'delete_list': set()
    },
    {'name': 'WaitingForGuest(Room102)', 
        'preconditions': {'RobotAt(Room102)', 'DoorClosed(Room102)'},
        'add_list': {'Waiting(Room102)'}, 
        'delete_list': set()
    },
    {'name': 'WaitingForGuest(Room201)', 
        'preconditions': {'RobotAt(Room201)', 'DoorClosed(Room201)'}, 
        'add_list': {'Waiting(Room201)'}, 
        'delete_list': set()
    },
    {'name': 'WaitingForGuest(Room202)', 
        'preconditions': {'RobotAt(Room202)', 'DoorClosed(Room202)'}, 
        'add_list': {'Waiting(Room202)'}, 
        'delete_list': set()
    },
    {'name': 'GuestOpensDoor(Room101)', 
        'preconditions': {'RobotAt(Room101)', 'DoorClosed(Room101)', 'Waiting(Room101)'}, 
        'add_list': {'DoorOpen(Room101)'},
        'delete_list': {'DoorClosed(Room101)', 'Waiting(Room101)'}
    },
    {'name': 'GuestOpensDoor(Room102)', 
        'preconditions': {'RobotAt(Room102)', 'DoorClosed(Room102)', 'Waiting(Room102)'}, 
        'add_list': {'DoorOpen(Room102)'},
        'delete_list': {'DoorClosed(Room102)', 'Waiting(Room102)'}
    },
    {'name': 'GuestOpensDoor(Room201)', 
        'preconditions': {'RobotAt(Room201)', 'DoorClosed(Room201)', 'Waiting(Room201)'}, 
        'add_list': {'DoorOpen(Room201)'}, 
        'delete_list': {'DoorClosed(Room201)', 'Waiting(Room201)'}
    },
    {'name': 'HandOverItem(Coffee,Room101)', 
        'preconditions': {'Carrying(Coffee)',  'RobotAt(Room101)', 'DoorOpen(Room101)'}, 
        'add_list': {'Delivered(Coffee,Room101)', 'ContainerEmpty', 'ItemAt(Coffee,Room101)'}, 
        'delete_list': {'Carrying(Coffee)', 'DoorOpen(Room101)'}
    },
    {'name': 'HandOverItem(Coffee,Room102)', 
        'preconditions': {'Carrying(Coffee)',  'RobotAt(Room102)', 'DoorOpen(Room102)'}, 
        'add_list': {'Delivered(Coffee,Room102)', 'ContainerEmpty', 'ItemAt(Coffee,Room102)'}, 
        'delete_list': {'Carrying(Coffee)', 'DoorOpen(Room102)'}
    },
    {'name': 'HandOverItem(Coffee,Room201)', 
        'preconditions': {'Carrying(Coffee)',  'RobotAt(Room201)', 'DoorOpen(Room201)'}, 
        'add_list': {'Delivered(Coffee,Room201)', 'ContainerEmpty', 'ItemAt(Coffee,Room201)'}, 
        'delete_list': {'Carrying(Coffee)', 'DoorOpen(Room201)'}
    },
    {'name': 'HandOverItem(Coffee,Room202)', 
        'preconditions': {'Carrying(Coffee)',  'RobotAt(Room202)', 'DoorOpen(Room202)'}, 
        'add_list': {'Delivered(Coffee,Room202)', 'ContainerEmpty', 'ItemAt(Coffee,Room202)'}, 
        'delete_list': {'Carrying(Coffee)', 'DoorOpen(Room202)'}
    },
    {'name': 'HandOverItem(Water,Room101)', 
        'preconditions': {'Carrying(Water)',  'RobotAt(Room101)', 'DoorOpen(Room101)'}, 
        'add_list': {'Delivered(Water,Room101)', 'ContainerEmpty', 'ItemAt(Water,Room101)'}, 
        'delete_list': {'Carrying(Water)', 'DoorOpen(Room101)'}
    },
    {'name': 'HandOverItem(Water,Room102)', 
        'preconditions': {'Carrying(Water)',  'RobotAt(Room102)', 'DoorOpen(Room102)'}, 
        'add_list': {'Delivered(Water,Room102)', 'ContainerEmpty', 'ItemAt(Water,Room102)'}, 
        'delete_list': {'Carrying(Water)', 'DoorOpen(Room102)'}
    },
    {'name': 'HandOverItem(Water,Room201)', 
        'preconditions': {'Carrying(Water)',  'RobotAt(Room201)', 'DoorOpen(Room201)'}, 
        'add_list': {'Delivered(Water,Room201)', 'ContainerEmpty', 'ItemAt(Water,Room201)'}, 
        'delete_list': {'Carrying(Water)', 'DoorOpen(Room201)'}
    },
    {'name': 'HandOverItem(Water,Room202)', 
        'preconditions': {'Carrying(Water)',  'RobotAt(Room202)', 'DoorOpen(Room202)'}, 
        'add_list': {'Delivered(Water,Room202)', 'ContainerEmpty', 'ItemAt(Water,Room202)'}, 
        'delete_list': {'Carrying(Water)', 'DoorOpen(Room202)'}
    }]