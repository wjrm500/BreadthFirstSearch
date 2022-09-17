from __future__ import annotations
import copy
import enum

class Person(enum.Enum):
    MISSIONARY = 0
    CANNIBAL = 1

class TravelDirection(enum.Enum):
    TO_END = 0
    TO_START = 1

class InvalidActionException(Exception):
    pass

class State:
    GOAL_STATE = [[0, 0], [3, 3]]

    def __init__(self, state: State = None) -> None:
        self.state = state or [[3, 3], [0, 0]]

    def is_goal_state(self) -> bool:
        return self.state == self.GOAL_STATE
    
    def next_state(self, action) -> State:
        person, travel_direction = action[0].value, action[1].value
        num_persons = self.state[travel_direction][person]
        if num_persons < 1:
            raise InvalidActionException("Not enough persons of that type on that side of the river")
        new_state = copy.copy(self.state)
        new_state[travel_direction][person] -= 1
        new_state[abs(1 - travel_direction)][person] += 1
        return State(new_state)
    
    def is_valid_state(self) -> bool:
        valid_left_side = self.state[TravelDirection.TO_END][Person.MISSIONARY] >= self.state[TravelDirection.TO_END][Person.CANNIBAL]
        valid_right_side = self.state[TravelDirection.TO_START][Person.MISSIONARY] >= self.state[TravelDirection.TO_START][Person.CANNIBAL]
        return valid_left_side and valid_right_side