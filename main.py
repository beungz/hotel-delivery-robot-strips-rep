from planner import forward_search, is_applicable, apply_action, goal_satisfied, get_applicable_actions, print_search_results
from domain_definition import actions

if __name__ == "__main__":
    # Define the initial state
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

    # Define the goal state
    goal = {
        'Delivered(Coffee,Room201)', 
        'RobotAt(Lobby)'
    }

    # Perform forward search to find a plan
    plan, explored, final_state = forward_search(initial_state, goal, actions)

    # Print the results
    print_search_results(plan, explored, final_state)