import os

LINE = "I held the door for you on floor 14. It cost me 2% battery. Please do not mention it. Ever."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
