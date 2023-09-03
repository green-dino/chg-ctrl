

class DataDictionary:
    def __init__(self):
        self.data = {
            'User': {'initiates': [], 'selects': []},
            'Work Role': {'addresses': [], 'initiates': []},
            'Problem': {'links_to': []},
            'Change': {'links_to': [], 'conducts': []},
            'Request': {'links_to': [], 'initiates': []},
            'Change Control Record': {'captures': [], 'determines': [], 'assesses': [], 'references': []},
            'Framework': {'incorporates': []},
            'Playbooks': {'maps': []},
            'Task': {'assigns': []},
            'Role Selected': {'manages': []},
            'Trouble Tickets': {'provides': []}
        }

    def add_relationship(self, from_entity, relationship, to_entity):
        if relationship in self.data[from_entity]:
            self.data[from_entity][relationship].append(to_entity)

    def get_relationships(self, entity, relationship):
        return self.data.get(entity, {}).get(relationship, [])


class RelationshipManager:
    def __init__(self, data_dict):
        self.data_dict = data_dict

    def add_relationships(self, relationships):
        for from_entity, actions in relationships.items():
            for relationship, to_entities in actions.items():
                for to_entity in to_entities:
                    self.data_dict.add_relationship(from_entity, relationship, to_entity)

    def display_relationships(self):
        for entity, relationships in self.data_dict.data.items():
            for relationship, related_entities in relationships.items():
                for related_entity in related_entities:
                    print(f"{entity} {relationship} {related_entity}")


def display_options(options_list):
    for idx, option in enumerate(options_list, start=1):
        print(f"{idx}. {option}")


def get_user_choice(options, message):
    while True:
        try:
            for idx, option in enumerate(options, start=1):
                print(f"{idx}. {option}")
            choice = int(input(message))
            if 1 <= choice <= len(options):
                return options[choice - 1]
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def authenticate_user():
    user_name = input("Enter your name: ")
    # Perform authentication logic here
    return user_name
def main():
    user_name = authenticate_user()
    print(f"Welcome, {user_name}!")

    data_dict = DataDictionary()
    relationship_manager = RelationshipManager(data_dict)

    relationships = {
        'User': {'initiates': ['Work Role'], 'selects': ['Role Selected']},
        'Work Role': {'addresses': ['Problem'], 'initiates': ['Change', 'Request']},
        'Problem': {'links_to': ['Change Control Record']},
        'Change': {'links_to': ['Change Control Record'], 'conducts': ['Evaluation']},
        'Request': {'links_to': ['Change Control Record'], 'initiates': ['Fulfillment']},
        'Change Control Record': {'captures': ['Document Control Information', 'Change Implementation Plan'],
                                  'determines': ['Communication and Notification'],
                                  'assesses': ['Risk Assessment and Control'],
                                  'references': ['Document References']},
        'Framework': {'incorporates': ['Loops', 'Functions']},
        'Playbooks': {'maps': ['Mappings', 'Roles']},
        'Role Selected': {'manages': ['Trouble Tickets']},
        'Trouble Tickets': {'provides': ['View']}
    }

    relationship_manager.add_relationships(relationships)

    while True:
        print("\nPlease choose an option:")
        print("1. View available functions")
        print("2. Display relationships")
        print("3. Exit")

        choice = get_user_choice([1, 2, 3], "Enter the number of your choice: ")

        if choice == 1:
            display_available_functions(data_dict)
        elif choice == 2:
            relationship_manager.display_relationships()
        elif choice == 3:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


def display_available_functions(data_dict):
    print("\nAvailable functions:")
    function_names = list(data_dict.data.keys())
    display_options(function_names)

    choice = get_user_choice(function_names, "Enter the number of the function you want to perform: ")

    if choice:
        chosen_function = function_names[int(choice) - 1]
        print("You selected:", chosen_function)
        display_actions(data_dict, chosen_function)


def display_actions(data_dict, chosen_function):
    actions = list(data_dict.data[chosen_function].keys())
    print("\nActions associated with chosen function:")
    display_options(actions)

    action_choice = get_user_choice(actions, "Enter the number of the action you want to perform: ")

    if action_choice:
        chosen_action = actions[action_choice - 1]
        print("You selected:", chosen_action)
        # Perform the chosen action here


if __name__ == "__main__":
    main()
