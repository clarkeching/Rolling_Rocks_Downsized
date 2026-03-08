#!/usr/bin/env python3
"""Update Full Text chapter navigation to include prev/next full text links."""

import os
import re

FULL_TEXT_DIR = "/sessions/stoic-dazzling-mendel/mnt/Documents/Rolling_Rocks_Vault/Full_Text"

for i in range(1, 62):
    ch_num = f"{i:02d}"
    filepath = os.path.join(FULL_TEXT_DIR, f"Chapter_{ch_num}_Full.md")

    if not os.path.exists(filepath):
        print(f"Skipping {filepath} - not found")
        continue

    with open(filepath, 'r') as f:
        content = f.read()

    # Build new navigation
    prev_num = f"{i-1:02d}" if i > 1 else None
    next_num = f"{i+1:02d}" if i < 61 else None

    # Top navigation - back to summary
    top_nav = f"[[Chapter_{ch_num}|← Back to Chapter {i} Summary]]"

    # Bottom navigation - prev/next full text + summary
    bottom_parts = []
    if prev_num:
        bottom_parts.append(f"[[Full_Text/Chapter_{prev_num}_Full|← Chapter {i-1} Full]]")
    bottom_parts.append(f"[[Chapter_{ch_num}|📋 Summary]]")
    if next_num:
        bottom_parts.append(f"[[Full_Text/Chapter_{next_num}_Full|Chapter {i+1} Full →]]")

    bottom_nav = " | ".join(bottom_parts)

    # Replace old navigation at top
    # Pattern: [[Chapter_XX|← Back to Chapter XX Summary]]
    content = re.sub(
        r'\[\[Chapter_\d+\|← Back to Chapter \d+ Summary\]\]',
        top_nav,
        content,
        count=1
    )

    # Replace old navigation at bottom (last occurrence)
    # Find last occurrence and replace
    old_bottom_pattern = r'\[\[Chapter_\d+\|← Back to Chapter \d+ Summary\]\]\s*$'
    if re.search(old_bottom_pattern, content):
        content = re.sub(old_bottom_pattern, bottom_nav, content)

    with open(filepath, 'w') as f:
        f.write(content)

    print(f"Updated Chapter {i}")

print("\nDone!")
