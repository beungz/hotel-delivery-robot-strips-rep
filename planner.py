def is_applicable(state, action):
    """
    Check if action's preconditions are satisfied.
    """
    # Return True if ALL preconditions are in state
    return action['preconditions'].issubset(state)



def apply_action(state, action):
    """
    Apply action to get new state.
    """
    # Return (state - delete_list) | add_list
    return (state - action['delete_list']) | action['add_list']



def goal_satisfied(state, goal):
    """
    Check if the goal is satisfied in the current state.
    
    Args:
        state: Current state (set of fluents)
        goal: Set of fluents that must ALL be true
    
    Returns:
        bool: True if all goal fluents are in state
    """
    # Check if ALL goal facts are in the state
    return goal.issubset(state)


def get_applicable_actions(state, actions):
    """
    Get all actions that can be applied in the current state.
    
    Args:
        state: Current state (set of fluents)
        actions: List of all action dictionaries
    
    Returns:
        list: Actions whose preconditions are satisfied
    """
    # Return list of applicable actions
    applicable_action = []
    
    for action in actions:
        if is_applicable(state, action):
            applicable_action.append(action)

    return applicable_action
            


def forward_search(initial_state, goal, actions):
    """
    Find a plan using BFS forward search.
    
    Args:
        initial_state: Starting state (set of fluents)
        goal: Goal condition (set of fluents that must be true)
        actions: List of all possible action dictionaries
    
    Returns:
        tuple: (plan, explored_count)
               - plan: List of action names, or None if no plan exists
               - explored_count: Number of states explored
               - final state: The state when the goal is reached
    
    Algorithm:
        1. Initialize queue with (initial_state, empty_plan)
        2. Initialize visited set with initial_state
        3. While queue not empty:
           a. Dequeue (current_state, current_plan)
           b. If goal satisfied: return plan
           c. For each applicable action:
              - Compute successor state
              - If not visited: add to queue and visited
        4. Return None (no plan found)
    """
    explored = 0
    
    # Initialize the queue with (initial_state, [])
    # queue holds tuples of (state, list_of_action_names_so_far)
    queue = []
    queue.append((initial_state, []))
    
    # Track visited states (using frozenset since regular sets aren't hashable)
    visited = {frozenset(initial_state)}
    
    # Implement BFS
    # While queue is not empty:
    #   1. Dequeue the first item: state, plan = queue.pop(0)
    #   2. Increment explored counter
    #   3. Check if goal is satisfied - if so, return (plan, explored)
    #   4. Get all applicable actions using get_applicable_actions()
    #   5. For each applicable action:
    #      - Apply it to get the new state using apply_action()
    #      - If frozenset(new_state) not in visited:
    #        - Add frozenset(new_state) to visited
    #        - Enqueue (new_state, plan + [action['name']])
    
    while queue:
        currentstate, currentplan = queue.pop(0)
        explored += 1
        if goal_satisfied(currentstate, goal):
            return currentplan, explored, currentstate

        applicable_actions = get_applicable_actions(currentstate, actions)
        for action in applicable_actions:
            new_state = apply_action(currentstate, action)
            if frozenset(new_state) not in visited:
                visited.add(frozenset(new_state))
                queue.append((new_state, currentplan + [action['name']]))
                
    
    return None, explored, None  # No plan found



def print_search_results(plan, explored, final_state):
    print("FORWARD SEARCH RESULT")
    print("-" * 60)

    if plan is None:
        print("No plan found.")
    else:
        print(f"Plan found ({len(plan)} steps):\n")
        for i, action in enumerate(plan, start=1):
            print(f"  {i:02d}. {action}")

    print("\n" + "-" * 60)
    print(f"States explored: {explored}")

    if final_state is not None:
        print("-" * 60)
        print("Final State:")
        for fluent in sorted(final_state):
            print(f"  - {fluent}")