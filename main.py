from classes import Person, TravelDirection, State

action = (Person.MISSIONARY, TravelDirection.TO_END)
state = State()
print(state.get_valid_actions())