from modols.agent import Agent

class FieldAgent(Agent):
    def __init__(self,code_name:str,clearance_level:int,region:str):
        super().__init__(code_name,clearance_level)
        self.region = region

    def print_details(self):
        super().print_details()
        print("region:",self.region)


class CyberAgent(Agent):
    def __init__(self,code_name:str,clearance_level:int,specialty):
        super().__init__(code_name,clearance_level)
        self.specialty = specialty

    def print_details(self):
        super().print_details()
        print("specialty:",self.specialty)

    @staticmethod
    def list_of_agent(list_agent):
        for agent in list_agent:
            agent.print_details()