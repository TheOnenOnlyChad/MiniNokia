# MiniNokiaV1

A menu-driven CLI "feature phone" written in Python. It bundles a calculator, a live date/time display, and a keyboard reaction-time game into a single script, driven by a `while` loop and `input()`-based menu dispatch.

## Features

| Option | Module | Description |
|---|---|---|
| 1. Calculator | built-in | Takes two integers and an operator (`+ - * /`), prints the result. Guards against division by zero. Loops until the user quits. |
| 2. Date/Time | `time` | Prints the date (`dd/mm/yy`) and a live 12-hour clock refreshed every second via carriage return (`\r`). Exit with `Ctrl+C` (handled via `KeyboardInterrupt`). |
| 3. Games | `keyboard`, `random`, `string`, `time` | 3-round reaction-time game. A random key is shown, and the player must press it as fast as possible. |
| 4. Exit | - | Ends the main loop. |

### Reaction game logic

- The target key is sampled from `a-z`, `0-9`, and a set of punctuation characters.
- The timer starts when the key is displayed (`time.time()`), and stops when `keyboard.read_key(suppress=True)` returns.
- A wrong key scores the round as `0` and is excluded from the average.
- The average is computed over valid rounds only, then mapped to a rank:

| Avg reaction time | Rank |
|---|---|
| < 0.8 s | F1 driver |
| < 1.6 s | Soldier |
| < 2.4 s | Normal human |
| otherwise | Snail |

## Requirements

- Python 3.x
- [`keyboard`](https://pypi.org/project/keyboard/) (third-party)

```bash
pip install keyboard
```

> **Platform note:** `keyboard` hooks global key events. On Linux it needs root (`sudo python MiniNokiaV1.py`). On macOS the terminal needs Accessibility/Input Monitoring permission. It works without extra setup on Windows.

## Run

```bash
python MiniNokiaV1.py
```

## Project structure

```
MiniNokiaV1.py   # entire application (single file)
```

## Known limitations

- Calculator uses `int()`, so decimals and non-numeric input raise `ValueError`.
- If all three reaction rounds are wrong, the average evaluates to `0`, so the `rt == 10` "all wrong" branch is never reached and the player is ranked as F1 driver.
- Using `0` as the "wrong round" sentinel conflates a missed round with a real time of 0.
- The game's three rounds are copy-pasted; they could be refactored into a function with a loop.
- `keyboard.read_key()` may return on a key-release event, which can skew timing.

## Possible improvements

- Switch to `float()` input with `try/except` validation.
- Replace the sentinel value with `None` and compute the average via `sum(valid) / len(valid)`.
- Extract each menu option into its own function.
- Replace the global-hook `keyboard` dependency with `msvcrt`/`termios` or `curses` for portability.

---
*My first Python program.*
