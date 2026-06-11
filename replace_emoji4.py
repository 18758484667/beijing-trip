import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html','r',encoding='utf-8') as f:
    content = f.read()

# Each remaining emoji needs a specific replacement
# We'll do targeted string replacements based on the context from remaining_emoji.txt

# Helper SVG definitions
def svg(inner, w=16, h=16, stroke='currentColor', extra=''):
    return f'<svg viewBox="0 0 24 24" width="{w}" height="{h}" fill="none" stroke="{stroke}" stroke-width="2" style="vertical-align:middle;{extra}">{inner}</svg>'

SVG = {
    'pin': svg('<circle cx="12" cy="10" r="3"/><path d="M12 2a8 8 0 0 0-8 8c0 5.4 8 12 8 12s8-6.6 8-12a8 8 0 0 0-8-8z"/>'),
    'food': svg('<path d="M18 8h1a4 4 0 0 1 0 8h-1M2 8h16v9a4 4 0 0 1-4 4H6a4 4 0 0 1-4-4V8z"/>'),
    'hotel': svg('<path d="M3 21h18M3 7v14M21 7v14M6 11h4v4H6zM14 11h4v4h-4zM9 3h6v4H9z"/>'),
    'ticket': svg('<rect x="2" y="4" width="20" height="16" rx="2"/><line x1="2" y1="10" x2="22" y2="10"/>'),
    'edit': svg('<path d="M12 20h9M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/>'),
    'trash': svg('<polyline points="3 6 5 6 21 6"/><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"/>'),
    'check': svg('<polyline points="20 6 9 17 4 12"/>', stroke='#27AE60'),
    'check_white': svg('<polyline points="20 6 9 17 4 12"/>', stroke='#FFF'),
    'bulb': svg('<path d="M9 18h6M10 22h4M15.09 14c.18-.98.65-1.74 1.41-2.5A4.65 4.65 0 0 0 18 8 6 6 0 0 0 6 8c0 1 .23 2.23 1.5 3.5A4.61 4.61 0 0 1 8.91 14"/>'),
    'book': svg('<path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/>'),
    'map': svg('<polygon points="1 6 1 22 8 18 16 22 23 18 23 2 16 6 8 2 1 6"/><line x1="8" y1="2" x2="8" y2="18"/><line x1="16" y1="6" x2="16" y2="22"/>'),
    'mic': svg('<path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z"/><path d="M19 10v2a7 7 0 0 1-14 0v-2"/><line x1="12" y1="19" x2="12" y2="23"/><line x1="8" y1="23" x2="16" y2="23"/>'),
    'plus': svg('<line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/>'),
    'plate': svg('<circle cx="12" cy="10" r="7"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/>'),
    'shop': svg('<path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/>'),
    'home': svg('<path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/>'),
    'thumbsup': svg('<path d="M14 9V5a3 3 0 0 0-3-3l-4 9v11h11.28a2 2 0 0 0 2-1.7l1.38-9a2 2 0 0 0-2-2.3zM7 22H4a2 2 0 0 1-2-2v-7a2 2 0 0 1 2-2h3"/>'),
    'calendar': svg('<rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/>'),
    'gallery': svg('<rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><polyline points="21 15 16 10 5 21"/>'),
    'doc': svg('<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/>', 36, 36, 'var(--text3)'),
    'plane': svg('<path d="M22 12l-4-4H6l-4 4M2 12h20"/>'),
    'plane_arr': svg('<path d="M2 12l4-4h12l4 4M2 12h20"/>'),
    'train': svg('<rect x="1" y="6" width="22" height="12" rx="2"/><line x1="6" y1="18" x2="6" y2="20"/><line x1="18" y1="18" x2="18" y2="20"/>'),
    'metro': svg('<rect x="4" y="4" width="16" height="16" rx="2"/><line x1="4" y1="12" x2="20" y2="12"/>'),
    'bus': svg('<rect x="1" y="6" width="22" height="12" rx="2"/><circle cx="6" cy="18" r="2"/><circle cx="18" cy="18" r="2"/>'),
    'car': svg('<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/>'),
    'phone': svg('<rect x="5" y="2" width="14" height="20" rx="2"/><line x1="12" y1="18" x2="12.01" y2="18"/>'),
    'warn': svg('<path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/>'),
    'search': svg('<circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/>'),
    'chat': svg('<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>'),
    'memo': svg('<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/>'),
    'xmark': svg('<line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/>', stroke='#E74C3C'),
}

# Direct replacements based on remaining emoji
reps = [
    # ✓ (check mark) - line 1213
    ('✓已加入规划', f'{SVG["check"]}已加入规划'),
    
    # Detail page - 地址 (line 1257)
    ('<span class="info-label">📍 地址：</span>', f'<span class="info-label">{SVG["pin"]} 地址：</span>'),
    # 预约 (line 1257)
    ('<span class="info-label">🎫 预约：</span>', f'<span class="info-label">{SVG["ticket"]} 预约：</span>'),
    
    # 加入行程规划 (line 1291)
    ('➕ 加入行程规划', f'{SVG["plus"]} 加入行程规划'),
    
    # Food detail - 美食简介 (line 1337)
    ('🍽️ 美食简介', f'{SVG["plate"]} 美食简介'),
    
    # Food detail - 推荐店铺 (line 1341)
    ('<span class="section-header-icon">🏪</span><span class="section-header-text">推荐店铺', f'<span class="section-header-icon">{SVG["shop"]}</span><span class="section-header-text">推荐店铺'),
    
    # Food detail - shop name (line 1347) 
    ('🏠 \' + s.name + \'', f'{SVG["home"]} \' + s.name + \''),
    
    # Food detail - shop addr (line 1350)
    ('📍 \' + s.addr + \'', f'{SVG["pin"]} \' + s.addr + \''),
    
    # Food detail - 推荐 (line 1351)
    ('👍 推荐：\'', f'{SVG["thumbsup"]} 推荐：\''),
    
    # Food detail - 添加到规划 (line 1352)
    ('📅 添加到规划', f'{SVG["calendar"]} 添加到规划'),
    
    # Street detail - 街区简介 (line 1376)
    ('📍 街区简介', f'{SVG["pin"]} 街区简介'),
    # 地址 (line 1382)
    ('<div style="font-size:14px;font-weight:600;color:#333;margin-bottom:4px;">📍 地址</div>', f'<div style="font-size:14px;font-weight:600;color:#333;margin-bottom:4px;">{SVG["pin"]} 地址</div>'),
    
    # Street detail - 推荐店铺 (line 1387)
    ('<span class="section-header-icon">🏪</span><span class="section-header-text">推荐店铺（', f'<span class="section-header-icon">{SVG["shop"]}</span><span class="section-header-text">推荐店铺（'),
    
    # Street detail - shop name (line 1393)
    # Already handled above
    
    # Street detail - shop addr (line 1396)
    # Already handled above
    
    # Street detail - 推荐 (line 1397)
    # Already handled above
    
    # Street detail - 添加到规划 (line 1398)
    # Already handled above
    
    # Street detail - 街区图集 (line 1405)
    ('<span class="section-header-icon">🖼️</span><span class="section-header-text">街区图集', f'<span class="section-header-icon">{SVG["gallery"]}</span><span class="section-header-text">街区图集'),
    
    # Plan empty (line 1527)
    ('<span class="plan-empty-icon">📋</span>', f'<span class="plan-empty-icon">{SVG["doc"]}</span>'),
    
    # Slot memo (line 1561)
    ('💬 \' + slot.memo + \'', f'{SVG["chat"]} \' + slot.memo + \''),
    
    # Slot edit (line 1563)
    ('\')✏️</span>\'', f'\'){SVG["edit"]}</span>\''),
    
    # Geo search (line 1994)
    ('🔍 正在查找位置...', f'{SVG["search"]} 正在查找位置...'),
    # Geo error (line 1998)
    ('⚠️ 地图未加载，可手动输入坐标', f'{SVG["warn"]} 地图未加载，可手动输入坐标'),
    # Geo success (line 2012)
    ('✅ 已定位：\'', f'{SVG["check_white"]} 已定位：\''),
    # Geo error 2 (line 2014)
    ('⚠️ 未找到位置，请手动输入坐标', f'{SVG["warn"]} 未找到位置，请手动输入坐标'),
    
    # Street render addr (line 2392)
    ('📍 \' + s.addr + \'', f'{SVG["pin"]} \' + s.addr + \''),
    # Street render shops (line 2393)
    ('🏪 \' + shopPreview + (shopCount > 3 ? \' 等\' : \'\') + \'', f'{SVG["shop"]} \' + shopPreview + (shopCount > 3 ? \' 等\' : \'\') + \''),
    
    # Transport render (line 2406)
    ('<div class="section-title">✈️ 宁波→北京</div>', f'<div class="section-title">{SVG["plane"]} 宁波→北京</div>'),
    # Flight card airports (line 2408)
    ('🛫 宁波栎社 → 北京大兴', f'{SVG["plane"]} 宁波栎社 → 北京大兴'),
    # Flight check mark (line 2408)
    ('✅ 早班机中午前到不耽误行程', f'{SVG["check_white"]} 早班机中午前到不耽误行程'),
    # Return flight (line 2409)
    ('🛬 北京大兴 → 宁波栎社', f'{SVG["plane_arr"]} 北京大兴 → 宁波栎社'),
    # Return flight check (line 2409)
    ('✅ 晚班机白天可多玩半天', f'{SVG["check_white"]} 晚班机白天可多玩半天'),
    # Airport transport title (line 2411)
    ('<div class="section-title">🛩️ 机场交通</div>', f'<div class="section-title">{SVG["plane"]} 机场交通</div>'),
    
    # Airport row icons (lines 2414-2416)
    ('<span>🚇</span><span class="airport-text">', f'<span>{SVG["metro"]}</span><span class="airport-text">'),
    ('<span>🚌</span><span class="airport-text">', f'<span>{SVG["bus"]}</span><span class="airport-text">'),
    ('<span>🚕</span><span class="airport-text">', f'<span>{SVG["car"]}</span><span class="airport-text">'),
    # Airport tip (line 2417)
    ('<span>💡</span><span class="tip-text">', f'<span>{SVG["bulb"]}</span><span class="tip-text">'),
    
    # City transport title (line 2419)
    ('<div class="section-title">🚇 市内交通</div>', f'<div class="section-title">{SVG["metro"]} 市内交通</div>'),
    # City transport tool (line 2422)
    ('📱 \' + c.tool + \'', f'{SVG["phone"]} \' + c.tool + \''),
    
    # Warnings title (line 2424)
    ('<div class="section-title">⚠️ 避坑提示</div>', f'<div class="section-title">{SVG["warn"]} 避坑提示</div>'),
    # Warning item (line 2426)
    ('<span class="warn-icon">⚠️</span>', f'<span class="warn-icon">{SVG["warn"]}</span>'),
    
    # Budget default items
    ('icon:\'✈️\', preset:true },     { id:\'hotel\'', f'icon:\'{SVG["plane"]}\', preset:true }},     {{ id:\'hotel\''),
    ('icon:\'🏨\', preset:true },     { id:\'ticket\'', f'icon:\'{SVG["hotel"]}\', preset:true }},     {{ id:\'ticket\''),
    ('icon:\'🎫\', preset:true },     { id:\'food\'', f'icon:\'{SVG["ticket"]}\', preset:true }},     {{ id:\'food\''),
    ('icon:\'🍜\', preset:true },     { id:\'transport\'', f'icon:\'{SVG["food"]}\', preset:true }},     {{ id:\'transport\''),
    ('icon:\'🚕\', preset:true }', f'icon:\'{SVG["car"]}\', preset:true }}'),
    
    # Budget add custom item
    ('icon:\'📝\', preset:false });   saveBud', f'icon:\'{SVG["memo"]}\', preset:false }});   saveBud'),
    
    # Budget reset default
    ('icon:\'✈️\', preset:true },{ id:\'hotel\'', f'icon:\'{SVG["plane"]}\', preset:true }},{{ id:\'hotel\''),
    ('icon:\'🏨\', preset:true },{ id:\'ticket\'', f'icon:\'{SVG["hotel"]}\', preset:true }},{{ id:\'ticket\''),
]

# Also fix the {{ double braces from budget replacement
content = content.replace('}},     {{ id:', '},     { id:')
content = content.replace('}}},     {{ id:', '},     { id:')
content = content.replace('}},{{ id:', '},{ id:')
content = content.replace('}}});   saveBud', '});   saveBud')

count = 0
for old, new in reps:
    if old in content:
        content = content.replace(old, new)
        count += 1

print(f"Applied {count} replacements")

# Final check - find any remaining emoji
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

remaining = 0
for i, ch in enumerate(content):
    if is_emoji(ord(ch)):
        # Skip if inside SVG tag
        before = content[max(0,i-200):i]
        if '<svg' in before and '</svg' not in before:
            continue
        remaining += 1

print(f"Remaining emoji: {remaining}")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Done!")
