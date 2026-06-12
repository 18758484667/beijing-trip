import sys, re
sys.stdout.reconfigure(encoding='utf-8')
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()
srcs = re.findall(r'src="([^"]+)"', content)
for s in srcs:
    print(s)
