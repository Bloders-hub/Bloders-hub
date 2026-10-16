#!/usr/bin/env python3
"""
BLODERS NEURAL CORE & DEVELOPER TERMINAL 🚀
Run anytime:
    python3 bloders.py
or directly from GitHub:
    curl -sSL https://raw.githubusercontent.com/Bloders-hub/Bloders-hub/main/bloders.py | python3
"""

import sys
import time
import random
import os

# Ensure clean UTF-8 output across all operating systems (Windows/Linux/macOS)
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

# ANSI color codes for rich terminal styling
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"
BLUE = "\033[94m"
BOLD = "\033[1m"
DIM = "\033[2m"
RESET = "\033[0m"

# Disable colors on dumb terminals
if not sys.stdout.isatty() or os.environ.get("NO_COLOR"):
    CYAN = GREEN = YELLOW = MAGENTA = BLUE = BOLD = DIM = RESET = ""

ASCII_LOGO = f"""{CYAN}{BOLD}
  ____  _             _                
 | __ )| | ___   __| | ___ _ __ ___  
 |  _ \\| |/ _ \\ / _` |/ _ \\ '__/ __| 
 | |_) | | (_) | (_| |  __/ |  \\__ \\ 
 |____/|_|\\___/ \\__,_|\\___|_|  |___/ 
{RESET}{DIM}   Systems & Distributed Infrastructure Engineer{RESET}
"""

QUOTES = [
    "I don't just fix bugs — I teach them to pay rent. 🐛🏠",
    "There are 10 types of people: those who understand binary, and those who don't.",
    "Good code is its own documentation. Great code has 100% test coverage.",
    "Write code so resilient you can sleep peacefully at night. 🛌💤",
    "First, solve the problem. Then, write the code. Finally, benchmark it.",
    "A clean git history is a love letter to your future self.",
    "Fail-fast in milliseconds, recover in silence, log with precision."
]

SKILLS = {
    "Languages": ["Python", "TypeScript", "JavaScript", "POSIX Shell / Bash"],
    "Infrastructure": ["Docker", "Linux Containers", "PostgreSQL", "Redis", "GitHub Actions"],
    "Architecture": ["Distributed Systems", "Circuit Breakers", "Resilience Engineering", "REST & RPC APIs"],
    "Testing & Quality": ["Pytest", "Vitest", "Jest", "Test-Driven Development (100% Armor)"]
}


def type_print(text: str, delay: float = 0.02, end: str = "\n"):
    """Animated typewriter effect"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(end)
    sys.stdout.flush()


def run_progress_bar(task_name: str, duration: float = 0.6):
    """Render a smooth terminal progress bar"""
    steps = 25
    sys.stdout.write(f"[*] {task_name:<36} [")
    for _ in range(steps):
        time.sleep(duration / steps)
        sys.stdout.write(f"{GREEN}█{RESET}")
        sys.stdout.flush()
    sys.stdout.write(f"] {GREEN}100% OK{RESET}\n")


def print_system_status():
    print(f"\n{BOLD}==================== SYSTEM METRICS ===================={RESET}")
    print(f"  ● {BOLD}Identity:{RESET}        Bloders (@Bloders-hub)")
    print(f"  ● {BOLD}Core Focus:{RESET}      Systems & Distributed Infrastructure")
    print(f"  ● {BOLD}Test Armor:{RESET}      {GREEN}100/100 (Zero Regressions Enforced){RESET}")
    print(f"  ● {BOLD}Coffee Reserves:{RESET} {YELLOW}98.4% (Optimal){RESET}")
    print(f"  ● {BOLD}Status:{RESET}           {GREEN}ONLINE & READY TO SHIP{RESET}")
    print(f"{BOLD}========================================================{RESET}\n")


def print_skills():
    print(f"{MAGENTA}{BOLD}--- TECH STACK & ARSENAL ---{RESET}")
    for category, items in SKILLS.items():
        print(f"  {BOLD}{category}:{RESET}")
        print(f"    {CYAN}•{' • '.join(items)}{RESET}")
    print()


def main():
    if "--quote" in sys.argv:
        print(f"\n{YELLOW}💡 \"{random.choice(QUOTES)}\"{RESET}\n")
        return

    print(ASCII_LOGO)
    type_print(f"{DIM}Booting Bloders Runtime Environment...{RESET}\n", delay=0.015)

    run_progress_bar("Initializing Neural Core", 0.4)
    run_progress_bar("Verifying Test Armor (Pytest/Vitest)", 0.5)
    run_progress_bar("Linking Open-Source Pipelines", 0.4)
    run_progress_bar("Calibrating Coffee Sensors", 0.3)

    print_system_status()
    print_skills()

    quote = random.choice(QUOTES)
    print(f"{YELLOW}💡 Today's Thought:{RESET} \"{quote}\"\n")
    print(f"{DIM}Tip: Check out my GitHub profile at https://github.com/Bloders-hub{RESET}\n")


if __name__ == "__main__":
    main()
