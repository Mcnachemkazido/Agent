from modols.fieldagent import FieldAgent,CyberAgent
from modols.mission import Mission



if __name__ == "__main__":
    f1 = FieldAgent("123",5,"gruozlm")
    f2 = FieldAgent("321",10,"tl aviv")
    c1 = CyberAgent("789",3,"sorva")
    c2 = CyberAgent("567",2,"nwe voork")
    print(CyberAgent.get_total_agents())
    CyberAgent.list_of_agent([f1,f2,c1,c2])
    m1 = Mission("good","hir")
    m1.assign_an_agent(f1)
    print(m1.assigned_agent.code_name)
