
class Agent:
    __total_agents = 0

    def __init__(self,code_name:str,clearance_level:int):
        self.code_name = code_name
        self.__clearance_level = clearance_level
        Agent.__total_agents += 1

    def print_details(self):
        print(f"agent:{self.code_name}, "
              f"clearance Level:{self.__clearance_level }")

    @property
    def agent_data(self):
        return self.__clearance_level

    @agent_data.setter
    def agent_data(self,status):
        if 1 >= status <= 10:
            self.__clearance_level = status
        else:
            print("error")

    @classmethod
    def get_total_agents(cls):
        return f"total_agents: {cls.__total_agents}"









