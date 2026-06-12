import sys, re
sys.stdout.reconfigure(encoding='utf-8')
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

scripts = re.findall(r'<script[^>]*>(.*?)</script>', content, re.DOTALL)
for i, s in enumerate(scripts):
    if len(s) > 1000:
        # Find line with dragData or attachDragListeners issues
        lines = s.split('\n')
        for j, line in enumerate(lines):
            if 'dragData' in line or 'attachDrag' in line or 'planMap' in line:
                if 'function ' in line or 'var ' in line or 'if ' in line:
                    print(f'Line ~{j}: {line.strip()[:150]}')
        
        # Check for }); without matching {
        for j, line in enumerate(lines):
            stripped = line.strip()
            if stripped == '});' and j > 0:
                prev = lines[j-1].strip()
                if prev and not prev.endswith(')') and not prev.endswith('})'):
                    print(f'Possible orphan }}); at line {j}: prev={prev[:80]}')
        print(f'Script block {i}: {len(s)} chars checked')
