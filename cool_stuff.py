#!/usr/bin/env python3
"""
Cool Stuff Generator - Makes your terminal look awesome!
"""

import random
import sys
from datetime import datetime

# Constants
INDENT = "    "
SEPARATOR_WIDTH = 50
GREEN = "\033[32m"
RESET = "\033[0m"


def generate_ascii_art():
    """Generate cool ASCII art patterns"""
    patterns = [
        r"""
    ⭐ COOL STUFF GENERATOR ⭐
    ═══════════════════════════
        """,
        r"""
    ╔═══════════════════════════╗
    ║   🚀 AWESOME PATTERNS 🚀   ║
    ╚═══════════════════════════╝
        """,
        r"""
    ┌─────────────────────────┐
    │  ✨ SOMETHING COOL ✨   │
    └─────────────────────────┘
        """
    ]
    return random.choice(patterns)


def generate_gradient():
    """Generate a cool gradient pattern"""
    colors = ['🔴', '🟠', '🟡', '🟢', '🔵', '🟣']
    print("\n" + INDENT + "Gradient Rainbow:")
    print(INDENT + " ".join(colors * 3))
    print()


def generate_matrix_rain():
    """Generate a Matrix-style rain pattern"""
    chars = ['0', '1', '╱', '╲', '│', '─']
    lines = 5
    width = 40
    
    print("\n" + INDENT + "Matrix Style:")
    for _ in range(lines):
        line = INDENT + "".join(random.choice(chars) for _ in range(width))
        print(f"{INDENT}{GREEN}{line}{RESET}")
    print()


def generate_wave_pattern():
    """Generate a wave pattern"""
    wave_chars = ['~', '≈', '∼', '⌇']
    print("\n" + INDENT + "Wave Pattern:")
    for i in range(5):
        spaces = " " * (4 + abs(2 - i) * 2)
        wave = random.choice(wave_chars) * 30
        print(f"{INDENT}{spaces}{wave}")
    print()


def show_timestamp():
    """Show current timestamp with cool formatting"""
    now = datetime.now()
    print(f"\n{INDENT}⏰ Generated at: {now.strftime('%Y-%m-%d %H:%M:%S')}")
    print()


def main():
    """Main function to run all cool stuff"""
    print("\n" + "=" * SEPARATOR_WIDTH)
    print(generate_ascii_art())
    print("=" * SEPARATOR_WIDTH)
    
    print("\n🎨 Generating Cool Patterns...\n")
    
    generate_gradient()
    generate_wave_pattern()
    generate_matrix_rain()
    show_timestamp()
    
    print("=" * SEPARATOR_WIDTH)
    print(INDENT + "✅ Done! Wasn't that cool? 😎")
    print("=" * SEPARATOR_WIDTH + "\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{INDENT}⚠️  Interrupted! See you later! 👋\n")
        sys.exit(0)
