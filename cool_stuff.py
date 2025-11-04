#!/usr/bin/env python3
"""
Cool Stuff Generator - Makes your terminal look awesome!
"""

import random
import sys
from datetime import datetime


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
    print("\n    Gradient Rainbow:")
    print("    " + " ".join(colors * 3))
    print()


def generate_matrix_rain():
    """Generate a Matrix-style rain pattern"""
    chars = ['0', '1', '╱', '╲', '│', '─']
    lines = 5
    width = 40
    
    print("\n    Matrix Style:")
    for _ in range(lines):
        line = "    " + "".join(random.choice(chars) for _ in range(width))
        print(f"    \033[32m{line}\033[0m")  # Green color
    print()


def generate_wave_pattern():
    """Generate a wave pattern"""
    wave_chars = ['~', '≈', '∼', '⌇']
    print("\n    Wave Pattern:")
    for i in range(5):
        spaces = " " * (4 + abs(2 - i) * 2)
        wave = random.choice(wave_chars) * 30
        print(f"    {spaces}{wave}")
    print()


def show_timestamp():
    """Show current timestamp with cool formatting"""
    now = datetime.now()
    print(f"\n    ⏰ Generated at: {now.strftime('%Y-%m-%d %H:%M:%S')}")
    print()


def main():
    """Main function to run all cool stuff"""
    print("\n" + "=" * 50)
    print(generate_ascii_art())
    print("=" * 50)
    
    print("\n🎨 Generating Cool Patterns...\n")
    
    generate_gradient()
    generate_wave_pattern()
    generate_matrix_rain()
    show_timestamp()
    
    print("=" * 50)
    print("    ✅ Done! Wasn't that cool? 😎")
    print("=" * 50 + "\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n    ⚠️  Interrupted! See you later! 👋\n")
        sys.exit(0)
