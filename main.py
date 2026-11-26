"""Deadpan forecast for the city of Port Regret.

Writes one straight-faced broadcast line to /output/entry.txt:
a forecast for a city that does not exist, where Thursday rain
falls upward and the umbrellas are still under city recall.
"""

import os

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")
MAX_CHARS = 200

# Forecast building blocks, kept apart so each piece can be tuned.
CITY = "Port Regret"
TEMPERATURES = "high 19, low 11"
WIND = "westerly winds at 25 km/h"
RAIN = "Rain from 2pm, falling upward as usual on Thursdays"
RECALL = "umbrellas still under city recall"


def build_line():
    """Assemble the forecast as a single deadpan sentence."""
    return f"{CITY}: {TEMPERATURES}, {WIND}. {RAIN}; {RECALL}."


def validate(line):
    """The entry must be exactly one non-empty line within the limit."""
    if not line:
        raise ValueError("forecast line is empty")
    if line != line.strip():
        raise ValueError("forecast line has leading or trailing whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("forecast must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"forecast is {len(line)} chars, over the {MAX_CHARS} limit"
        )
    if not line.endswith("."):
        raise ValueError("forecast must end with a full stop")


def write_entry(line):
    """Write the line, then read it back to prove it landed intact."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        if f.read() != line:
            raise IOError("written entry does not match the forecast line")


def main():
    line = build_line()
    validate(line)
    write_entry(line)


if __name__ == "__main__":
    main()
