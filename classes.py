from __future__ import annotations
import copy
import enum
import itertools
from typing import List

class Person(enum.Enum):
    MISSIONARY = 0
    CANNIBAL = 1

class TravelDirection(enum.Enum):
    TO_END = 0
    TO_START = 1

class State:
    GOAL_STATE = [[0, 0], [3, 3]]

    def __init__(self, state: State = None) -> None:
        self.state = state or [[3, 3], [0, 0]]
    
    def __eq__(self, state: State) -> bool:
        return self.state == state.state

    def is_goal_state(self) -> bool:
        return self.state == self.GOAL_STATE
    
    def next_state(self, action) -> State:
        first_person, second_person, river_side = action
        new_state = copy.deepcopy(self.state)
        for person in [first_person, second_person]:
            if person is not None:
                new_state[river_side.value][person.value] -= 1
                new_state[abs(river_side.value - 1)][person.value] += 1
        return State(new_state)
    
    def is_valid_state(self) -> bool:
        no_negative_counts = -1 not in itertools.chain(*self.state)
        left_missionaries = self.state[0][Person.MISSIONARY.value]
        left_cannibals = self.state[0][Person.CANNIBAL.value]
        right_missionaries = self.state[1][Person.MISSIONARY.value]
        right_cannibals = self.state[1][Person.CANNIBAL.value]
        valid_left_side = left_missionaries == 0 or left_missionaries >= left_cannibals
        valid_right_side = right_missionaries == 0 or right_missionaries >= right_cannibals
        return no_negative_counts and valid_left_side and valid_right_side
    
    def get_possible_actions(self) -> List: # Regardless of valid
        first_person_opts = [Person.MISSIONARY, Person.CANNIBAL]
        second_person_opts = [Person.MISSIONARY, Person.CANNIBAL, None]
        travel_direction_opts = [TravelDirection.TO_START, TravelDirection.TO_END]
        return list(itertools.product(first_person_opts, second_person_opts, travel_direction_opts))
    
    def get_valid_actions(self) -> List:
        return [action for action in self.get_possible_actions() if self.next_state(action).is_valid_state()]