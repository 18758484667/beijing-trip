import re

with open('index.html','r',encoding='utf-8') as f:
    content = f.read()

# More replacements - these are in name fields, category fields, and render functions
replacements = [
    # Street names in DATA.food.streets
    ("name:'🏮 前门大街 · 大栅栏'", "name:'<svg viewBox=\"0 0 24 24\" width=\"16\" height=\"16\" fill=\"none\" stroke=\"var(--red)\" stroke-width=\"2\" style=\"vertical-align:middle;margin-right:4px;\"><path d=\"M8 2h8M4 7h16M7 7v10a3 3 0 0 0 3 3h4a3 3 0 0 0 3-3V7M12 20v2\"/></svg>前门大街 · 大栅栏'"),
    ("name:'🕌 牛街'", "name:'<svg viewBox=\"0 0 24 24\" width=\"16\" height=\"16\" fill=\"none\" stroke=\"var(--red)\" stroke-width=\"2\" style=\"vertical-align:middle;margin-right:4px;\"><path d=\"M3 21h18M5 21V7l7-4 7 4v14M9 21v-6h6v6\"/></svg>牛街'"),
    ("name:'🍜 簋街'", "name:'<svg viewBox=\"0 0 24 24\" width=\"16\" height=\"16\" fill=\"none\" stroke=\"var(--red)\" stroke-width=\"2\" style=\"vertical-align:middle;margin-right:4px;\"><path d=\"M18 8h1a4 4 0 0 1 0 8h-1M2 8h16v9a4 4 0 0 1-4 4H6a4 4 0 0 1-4-4V8z\"/></svg>簋街'"),
    ("name:'🏛️ 护国寺小吃街'", "name:'<svg viewBox=\"0 0 24 24\" width=\"16\" height=\"16\" fill=\"none\" stroke=\"var(--red)\" stroke-width=\"2\" style=\"vertical-align:middle;margin-right:4px;\"><rect x=\"3\" y=\"7\" width=\"18\" height=\"13\" rx=\"1\"/></svg>护国寺小吃街'"),
    ("name:'🎨 五道营胡同'", "name:'<svg viewBox=\"0 0 24 24\" width=\"16\" height=\"16\" fill=\"none\" stroke=\"var(--red)\" stroke-width=\"2\" style=\"vertical-align:middle;margin-right:4px;\"><circle cx=\"12\" cy=\"12\" r=\"10\"/><path d=\"M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10\"/><path d=\"M2 12h20\"/></svg>五道营胡同'"),
    ("name:'🏘️ 杨梅竹斜街'", "name:'<svg viewBox=\"0 0 24 24\" width=\"16\" height=\"16\" fill=\"none\" stroke=\"var(--red)\" stroke-width=\"2\" style=\"vertical-align:middle;margin-right:4px;\"><path d=\"M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z\"/><polyline points=\"9 22 9 12 15 12 15 22\"/></svg>杨梅竹斜街'"),
    
    # Transport option categories
    ("category:'✈️ 往返机票'", "category:'<svg viewBox=\"0 0 24 24\" width=\"14\" height=\"14\" fill=\"none\" stroke=\"var(--red)\" stroke-width=\"2\" style=\"vertical-align:middle;margin-right:2px;\"><path d=\"M22 12l-4-4H6l-4 4M2 12h20\"/></svg>往返机票'"),
    ("category:'🚄 高铁/动车'", "category:'<svg viewBox=\"0 0 24 24\" width=\"14\" height=\"14\" fill=\"none\" stroke=\"var(--red)\" stroke-width=\"2\" style=\"vertical-align:middle;margin-right:2px;\"><rect x=\"1\" y=\"6\" width=\"22\" height=\"12\" rx=\"2\"/><line x1=\"6\" y1=\"18\" x2=\"6\" y2=\"20\"/><line x1=\"18\" y1=\"18\" x2=\"18\" y2=\"20\"/></svg>高铁/动车'"),
    ("category:'🚇 机场交通'", "category:'<svg viewBox=\"0 0 24 24\" width=\"14\" height=\"14\" fill=\"none\" stroke=\"var(--red)\" stroke-width=\"2\" style=\"vertical-align:middle;margin-right:2px;\"><rect x=\"4\" y=\"4\" width=\"16\" height=\"16\" rx=\"2\"/><line x1=\"4\" y1=\"12\" x2=\"20\" y2=\"12\"/></svg>机场交通'"),
    ("category:'🚌 机场交通'", "category:'<svg viewBox=\"0 0 24 24\" width=\"14\" height=\"14\" fill=\"none\" stroke=\"var(--red)\" stroke-width=\"2\" style=\"vertical-align:middle;margin-right:2px;\"><rect x=\"1\" y=\"6\" width=\"22\" height=\"12\" rx=\"2\"/><circle cx=\"6\" cy=\"18\" r=\"2\"/><circle cx=\"18\" cy=\"18\" r=\"2\"/></svg>机场交通'"),
    ("category:'🚕 机场交通'", "category:'<svg viewBox=\"0 0 24 24\" width=\"14\" height=\"14\" fill=\"none\" stroke=\"var(--red)\" stroke-width=\"2\" style=\"vertical-align:middle;margin-right:2px;\"><path d=\"M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z\"/><polyline points=\"14 2 14 8 20 8\"/></svg>机场交通'"),
    ("category:'🚌 旅游专线'", "category:'<svg viewBox=\"0 0 24 24\" width=\"14\" height=\"14\" fill=\"none\" stroke=\"var(--red)\" stroke-width=\"2\" style=\"vertical-align:middle;margin-right:2px;\"><rect x=\"1\" y=\"6\" width=\"22\" height=\"12\" rx=\"2\"/><circle cx=\"6\" cy=\"18\" r=\"2\"/><circle cx=\"18\" cy=\"18\" r=\"2\"/></svg>旅游专线'"),
    ("category:'🚕 包车/打车'", "category:'<svg viewBox=\"0 0 24 24\" width=\"14\" height=\"14\" fill=\"none\" stroke=\"var(--red)\" stroke-width=\"2\" style=\"vertical-align:middle;margin-right:2px;\"><path d=\"M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z\"/><polyline points=\"14 2 14 8 20 8\"/></svg>包车/打车'"),
    ("category:'🚇 市内交通'", "category:'<svg viewBox=\"0 0 24 24\" width=\"14\" height=\"14\" fill=\"none\" stroke=\"var(--red)\" stroke-width=\"2\" style=\"vertical-align:middle;margin-right:2px;\"><rect x=\"4\" y=\"4\" width=\"16\" height=\"16\" rx=\"2\"/><line x1=\"4\" y1=\"12\" x2=\"20\" y2=\"12\"/></svg>市内交通'"),
    ("category:'🚕 市内交通'", "category:'<svg viewBox=\"0 0 24 24\" width=\"14\" height=\"14\" fill=\"none\" stroke=\"var(--red)\" stroke-width=\"2\" style=\"vertical-align:middle;margin-right:2px;\"><path d=\"M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z\"/><polyline points=\"14 2 14 8 20 8\"/></svg>市内交通'"),
    ("category:'🎫 交通卡'", "category:'<svg viewBox=\"0 0 24 24\" width=\"14\" height=\"14\" fill=\"none\" stroke=\"var(--red)\" stroke-width=\"2\" style=\"vertical-align:middle;margin-right:2px;\"><rect x=\"2\" y=\"4\" width=\"20\" height=\"16\" rx=\"2\"/><line x1=\"2\" y1=\"10\" x2=\"22\" y2=\"10\"/></svg>交通卡'"),
    
    # Transport option icons (in icon field)
    ("icon:'🛫'", "icon:'<svg viewBox=\"0 0 24 24\" width=\"14\" height=\"14\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\"><path d=\"M22 12l-4-4H6l-4 4M2 12h20\"/></svg>'"),
    ("icon:'🛬'", "icon:'<svg viewBox=\"0 0 24 24\" width=\"14\" height=\"14\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\"><path d=\"M2 12l4-4h12l4 4M2 12h20\"/></svg>'"),
    ("icon:'🚄'", "icon:'<svg viewBox=\"0 0 24 24\" width=\"14\" height=\"14\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\"><rect x=\"1\" y=\"6\" width=\"22\" height=\"12\" rx=\"2\"/><line x1=\"6\" y1=\"18\" x2=\"6\" y2=\"20\"/><line x1=\"18\" y1=\"18\" x2=\"18\" y2=\"20\"/></svg>'"),
    ("icon:'🚇'", "icon:'<svg viewBox=\"0 0 24 24\" width=\"14\" height=\"14\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\"><rect x=\"4\" y=\"4\" width=\"16\" height=\"16\" rx=\"2\"/><line x1=\"4\" y1=\"12\" x2=\"20\" y2=\"12\"/></svg>'"),
    ("icon:'🚌'", "icon:'<svg viewBox=\"0 0 24 24\" width=\"14\" height=\"14\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\"><rect x=\"1\" y=\"6\" width=\"22\" height=\"12\" rx=\"2\"/><circle cx=\"6\" cy=\"18\" r=\"2\"/><circle cx=\"18\" cy=\"18\" r=\"2\"/></svg>'"),
    ("icon:'🚕'", "icon:'<svg viewBox=\"0 0 24 24\" width=\"14\" height=\"14\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\"><path d=\"M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z\"/><polyline points=\"14 2 14 8 20 8\"/></svg>'"),
    ("icon:'🎫'", "icon:'<svg viewBox=\"0 0 24 24\" width=\"14\" height=\"14\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\"><rect x=\"2\" y=\"4\" width=\"20\" height=\"16\" rx=\"2\"/><line x1=\"2\" y1=\"10\" x2=\"22\" y2=\"10\"/></svg>'"),
]

count = 0
import sys
sys.stdout.reconfigure(encoding='utf-8')
for old, new in replacements:
    if old in content:
        content = content.replace(old, new)
        count += 1
    else:
        print("NOT FOUND: " + str(old[:30].encode('unicode_escape')))

print(f"\nApplied {count} replacements")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Done!")
