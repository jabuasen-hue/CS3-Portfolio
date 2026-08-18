# zodiacSectionLN.py

# Define baseline year and zodiac signs with Chinese characters and pinyin
START_YEAR = 1900
ZODIAC_SIGNS = [
    "Rat (鼠 / Shǔ)",
    "Ox (牛 / Niú)",
    "Tiger (虎 / Hǔ)",
    "Rabbit (兔 / Tù)",
    "Dragon (龙 / Lóng)",
    "Snake (蛇 / Shé)",
    "Horse (马 / Mǎ)",
    "Goat (羊 / Yáng)",
    "Monkey (猴 / Hóu)",
    "Rooster (鸡 / Jī)",
    "Dog (狗 / Gǒu)",
    "Pig (猪 / Zhū)"
]

def main():
    # Requirement a: Ask the user to enter a year of birth
    try:
        birth_year = int(input("Enter your birth year: "))
    except ValueError:
        print("Invalid input! Please enter a valid integer year.")
        return

    # Requirement b & c: Validate user input (must not be earlier than 1900)
    if birth_year < START_YEAR:
        print(f"Invalid year! Year of birth must not be earlier than {START_YEAR}.")
        return

    # Requirement d & e: Determine Chinese zodiac sign using modulo arithmetic
    # Baseline year 1900 maps to index 0 (Rat)
    zodiac_index = (birth_year - START_YEAR) % 12
    zodiac_sign = ZODIAC_SIGNS[zodiac_index]

    # Display output
    print(f"Your Chinese Zodiac Sign is: {zodiac_sign}")

if __name__ == "__main__":
    main()