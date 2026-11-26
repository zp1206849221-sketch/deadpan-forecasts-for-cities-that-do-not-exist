import os

LINE = "Port Regret: high 19, low 11, winds west at 25 km/h. Rain from 2pm, falling upward as usual on Thursdays; umbrellas remain under city recall."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
