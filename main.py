from classes import State

test_state = State()

# for action in test_state.get_possible_actions():
    # print(action)

def breadth_first_search(state: State) -> State:
    explored, frontier = [], []
    while not state.is_goal_state():
        explored.append(state)
        for valid_action in state.get_valid_actions():
            next_state = state.next_state(valid_action)
            if next_state not in explored and next_state not in frontier:
                frontier.append(next_state)
        if len(frontier) == 0:
            return None
        state = frontier.pop(0)
    return state

print(breadth_first_search(test_state).state)