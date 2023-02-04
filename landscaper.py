game = {"tool": 0, "bank": 0}

tools = [
    {"name":"teeth", "profit": 1, "cost": 0},
    {"name":"rusty scissors",  "profit": 5, "cost": 5},
    {"name":"old push mower",  "profit": 50, "cost": 25},
    {"name":"battery-powered lawnmower",  "profit": 100, "cost": 250},
    {"name":"hire a team of starving students",  "profit": 250, "cost": 500},
]

def cut_grass():
    tool = tools[game['tool']]
    print(f"You cut grass for ${tool['profit']} with your {tool['name']}")
    game['bank'] += tool['profit']
    
def check_stats():
    tool = tools[game["tool"]]
    print(f'You have ${game["bank"]} and are using {tool["name"]}')
    
def upgrade():
    if (game["tool"] >= len(tools) - 1):
        print("No new tools to buy")
        return 0
    next_tool = tools[game["tool"] + 1]
    if (next_tool == None):
        print("No more tool upgrades")
        return 0
    if (game["bank"] < next_tool["cost"]):
        print("Not enough money to buy tool")
        return 0
    print(f'You upgraded your tool to {next_tool["name"]}')
    game["bank"] -= next_tool["cost"]
    game["tool"] += 1
    
def win_check():
    if (game["tool"] == 4 and game["bank"] >= 1000):
        print('You made enough to retire Congrats, if only it was that easy right minus having to use your teeth')
        return True
    return False


user_start = input("You are starting a landscaping business, but all you have are your teeth to start cutting grass and make money [S] Start earing money [Q] Not worth doing")
    
if (user_start == "Q"):
        print("Good luck hope that works out if not come back and make some money")
    
if (user_start == "S"):
    while (True):
        user_choice = input("[1] Cut Grass [2] Check Stats [3] Upgrade [4] Quit")
        
        if (user_choice == "1"):
            cut_grass()
        
        if (user_choice == "2"):
            check_stats()
        
        if (user_choice == "3"):
            upgrade()
        
        if (user_choice == "4"):
            print("You weren't willing to work and quit")
            break
    
        if (win_check()):
            break