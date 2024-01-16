# test_image_recognition.py

import pyautogui
import time

def identify_shop():
    print("Wait a few seconds before starting...")
    time.sleep(3)
    print("Identifying shop...")
    possible_pets_by_tier = {
        'tier_1': ['ant', 'pig', 'fish', 'cricket', 'mosquito', 'beaver', 'otter', 'duck', 'horse', 'mouse'],
    }
    shop = []
    for tier, pets in possible_pets_by_tier.items():
        for pet in pets:
            try:
                pet_location = pyautogui.locateCenterOnScreen(f'pets/{pet}.png', confidence=0.5)
                if pet_location is not None:
                    shop.append(pet)
            except pyautogui.ImageNotFoundException:
                continue
    print(f"The shop contains: {shop}")

if __name__ == "__main__":
    identify_shop()