import pyautogui
import cv2
import numpy as np
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
            pet_image = cv2.imread(f'pets/{pet}.png')
            screen = np.array(pyautogui.screenshot())

            result = cv2.matchTemplate(screen, pet_image, cv2.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

            # You can adjust the threshold based on your needs
            if max_val > 0.7:
                pet_location = (max_loc[0] + pet_image.shape[1] / 2, max_loc[1] + pet_image.shape[0] / 2)
                shop.append((pet, pet_location))

    print(f"The shop contains: {shop}")

if __name__ == "__main__":
    identify_shop()
