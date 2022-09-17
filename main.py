from classes import Person, TravelDirection, State

action = (Person.MISSIONARY, TravelDirection.TO_END)
state = State()
print(state.next_state(action).state)