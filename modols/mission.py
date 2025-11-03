
class Mission:
    def __init__(self,mission_name:str,target_location:str):
        self.mission_name = mission_name
        self.target_location = target_location
        self.assigned_agent =None

    def assign_an_agent(self,agent:Agent):
        self.assigned_agent = agent

    def print_mission(self):
        print(f" Mission:{ self.mission_name},"
              f" Target:{self.target_location}, Agent:{self.assigned_agent.code_name}")

