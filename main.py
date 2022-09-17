import itertools
from classes import State

test_state = State()

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

end_state = breadth_first_search(test_state)
list_of_prior_actions, list_of_states = [], []
if end_state is not None:
    current_state = end_state
    while True:
        list_of_prior_actions.append(current_state.prior_action)
        list_of_states.append(current_state.state)
        current_state = current_state.parent
        if current_state is None:
            break

x = list(itertools.zip_longest(list_of_prior_actions, list_of_states))
x.reverse()
for prior_action, state in x:
    print('Prior action: ', prior_action)
    print('State: ', state)
    print('\n')