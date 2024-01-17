import pyautogui
import numpy as np
import time

STARTING_GOLD = 10
STARTING_LIVES = 5
STARTING_TURN = 1
STARTING_VICTORIES = 0
STARTING_PETS = []
STARTING_SHOP = []

# Pets
tier_1 = ['ant', 'pig', 'fish', 'cricket', 'mosquito', 'beaver', 'otter', 'duck', 'horse', 'pigeon']
tier_2 = ['rat', 'hedgehog', 'flamingo', 'spider', 'worm', 'goose', 'peacock', 'snail', 'crab', 'kangaroo']
tier_3 = ['dolphin', 'rabbit', 'dog', 'dodo', 'elephant', 'sheep', 'badger', 'camel', 'ox', 'giraffe']
tier_4 = ['blowfish', 'skunk', 'turtle', 'squirrel', 'deer', 'bison', 'whale', 'penguin', 'hippo', 'parrot']
tier_5 = ['scorpion', 'rhino', 'seal', 'armadillo', 'cow', 'monkey', 'shark', 'turkey', 'crocodile', 'rooster']
tier_6 = ['dragon', 'leopard', 'mammoth', 'gorilla', 'boar', 'tiger', 'snake', 'fly', 'cat', 'wolverine']

# Food
tier_1_food = ['apple', 'honey']
tier_2_food = ['sleeping_pill', 'cupcake', 'meatbone']
tier_3_food = ['salad', 'garlic']
tier_4_food = ['canned_food', 'pear']
tier_5_food = ['chili', 'chocolate', 'sushi']
tier_6_food = ['pizza', 'mushroom', 'steak', 'melon']

class SuperAutoBots:
    def __init__(self):
        self.alive = True
        self.gold = STARTING_GOLD
        self.lives = STARTING_LIVES
        self.turn = STARTING_TURN
        self.victories = STARTING_VICTORIES
        self.pets = STARTING_PETS
        self.shop = STARTING_SHOP

    def start_game(self):
        # Wait a few seconds before starting
        print("Welcome to SuperAutoBots! Getting started in a few seconds...")
        time.sleep(3)
        # Click the "Play" button
        pyautogui.moveTo(835, 276, duration=0.1)
        pyautogui.click()
        # Click the "Arena" button
        pyautogui.moveTo(835, 290, duration=0.1)
        pyautogui.click()
        # Click the "Start" button (assuming you have the correct pack selected)
        pyautogui.moveTo(1460, 937, duration=0.4)
        pyautogui.click()
        # Game has begun!
        print("Let's go!")
        
    def identify_shop(self):
        print("Identifying shop...")
        # List of all possible pets by tier
        possible_pets_by_tier = {
            'tier_1': ['ant', 'pig', 'fish', 'cricket', 'mosquito', 'beaver', 'otter', 'duck', 'horse', 'mouse'],
            # 'tier_2': ['rat', 'hedgehog', 'flamingo', 'spider', 'worm', 'goose', 'peacock', 'snail', 'crab', 'kangaroo'],
            # 'tier_3': ['dolphin', 'rabbit', 'dog', 'dodo', 'elephant', 'sheep', 'badger', 'camel', 'ox', 'giraffe'],
            # 'tier_4': ['blowfish', 'skunk', 'turtle', 'squirrel', 'deer', 'bison', 'whale', 'penguin', 'hippo', 'parrot'],
            # 'tier_5': ['scorpion', 'rhino', 'seal', 'armadillo', 'cow', 'monkey', 'shark', 'turkey', 'crocodile', 'rooster'],
            # 'tier_6': ['dragon', 'leopard', 'mammoth', 'gorilla', 'boar', 'tiger', 'snake', 'fly', 'cat', 'wolverine']
        }
        # Initialize the shop as an empty list
        self.shop = []
        # Loop over all possible pets by tier
        for tier, pets in possible_pets_by_tier.items():
            for pet in pets:
                # Check if the pet is in the shop
                try:
                    pet_location = pyautogui.locateCenterOnScreen(f'pets/{pet}.png', confidence=0.8)
                    if pet_location is not None:
                        # The pet is in the shop, so add it to the list
                        self.shop.append(pet)
                except pyautogui.ImageNotFoundException:
                    # The pet is not in the shop, so continue with the next pet
                    continue
        print(f"The shop contains: {self.shop}")

    def play_round(self):
        print(f"Playing round #{self.turn}...")
        print(f"Our current pets are: {self.pets}")
        self.identify_shop()
        # Your code to play a round goes here...
        # Update the state after the round
        self.gold = new_gold
        self.lives = new_lives
        self.turn += 1
        self.victories = new_victories
        self.pets = new_pets
        self.shop = new_shop

while True:
    game = SuperAutoBots()
    game.start_game()

    while game.alive:
        game.play_round()

        # Check if the game is over
        if game.lives <= 0:
            game.alive = False
            
    # Game over... Start again!
