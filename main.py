import os

LINE = "So... you also pretend to charge at 38% just to avoid small talk on floor 14?"

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
