import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html','r',encoding='utf-8') as f:
    content = f.read()

emoji_ranges = [
    (0x1F600, 0x1F64F), (0x1F300, 0x1F5FF), (0x1F680, 0x1F6FF), (0x1F1E0, 0x1F1FF),
    (0x2600, 0x26FF), (0x2700, 0x27BF), (0x1F900, 0x1F9FF), (0x1FA00, 0x1FA6F),
    (0x1FA70, 0x1FAFF), (0x231A, 0x231B), (0x23E9, 0x23F3), (0x23F8, 0x23FA),
    (0x25AA, 0x25AB), (0x25B6, 0x25B6), (0x25C0, 0x25C0), (0x25FB, 0x25FE),
    (0x2934, 0x2935), (0x2B05, 0x2B07), (0x2B1B, 0x2B1C), (0x2B50, 0x2B50),
    (0x2B55, 0x2B55), (0x3030, 0x3030), (0x303D, 0x303D), (0x3297, 0x3297),
    (0x3299, 0x3299),
]

def is_emoji(cp):
    for lo, hi in emoji_ranges:
        if lo <= cp <= hi:
            return True
    return False

for i, ch in enumerate(content):
    if is_emoji(ord(ch)):
        before = content[max(0,i-200):i]
        if '<svg' in before and '</svg' not in before:
            continue
        ctx = content[max(0,i-30):min(len(content),i+30)].replace('\n',' ')
        print(f"U+{ord(ch):04X} -> ...{ctx}...")
