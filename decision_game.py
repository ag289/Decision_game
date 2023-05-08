import random

# Define decision-making scenario
options = ['Buy a house', 'Rent a house', 'Invest in stocks']
outcomes = {
    'Buy a house': {
        'Monthly income': {'Good': 20, 'Average': 10, 'Low': 5},
        'Savings': {'High': 25, 'Medium': 15, 'Low': 5},
        'Location': {'Close to work': 20, 'Good neighborhood': 15, 'Affordable area': 10},
        'Family size': {'Small': 20, 'Medium': 15, 'Large': 5}
    },
    'Rent a house': {
        'Monthly income': {'Good': 15, 'Average': 10, 'Low': 5},
        'Savings': {'High': 10, 'Medium': 5, 'Low': 3},
        'Location': {'Close to work': 15, 'Good neighborhood': 10, 'Affordable area': 5},
        'Family size': {'Small': 15, 'Medium': 10, 'Large': 5}
    },
    'Invest in stocks': {
        'Monthly income': {'Good': 25, 'Average': 15, 'Low': 5},
        'Savings': {'High': 30, 'Medium': 20, 'Low': 10},
        'Investment knowledge': {'Expert': 25, 'Intermediate': 15, 'Novice': 5},
        'Risk tolerance': {'High': 25, 'Medium': 15, 'Low': 5}
    }
}

# Define player and game
class Player:
    def __init__(self):
        self.score = 0

class Game:
    def __init__(self):
        self.player = Player()
        self.rounds = 5
        
    def play(self):
        print(f"Starting game with {self.rounds} rounds.")
        for i in range(self.rounds):
            print(f"\nRound {i+1}:")
            # Generate random input values
            input_values = {
                'Monthly income': random.choice(['Good', 'Average', 'Low']),
                'Savings': random.choice(['High', 'Medium', 'Low']),
                'Location': random.choice(['Close to work', 'Good neighborhood', 'Affordable area']),
                'Family size': random.choice(['Small', 'Medium', 'Large'])
            }
            # Display options and let player choose
            print(f"\nYour choices:")
            for input_, value in input_values.items():
                print(f"{input_}: {value}")
            print("\nYour options:")
            for index, option in enumerate(options):
                print(f"{index+1}. {option}")
            valid_choices = list(range(1, len(options)+1))
            choice = int(input(f"\nWhich option do you choose? Type the number {str(valid_choices)}: "))
            while choice not in valid_choices:
                print(f"Invalid choice, please select a number from {valid_choices}.")
                choice = int(input(f"\nWhich option do you choose? Type the number {str(valid_choices)}: "))
            option = options[choice-1]
            print(f"You chose to {option}.")
            # Evaluate outcome and update score
            outcome = 0
            for input_, value in input_values.items():
                outcome += outcomes.get(option, {}).get(input_, {}).get(value, 0)
            self.player.score += outcome
            print(f"You earned {outcome} points.")
        
        # Provide feedback based on statistical analysis of outcomes
        average_score = self.player.score / self.rounds
        if average_score > 70:
            print("\nBased on statistical analysis of your decisions, your decision-making skills are excellent!")
        elif average_score > 50:
            print("\nBased on statistical analysis of your decisions, your decision-making skills are average.")
        elif average_score > 30:
            print("\nBased on statistical analysis of your decisions, your decision-making skills are low.")
            
        # Ask if user wants to play again
        choice = input("Do you want to play again? (y/n)")
        if choice.lower() == 'y':
            self.play()




# Play game
game = Game()
game.play()
