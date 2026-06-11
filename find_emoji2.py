import re
with open('index.html','r',encoding='utf-8') as f:
    content = f.read()

# More precise emoji detection - only match actual emoji characters
# Emoji have codepoints in specific ranges
emoji_ranges = [
    (0x1F600, 0x1F64F),  # Emoticons
    (0x1F300, 0x1F5FF),  # Misc Symbols and Pictographs
    (0x1F680, 0x1F6FF),  # Transport and Map
    (0x1F1E0, 0x1F1FF),  # Flags
    (0x2600, 0x26FF),    # Misc symbols
    (0x2700, 0x27BF),    # Dingbats
    (0xFE00, 0xFE0F),    # Variation Selectors
    (0x1F900, 0x1F9FF),  # Supplemental Symbols and Pictographs
    (0x1FA00, 0x1FA6F),  # Chess Symbols
    (0x1FA70, 0x1FAFF),  # Symbols and Pictographs Extended-A
    (0x231A, 0x231B),    # Watch, Hourglass
    (0x23E9, 0x23F3),    # Double triangles
    (0x23F8, 0x23FA),    # Media controls
    (0x25AA, 0x25AB),    # Small squares
    (0x25B6, 0x25B6),    # Play
    (0x25C0, 0x25C0),    # Reverse
    (0x25FB, 0x25FE),    # Medium squares
    (0x2934, 0x2935),    # Curved arrows
    (0x2B05, 0x2B07),    # Arrow emoji
    (0x2B1B, 0x2B1C),    # Black/white large squares
    (0x2B50, 0x2B50),    # Star
    (0x2B55, 0x2B55),    # Circle
    (0x3030, 0x3030),    # Wavy dash
    (0x303D, 0x303D),    # Part alternation mark
    (0x3297, 0x3297),    # Japanese congratulations
    (0x3299, 0x3299),    # Japanese secret
]

def is_emoji(cp):
    for lo, hi in emoji_ranges:
        if lo <= cp <= hi:
            return True
    return False

remaining = []
i = 0
while i < len(content):
    cp = ord(content[i])
    if is_emoji(cp):
        # Check if this is inside an SVG (skip if inside <svg...>)
        before = content[max(0,i-200):i]
        if '<svg' in before and '</svg' not in before:
            i += 1
            continue
        ctx_start = max(0, i-30)
        ctx_end = min(len(content), i+30)
        ctx = content[ctx_start:ctx_end].replace('\n',' ').replace('\r','')
        remaining.append(f'U+{cp:04X} ({content[i]}) -> ...{ctx}...')
        i += 1
    else:
        i += 1

with open('remaining_emoji.txt','w',encoding='utf-8') as out:
    for r in remaining:
        out.write(r + '\n')
    out.write(f'\nTotal remaining: {len(remaining)}\n')

print(f'Total remaining emoji: {len(remaining)}')
