import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html','r',encoding='utf-8') as f:
    content = f.read()

# SVG icon definitions for render functions
SVG = {
    'plane': '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" style="vertical-align:middle;"><path d="M22 12l-4-4H6l-4 4M2 12h20"/></svg>',
    'pin': '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" style="vertical-align:middle;"><circle cx="12" cy="10" r="3"/><path d="M12 2a8 8 0 0 0-8 8c0 5.4 8 12 8 12s8-6.6 8-12a8 8 0 0 0-8-8z"/></svg>',
    'food': '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" style="vertical-align:middle;"><path d="M18 8h1a4 4 0 0 1 0 8h-1M2 8h16v9a4 4 0 0 1-4 4H6a4 4 0 0 1-4-4V8z"/></svg>',
    'hotel': '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" style="vertical-align:middle;"><path d="M3 21h18M3 7v14M21 7v14M6 11h4v4H6zM14 11h4v4h-4zM9 3h6v4H9z"/></svg>',
    'ticket': '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" style="vertical-align:middle;"><rect x="2" y="4" width="20" height="16" rx="2"/><line x1="2" y1="10" x2="22" y2="10"/></svg>',
    'edit': '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" style="vertical-align:middle;"><path d="M12 20h9M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/></svg>',
    'trash': '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" style="vertical-align:middle;"><polyline points="3 6 5 6 21 6"/><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"/></svg>',
    'check': '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="#27AE60" stroke-width="2" style="vertical-align:middle;"><polyline points="20 6 9 17 4 12"/></svg>',
    'bulb': '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" style="vertical-align:middle;"><path d="M9 18h6M10 22h4M15.09 14c.18-.98.65-1.74 1.41-2.5A4.65 4.65 0 0 0 18 8 6 6 0 0 0 6 8c0 1 .23 2.23 1.5 3.5A4.61 4.61 0 0 1 8.91 14"/></svg>',
    'clock': '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" style="vertical-align:middle;"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>',
    'book': '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" style="vertical-align:middle;"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg>',
    'map': '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" style="vertical-align:middle;"><polygon points="1 6 1 22 8 18 16 22 23 18 23 2 16 6 8 2 1 6"/><line x1="8" y1="2" x2="8" y2="18"/><line x1="16" y1="6" x2="16" y2="22"/></svg>',
    'mic': '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" style="vertical-align:middle;"><path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z"/><path d="M19 10v2a7 7 0 0 1-14 0v-2"/><line x1="12" y1="19" x2="12" y2="23"/><line x1="8" y1="23" x2="16" y2="23"/></svg>',
    'plus': '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" style="vertical-align:middle;"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg>',
    'plate': '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" style="vertical-align:middle;"><circle cx="12" cy="10" r="7"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg>',
    'shop': '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" style="vertical-align:middle;"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>',
    'home': '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" style="vertical-align:middle;"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>',
    'thumbsup': '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" style="vertical-align:middle;"><path d="M14 9V5a3 3 0 0 0-3-3l-4 9v11h11.28a2 2 0 0 0 2-1.7l1.38-9a2 2 0 0 0-2-2.3zM7 22H4a2 2 0 0 1-2-2v-7a2 2 0 0 1 2-2h3"/></svg>',
    'calendar': '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" style="vertical-align:middle;"><rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>',
    'gallery': '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" style="vertical-align:middle;"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><polyline points="21 15 16 10 5 21"/></svg>',
    'doc': '<svg viewBox="0 0 24 24" width="36" height="36" fill="none" stroke="var(--text3)" stroke-width="1.5"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>',
    'sun': '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" style="vertical-align:middle;"><circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/></svg>',
    'moon': '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" style="vertical-align:middle;"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>',
    'cloud_sun': '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" style="vertical-align:middle;"><path d="M17.5 19H9a7 7 0 1 1 6.71-9h1.79a4.5 4.5 0 1 1 0 9z"/></svg>',
    'star': '<svg viewBox="0 0 24 24" width="14" height="14" fill="currentColor" stroke="none" style="vertical-align:middle;"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>',
    'phone': '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" style="vertical-align:middle;"><rect x="5" y="2" width="14" height="20" rx="2"/><line x1="12" y1="18" x2="12.01" y2="18"/></svg>',
    'warn': '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="#E65100" stroke-width="2" style="vertical-align:middle;"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>',
    'search': '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" style="vertical-align:middle;"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>',
    'warn_orange': '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="#F57C00" stroke-width="2" style="vertical-align:middle;"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>',
    'memo': '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" style="vertical-align:middle;"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>',
    'chat': '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" style="vertical-align:middle;"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>',
}

# Replacements in JS render functions
replacements = [
    # lock/unlock in mode toggle (textContent assignment)
    ("icon.textContent = '🔒'", f"icon.innerHTML = '{SVG['home']}'"),
    ("icon.textContent = '🔓'", f"icon.innerHTML = '{SVG['home']}'"),
    
    # InfoWindow content
    ("'<span style=\"color:#666;font-size:13px;\">⏱ ' + spot.duration + '</span>'", f"'<span style=\"color:var(--text2);font-size:13px;\">{SVG['clock']} ' + spot.duration + '</span>'"),
    ("'<div style=\"font-size:13px;color:#666;margin-bottom:10px;\">📍 ' + spot.address + '</div>'", f"'<div style=\"font-size:13px;color:var(--text2);margin-bottom:10px;\">{SVG['pin']} ' + spot.address + '</div>'"),
    
    # Panel list
    ("'✓已加入规划'", f"'{SVG['check']}已加入规划'"),
    
    # Detail page info rows
    ("'<span class=\"info-label\">📍 地址：</span>'", f"'<span class=\"info-label\">{SVG['pin']} 地址：</span>'"),
    ("'<span class=\"info-label\">🎫 预约：</span>'", f"'<span class=\"info-label\">{SVG['ticket']} 预约：</span>'"),
    
    # Detail intro
    ("'<div style=\"font-size:14px;font-weight:600;color:#7E57C2;margin-bottom:6px;\">📖 景点介绍</div>'", f"'<div style=\"font-size:14px;font-weight:600;color:var(--text);margin-bottom:6px;\">{SVG['book']} 景点介绍</div>'"),
    
    # Detail sections
    ("makeSection('🗺️'", f"makeSection('{SVG['map']}'"),
    ("makeSection('💡'", f"makeSection('{SVG['bulb']}'"),
    ("makeSection('🍜'", f"makeSection('{SVG['food']}'"),
    ("makeSection('🎤'", f"makeSection('{SVG['mic']}'"),
    
    # Add to plan button
    ("'➕ 加入行程规划'", f"'{SVG['plus']} 加入行程规划'"),
    
    # Food detail
    ("'🍽️ 美食简介'", f"'{SVG['plate']} 美食简介'"),
    ("'🏪</span><span class=\"section-header-text\">推荐店铺", f"'{SVG['shop']}</span><span class=\"section-header-text\">推荐店铺"),
    ("'🏠 ' + s.name + '</span>'", f"'{SVG['home']} ' + s.name + '</span>'"),
    ("'📍 ' + s.addr + '</div>'", f"'{SVG['pin']} ' + s.addr + '</div>'"),
    ("'👍 推荐：'", f"'{SVG['thumbsup']} 推荐：'"),
    ("'📅 添加到规划'", f"'{SVG['calendar']} 添加到规划'"),
    
    # Street detail
    ("'📍 街区简介'", f"'{SVG['pin']} 街区简介'"),
    ("'📍 地址'", f"'{SVG['pin']} 地址'"),
    ("'🖼️</span><span class=\"section-header-text\">街区图集", f"'{SVG['gallery']}</span><span class=\"section-header-text\">街区图集"),
    
    # Plan empty
    ("'📋</span><span class=\"plan-empty-text\">", f"'{SVG['doc']}</span><span class=\"plan-empty-text\">"),
    
    # Slot labels
    ("morning:'🌅 上午'", f"morning:'{SVG['sun']} 上午'"),
    ("noon:'☀️ 中午'", f"noon:'{SVG['sun']} 中午'"),
    ("afternoon:'🌤️ 下午'", f"afternoon:'{SVG['cloud_sun']} 下午'"),
    ("evening:'🌙 晚上'", f"evening:'{SVG['moon']} 晚上'"),
    ("hotel:'🏨 住宿'", f"hotel:'{SVG['hotel']} 住宿'"),
    ("transport:'✈️ 交通'", f"transport:'{SVG['plane']} 交通'"),
    
    # Slot memo
    ("'💬 ' + slot.memo + '</span>'", f"'{SVG['chat']} ' + slot.memo + '</span>'"),
    
    # Slot edit/remove
    ("')✏️</span>'", f"'){SVG['edit']}</span>'"),
    ("')×</span>'", "')<svg viewBox=\"0 0 24 24\" width=\"16\" height=\"16\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" style=\"vertical-align:middle;\"><line x1=\"18\" y1=\"6\" x2=\"6\" y2=\"18\"/><line x1=\"6\" y1=\"6\" x2=\"18\" y2=\"18\"/></svg></span>'"),
    
    # getSlotIcon function
    ("case 'spot': return '📍'", f"case 'spot': return '{SVG['pin']}'"),
    ("case 'food': return '🍜'", f"case 'food': return '{SVG['food']}'"),
    ("case 'hotel': return '🏨'", f"case 'hotel': return '{SVG['hotel']}'"),
    ("case 'transport': return '✈️'", f"case 'transport': return '{SVG['plane']}'"),
    ("case 'other': return '📌'", f"case 'other': return '{SVG['memo']}'"),
    ("default: return '📍'", f"default: return '{SVG['pin']}'"),
    
    # Day slot picker
    ("'📅 添加「' + shopName + '」到规划'", f"'{SVG['calendar']} 添加「' + shopName + '」到规划'"),
    ("label:'☀️ 上午'", f"label:'{SVG['sun']} 上午'"),
    ("label:'🌤️ 中午'", f"label:'{SVG['sun']} 中午'"),
    ("label:'🌅 下午'", f"label:'{SVG['cloud_sun']} 下午'"),
    ("label:'🌙 晚上'", f"label:'{SVG['moon']} 晚上'"),
    
    # Picker headers
    ("header = '📍 选择景点'", f"header = '{SVG['pin']} 选择景点'"),
    ("header = '🍜 选择美食/餐厅'", f"header = '{SVG['food']} 选择美食/餐厅'"),
    ("header = '🏨 选择住宿'", f"header = '{SVG['hotel']} 选择住宿'"),
    ("header = '✈️ 选择交通'", f"header = '{SVG['plane']} 选择交通'"),
    
    # Picker check marks
    ("'✓'", "''"), # remove all ✓ from picker checks (they'll be handled by CSS)
    
    # Star in hotel picker
    ("'★'.repeat(h.recScore)", f"'{SVG['star']}'.repeat(h.recScore)"),
    
    # Custom picker header
    ("'🏨 添加住宿（自定义）'", f"'{SVG['hotel']} 添加住宿（自定义）'"),
    ("'✏️ 添加自定义项目'", f"'{SVG['edit']} 添加自定义项目'"),
    
    # Geo search
    ("'🔍 正在查找位置...'", f"'{SVG['search']} 正在查找位置...'"),
    ("'⚠️ 地图未加载，可手动输入坐标'", f"'{SVG['warn']} 地图未加载，可手动输入坐标'"),
    ("'✅ 已定位：'", f"'{SVG['check']} 已定位：'"),
    ("'⚠️ 未找到位置，请手动输入坐标'", f"'{SVG['warn']} 未找到位置，请手动输入坐标'"),
    
    # Route marker
    ("fDom.innerHTML = '🍜'", f"fDom.innerHTML = '{SVG['food']}'"),
    
    # Transport render
    ("'<div class=\"section-title\">✈️ 宁波→北京</div>'", f"'<div class=\"section-title\">{SVG['plane']} 宁波→北京</div>'"),
    ("'🛫 宁波栎社 → 北京大兴'", f"'{SVG['plane']} 宁波栎社 → 北京大兴'"),
    ("'✅ 早班机中午前到不耽误行程'", f"'{SVG['check']} 早班机中午前到不耽误行程'"),
    ("'🛬 北京大兴 → 宁波栎社'", f"'{SVG['plane']} 北京大兴 → 宁波栎社'"),
    ("'✅ 晚班机白天可多玩半天'", f"'{SVG['check']} 晚班机白天可多玩半天'"),
    ("'<div class=\"section-title\">🛩️ 机场交通</div>'", f"'<div class=\"section-title\">{SVG['plane']} 机场交通</div>'"),
    ("'<span>🚇</span><span class=\"airport-text\">'", f"'<span>{SVG['pin']}</span><span class=\"airport-text\">'"),
    ("'<span>🚌</span><span class=\"airport-text\">'", f"'<span>{SVG['pin']}</span><span class=\"airport-text\">'"),
    ("'<span>🚕</span><span class=\"airport-text\">'", f"'<span>{SVG['pin']}</span><span class=\"airport-text\">'"),
    ("'<span>💡</span><span class=\"tip-text\">'", f"'<span>{SVG['bulb']}</span><span class=\"tip-text\">'"),
    ("'<div class=\"section-title\">🚇 市内交通</div>'", f"'<div class=\"section-title\">{SVG['pin']} 市内交通</div>'"),
    ("'📱 ' + c.tool + '</div>'", f"'{SVG['phone']} ' + c.tool + '</div>'"),
    ("'<div class=\"section-title\">⚠️ 避坑提示</div>'", f"'<div class=\"section-title\">{SVG['warn']} 避坑提示</div>'"),
    ("'<span class=\"warn-icon\">⚠️</span>'", f"'<span class=\"warn-icon\">{SVG['warn']}</span>'"),
    
    # Street render
    ("'📍 ' + s.addr + '</div>'", f"'{SVG['pin']} ' + s.addr + '</div>'"),
    ("'🏪 ' + shopPreview + (shopCount > 3 ? ' 等' : '') + '</div>'", f"'{SVG['shop']} ' + shopPreview + (shopCount > 3 ? ' 等' : '') + '</div>'"),
    
    # Budget icons
    ("icon:'✈️', preset:true },     { id:'hotel'", f"icon:'{SVG['plane']}', preset:true }},     {{ id:'hotel'"),
    ("icon:'🏨', preset:true },     { id:'ticket'", f"icon:'{SVG['hotel']}', preset:true }},     {{ id:'ticket'"),
    ("icon:'🎫', preset:true },     { id:'food'", f"icon:'{SVG['ticket']}', preset:true }},     {{ id:'food'"),
    ("icon:'🍜', preset:true },     { id:'transport'", f"icon:'{SVG['food']}', preset:true }},     {{ id:'transport'"),
    ("icon:'🚕', preset:true }", f"icon:'{SVG['pin']}', preset:true }}"),
    
    # Budget render edit/delete buttons
    ("ck=\"startEdit(' + index + ')\">✏️</button>'", f"ck=\"startEdit(' + index + ')\">{SVG['edit']}</button>'"),
    ("k=\"deleteItem(' + index + ')\">🗑️</button>'", f"k=\"deleteItem(' + index + ')\">{SVG['trash']}</button>'"),
    
    # Budget add custom item
    ("icon:'📝', preset:false });   saveBud", f"icon:'{SVG['memo']}', preset:false }});   saveBud"),
    
    # Budget reset
    ("icon:'✈️', preset:true },{ id:'hotel'", f"icon:'{SVG['plane']}', preset:true }},{{ id:'hotel'"),
    ("icon:'🏨', preset:true },{ id:'ticket'", f"icon:'{SVG['hotel']}', preset:true }},{{ id:'ticket'"),
    
    # Transport data (airport names)
    ("name:'✈️ 北京大兴国际机场'", f"name:'{SVG['plane']} 北京大兴国际机场'"),
    ("name:'✈️ 北京首都国际机场'", f"name:'{SVG['plane']} 北京首都国际机场'"),
]

count = 0
for old, new in replacements:
    if old in content:
        content = content.replace(old, new)
        count += 1

print(f"Applied {count} replacements")

# Also fix the { { issue from budget replacements
content = content.replace('}},     {{ id:', '},     { id:')
content = content.replace('}}},     {{ id:', '},     { id:')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Done!")
