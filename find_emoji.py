import re
with open('index.html','r',encoding='utf-8') as f:
    content = f.read()

# Find remaining emoji
emoji_pattern = re.compile(r'[\U0001F300-\U0001FAFF\u2600-\u27BF\u2700-\u27BF\u2B50\u2702-\u27B0\u24C2-\U0001F251\u200D\uFE0F\u20E3\u0023-\u0039\u00A9\u00AE\u2122\u2139\u2328\u23CF\u23E9-\u23F3\u23F8-\u23FA\u24C2\u25AA-\u25AB\u25B6\u25C0\u25FB-\u25FE\u2600-\u2B55\u2934-\u2935\u2B05-\u2B07\u2B1B-\u2B1C\u2B50\u2B55\u3030\u303D\u3297\u3299\U0001F000-\U0001FFFF]')
matches = emoji_pattern.findall(content)

seen = {}
for m in matches:
    if m not in seen:
        idx = content.find(m)
        ctx = content[max(0,idx-20):idx+30].replace('\n',' ')
        seen[m] = ctx

with open('remaining_emoji.txt','w',encoding='utf-8') as out:
    for e,c in seen.items():
        out.write(f'EMOJI: {repr(e)} -> ...{c}...\n')
    out.write(f'\nTotal: {len(matches)}\n')

print(f'Total remaining: {len(matches)}')
