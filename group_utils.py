import random

class Group:
    '''A class for Group utilities. A Group consists of people that are associated with:
          - a name
          - amount of time in group (in years)
          - relevant skills to the group
          
        Fields:
        person_list: a list of people. See the documentation for the constructor
        for the description of a person.
        skill_dict: a dict from a skill (string) to a set of all of the people's
        names (strings) who have that skill'''

    '''Constructor for a Group that takes in a list of people. Assume all names are unique.
    
    Parameters:
    starting_list -- (default empty list): a list of dicts representing people
                     the dicts must have the following key/value pairs:
                    "name" (maps to a person's name as a string)
                    "time in group" (maps to how long the person has been in the group, as a float)
                    "skills" (maps to a list of strings representing the person's skills)
    '''
    def __init__(self, starting_list: list[dict] = None):
        if starting_list is None:
            self.person_list = []
        else:
            self.person_list = starting_list
        self.populate_skills()

    def populate_skills(self) -> None:
        ''' Goes through the people in person_list and populates skill_dict,
        which maps a skill name to a Set of people who have that skill. Intended
        as a helper function for the constructor (should not be called 
        by itself).'''

        self.skill_dict = {}
        for person in self.person_list:
            for skill in person["skills"]:
                if skill not in self.skill_dict:
                    self.skill_dict[skill] = set([person["name"]])
                else:
                    self.skill_dict[skill].add(person["name"])

    def add_person(self, name: str, time: float, skills: list[str]) -> None:
        '''Adds a person to the person list. Assume a person of that name does not already 
        exist in the group.
        
        Parameters:
        name   -- The person's name (as a string)
        time   -- The time the person has been in the group (as a float)
        skills -- The list of skills (as a string)
        '''

        # makes a copy of the skills list to avoid mutation from the outside
        new_person = {"name": name, "time in group": time, "skills": list(skills)}

        self.person_list.append(new_person)
        for skill in skills:
            self.skill_dict[skill].add(name)

    def add_skill(self, name: str, skill: str) -> None:
        '''Associates the person with the given name the skill in both
        person_list and skill_dict. If the name is not in the group or
        the person already has the skill, does nothing.
        
        name  -- The person's name (as a string)
        skill -- the skill to be added (as a string)
        '''

        for person in self.person_list:
            if person["name"] == name:
                person["skills"].append(skill)

    def person_has_skill(self, name: str, skill: str) -> bool:
        '''Returns true if a person with the given name in the group 
        who has the given skill. 

        Parameters:
        name  -- the name of the person
        skill -- the skill to check

        Returns:
        a boolean that answers whether or not the person has the skill
        '''

        return name in self.skill_dict[skill]

    def average_length_of_membership(self) -> float:
        '''Returns the average (arithmetic mean) of the time all members have 
        been in the group. If there are no people in the group, should return 0.
        
        Returns:
        a float representing the average time all members have been in the group
        '''

        level_sum = 0
        for person in self.person_list:
            level_sum += person["time in group"]

        return level_sum
    
    def measure_progress(self, name: str) -> float:
        '''Returns the number of skills divided by the length of time the person
        has been in the group. Raises a LookupError if the person is not found 
        in the group. Does not handle division by zero (meaning Python will 
        raise an error if the time in group is 0).
        
        Parameters:
        name -- the name of the person
        
        Returns:
        a float representing the number of skills divided by the length of time
        in the group
        '''

        for person in self.person_list:
            if person["name"] == name:
                return len(person["skills"]) / person["time in group"]
        raise LookupError("Person was not found!")

    def n_person_subgroup(self, n: int) -> list[str]:
        '''Returns a list of the names of n random people from the group. If n 
        exceeds the number of people in the group, returns the names of all of 
        the people in the group. If n is 0 or negative, returns an empty list.
        
        Parameters:
        n -- the size of the subgroup to be returned
        
        Returns:
        a list of names (as strings) of n random people from the group
        '''
        if n <= 0:
            return []

        # we don't care what order person_list is in, so mutating it this way is fine
        random.shuffle(self.person_list)

        name_list = [p["name"] for p in self.person_list]
        return name_list[1:n + 1]