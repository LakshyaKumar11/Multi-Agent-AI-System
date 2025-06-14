from agents.planner_agent import PlannerAgent

if __name__ == '__main__':
    user_goal = input("Enter your goal: ")
    planner = PlannerAgent()
    result = planner.execute(user_goal)
    print("\nFinal Result:")
    print(result)
