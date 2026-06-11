import re
import os

# Read the file
filepath = r'd:\Documents\CodeBuddy Files\北京游\index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# SVG icon map for spot icons (used in DATA.spots)
spot_svg_map = {
    '🏯': '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="var(--red)" stroke-width="2"><path d="M3 21h18M5 21V7l7-4 7 4v14M9 21v-6h6v6M9 11h6"/></svg>',
    '🏛️': '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="var(--red)" stroke-width="2"><rect x="3" y="7" width="18" height="13" rx="1"/><line x1="8" y1="3" x2="8" y2="7"/><line x1="16" y1="3" x2="16" y2="7"/><line x1="3" y1="12" x2="21" y2="12"/></svg>',
    '🌄': '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="var(--red)" stroke-width="2"><path d="M17 10l-5 5-5-5"/><path d="M3 18h18"/><path d="M3 6h18"/></svg>',
    '🌳': '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="var(--red)" stroke-width="2"><circle cx="12" cy="12" r="5"/><path d="M12 2v4M12 18v4M4.22 4.22l2.83 2.83M16.97 16.97l2.83 2.83M2 12h4M18 12h4"/></svg>',
    '🎓': '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="var(--red)" stroke-width="2"><path d="M22 10l-10-5-10 5 10 5 10-5zM6 12v5c0 1.66 2.69 3 6 3s6-1.34 6-3v-5"/></svg>',
    '🌊': '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="var(--red)" stroke-width="2"><path d="M2 12c2-1 4-1 6 0s4 1 6 0 4-1 6 0M2 16c2-1 4-1 6 0s4 1 6 0 4-1 6 0M2 8c2-1 4-1 6 0s4 1 6 0 4-1 6 0"/></svg>',
    '🔔': '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="var(--red)" stroke-width="2"><path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9M13.73 21a2 2 0 0 1-3.46 0"/></svg>',
    '🏮': '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="var(--red)" stroke-width="2"><path d="M8 2h8M4 7h16M7 7v10a3 3 0 0 0 3 3h4a3 3 0 0 0 3-3V7M12 20v2"/></svg>',
    '🏘️': '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="var(--red)" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>',
    '⛩️': '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="var(--red)" stroke-width="2"><path d="M6 3h12M6 21h12M6 7h12M8 3l2 4M16 3l-2 4"/></svg>',
    '🏟️': '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="var(--red)" stroke-width="2"><ellipse cx="12" cy="12" rx="10" ry="6"/><path d="M2 12h20M12 6v12"/></svg>',
    '🔬': '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="var(--red)" stroke-width="2"><circle cx="12" cy="10" r="7"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg>',
}

# Food dish icons
food_svg_map = {
    '🦆': '<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="var(--red)" stroke-width="2"><path d="M18 8h1a4 4 0 0 1 0 8h-1M2 8h16v9a4 4 0 0 1-4 4H6a4 4 0 0 1-4-4V8z"/></svg>',
    '🍲': '<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="var(--red)" stroke-width="2"><circle cx="12" cy="10" r="7"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg>',
    '🥟': '<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="var(--red)" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>',
    '🍰': '<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="var(--red)" stroke-width="2"><path d="M12 2l10 6.5v7L12 22 2 15.5v-7L12 2z"/><path d="M2 9l10 6.5L22 9"/></svg>',
    '🍡': '<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="var(--red)" stroke-width="2"><circle cx="12" cy="4" r="2"/><circle cx="12" cy="12" r="2"/><circle cx="12" cy="20" r="2"/><line x1="12" y1="6" x2="12" y2="10"/><line x1="12" y1="14" x2="12" y2="18"/></svg>',
    '🍜': '<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="var(--red)" stroke-width="2"><circle cx="12" cy="10" r="7"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg>',
    '🥘': '<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="var(--red)" stroke-width="2"><circle cx="12" cy="10" r="7"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg>',
    '🍳': '<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="var(--red)" stroke-width="2"><circle cx="12" cy="12" r="3"/><path d="M12 2v7M12 15v7M4.93 4.93l4.24 4.24M14.83 14.83l4.24 4.24M2 12h7M15 12h7"/></svg>',
}

# Hotel icons
hotel_svg_map = {
    '🚇': '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="var(--red)" stroke-width="2"><rect x="4" y="4" width="16" height="16" rx="2"/><line x1="4" y1="12" x2="20" y2="12"/><line x1="12" y1="4" x2="12" y2="20"/></svg>',
    '🏮': '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="var(--red)" stroke-width="2"><path d="M8 2h8M4 7h16M7 7v10a3 3 0 0 0 3 3h4a3 3 0 0 0 3-3V7M12 20v2"/></svg>',
    '🏟️': '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="var(--red)" stroke-width="2"><ellipse cx="12" cy="12" rx="10" ry="6"/><path d="M2 12h20M12 6v12"/></svg>',
}

# Transport icons
transport_svg_map = {
    '🛫': '<svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 12l-4-4H6l-4 4M2 12h20"/></svg>',
    '🛬': '<svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2"><path d="M2 12l4-4h12l4 4M2 12h20"/></svg>',
    '🚄': '<svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2"><rect x="1" y="6" width="22" height="12" rx="2"/><line x1="6" y1="18" x2="6" y2="20"/><line x1="18" y1="18" x2="18" y2="20"/></svg>',
    '🚇': '<svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2"><rect x="4" y="4" width="16" height="16" rx="2"/><line x1="4" y1="12" x2="20" y2="12"/><line x1="12" y1="4" x2="12" y2="20"/></svg>',
    '🚌': '<svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2"><rect x="1" y="6" width="22" height="12" rx="2"/><circle cx="6" cy="18" r="2"/><circle cx="18" cy="18" r="2"/></svg>',
    '🚕': '<svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>',
    '🎫': '<svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2"><path d="M15 5v2M15 11v2M15 17v2M5 5h14a2 2 0 0 1 2 2v3a2 2 0 0 0 0 4v3a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-3a2 2 0 0 0 0-4V7a2 2 0 0 1 2-2z"/></svg>',
}

# Tips icons
tips_svg_map = {
    '👟': '<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2"><path d="M2 20h20M4 12h16M4 4h16"/></svg>',
    '📅': '<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>',
    '👶': '<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="8" r="5"/><path d="M3 21v-2a7 7 0 0 1 7-7h4a7 7 0 0 1 7 7v2"/></svg>',
    '☀️': '<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/></svg>',
    '🚫': '<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="4.93" y1="4.93" x2="19.07" y2="19.07"/></svg>',
    '📱': '<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2"><rect x="5" y="2" width="14" height="20" rx="2"/><line x1="12" y1="18" x2="12.01" y2="18"/></svg>',
    '💰': '<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2"><line x1="12" y1="1" x2="12" y2="23"/><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>',
}

# Spot tips icons (in tips array within each spot)
spot_tip_svg = {
    '💡': '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="#E74C3C" stroke-width="2"><path d="M9 18h6M10 22h4M15.09 14c.18-.98.65-1.74 1.41-2.5A4.65 4.65 0 0 0 18 8 6 6 0 0 0 6 8c0 1 .23 2.23 1.5 3.5A4.61 4.61 0 0 1 8.91 14"/></svg>',
    '🎒': '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="#E74C3C" stroke-width="2"><path d="M6 2L3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z"/><line x1="3" y1="6" x2="21" y2="6"/><path d="M16 10a4 4 0 0 1-8 0"/></svg>',
    '☂️': '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="#E74C3C" stroke-width="2"><path d="M23 12a11.05 11.05 0 0 0-22 0zm-5 7a3 3 0 0 1-6 0v-7"/></svg>',
    '🚶': '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="#E74C3C" stroke-width="2"><circle cx="12" cy="5" r="2"/><path d="M10 22l4-10-3-4-5 8"/><path d="M14 22l2-10"/></svg>',
    '🚕': '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="#E74C3C" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>',
    '🪪': '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="#E74C3C" stroke-width="2"><rect x="2" y="4" width="20" height="16" rx="2"/><line x1="2" y1="10" x2="22" y2="10"/></svg>',
    '🪑': '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="#E74C3C" stroke-width="2"><path d="M6 3h12M6 21h12M6 9h12M6 3l2 6M18 3l-2 6"/></svg>',
    '🌇': '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="#E74C3C" stroke-width="2"><path d="M17 18a5 5 0 0 0-10 0"/><line x1="12" y1="9" x2="12" y2="3"/></svg>',
    '🎫': '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="#E74C3C" stroke-width="2"><path d="M15 5v2M15 11v2M15 17v2M5 5h14a2 2 0 0 1 2 2v3a2 2 0 0 0 0 4v3a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-3a2 2 0 0 0 0-4V7a2 2 0 0 1 2-2z"/></svg>',
    '🚇': '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="#E74C3C" stroke-width="2"><rect x="4" y="4" width="16" height="16" rx="2"/><line x1="4" y1="12" x2="20" y2="12"/></svg>',
    '🚼': '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="#E74C3C" stroke-width="2"><circle cx="12" cy="8" r="5"/><path d="M3 21v-2a7 7 0 0 1 7-7h4a7 7 0 0 1 7 7v2"/></svg>',
    '📸': '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="#E74C3C" stroke-width="2"><path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z"/><circle cx="12" cy="13" r="4"/></svg>',
    '⏰': '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="#E74C3C" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>',
    '🚢': '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="#E74C3C" stroke-width="2"><path d="M2 21c.6.5 1.2 1 2.5 1 2.5 0 2.5-2 5-2 1.3 0 1.9.5 2.5 1 .6.5 1.2 1 2.5 1 2.5 0 2.5-2 5-2 1.3 0 1.9.5 2.5 1"/><path d="M2 18c.6.5 1.2 1 2.5 1 2.5 0 2.5-2 5-2s2.5 2 5 2 2.5-2 5-2 2.5 2 2.5 2"/></svg>',
    '📍': '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="#E74C3C" stroke-width="2"><circle cx="12" cy="10" r="3"/><path d="M12 2a8 8 0 0 0-8 8c0 5.4 8 12 8 12s8-6.6 8-12a8 8 0 0 0-8-8z"/></svg>',
    '📅': '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="#E74C3C" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/></svg>',
    '🚲': '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="#E74C3C" stroke-width="2"><circle cx="5.5" cy="17.5" r="4.5"/><circle cx="18.5" cy="17.5" r="4.5"/><path d="M15 6h3l3 9M5.5 17.5h4"/></svg>',
    '🌃': '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="#E74C3C" stroke-width="2"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>',
    '🛺': '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="#E74C3C" stroke-width="2"><rect x="1" y="6" width="22" height="12" rx="2"/><circle cx="6" cy="18" r="2"/><circle cx="18" cy="18" r="2"/></svg>',
    '🍺': '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="#E74C3C" stroke-width="2"><path d="M17 8h1a4 4 0 0 1 0 8h-1M2 8h16v9a4 4 0 0 1-4 4H6a4 4 0 0 1-4-4V8z"/></svg>',
    '🧭': '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="#E74C3C" stroke-width="2"><circle cx="12" cy="12" r="10"/><polygon points="16.24 7.76 14.12 14.12 7.76 16.24 9.88 9.88 16.24 7.76"/></svg>',
    '🌅': '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="#E74C3C" stroke-width="2"><path d="M17 18a5 5 0 0 0-10 0"/><line x1="12" y1="9" x2="12" y2="3"/></svg>',
    '🍢': '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="#E74C3C" stroke-width="2"><circle cx="12" cy="4" r="2"/><circle cx="12" cy="12" r="2"/><circle cx="12" cy="20" r="2"/></svg>',
    '☕': '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="#E74C3C" stroke-width="2"><path d="M18 8h1a4 4 0 0 1 0 8h-1M2 8h16v9a4 4 0 0 1-4 4H6a4 4 0 0 1-4-4V8z"/></svg>',
    '🍰': '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="#E74C3C" stroke-width="2"><path d="M12 2l10 6.5v7L12 22 2 15.5v-7L12 2z"/></svg>',
    '⛪': '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="#E74C3C" stroke-width="2"><path d="M3 21h18M5 21V7l7-4 7 4v14M9 21v-6h6v6"/></svg>',
    '🏛️': '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="#E74C3C" stroke-width="2"><rect x="3" y="7" width="18" height="13" rx="1"/></svg>',
    '🖋️': '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="#E74C3C" stroke-width="2"><path d="M12 20h9M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/></svg>',
    '🚠': '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="#E74C3C" stroke-width="2"><line x1="2" y1="22" x2="22" y2="22"/><path d="M6 22V4l12-2v20"/></svg>',
    '🚌': '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="#E74C3C" stroke-width="2"><rect x="1" y="6" width="22" height="12" rx="2"/><circle cx="6" cy="18" r="2"/><circle cx="18" cy="18" r="2"/></svg>',
    '🎿': '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="#E74C3C" stroke-width="2"><path d="M2 22h20M4 2l16 16M8 2l8 18"/></svg>',
    '🍽️': '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="#E74C3C" stroke-width="2"><path d="M18 8h1a4 4 0 0 1 0 8h-1M2 8h16v9a4 4 0 0 1-4 4H6a4 4 0 0 1-4-4V8z"/></svg>',
    '🙏': '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="#E74C3C" stroke-width="2"><path d="M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20zM12 6v6l4 2"/></svg>',
    '👶': '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="#E74C3C" stroke-width="2"><circle cx="12" cy="8" r="5"/><path d="M3 21v-2a7 7 0 0 1 7-7h4a7 7 0 0 1 7 7v2"/></svg>',
    '⛵': '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="#E74C3C" stroke-width="2"><path d="M2 21c.6.5 1.2 1 2.5 1 2.5 0 2.5-2 5-2s2.5 2 5 2 2.5-2 5-2 2.5 2 2.5 2"/></svg>',
    '🛒': '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="#E74C3C" stroke-width="2"><circle cx="9" cy="21" r="1"/><circle cx="20" cy="21" r="1"/><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"/></svg>',
    '⚠️': '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="#E74C3C" stroke-width="2"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>',
}

# Now build the mapping for DATA.spots icons
# We'll replace icon: '🏯' with icon:'spot-palace' etc and add a mapping function

# But wait - the existing approach of putting SVG directly in icon string is messy for rendering.
# Better approach: use short type strings and create a renderIcon function.

# Let's just replace emoji in DATA with simple HTML-safe text markers
# and add a JS function to convert them.

# Actually, the cleanest approach for this file:
# 1. Replace spot.icon emojis with short type codes
# 2. Add getSpotIconHTML(type) function
# 3. Replace all usages of spot.icon with getSpotIconHTML

# But that requires modifying every render point...
# Let me just batch-replace all emoji with their SVG equivalents directly.

all_icons = {}
all_icons.update(spot_svg_map)
all_icons.update(food_svg_map)
all_icons.update(hotel_svg_map)
all_icons.update(transport_svg_map)
all_icons.update(tips_svg_map)
all_icons.update(spot_tip_svg)

count = 0
for emoji, svg in all_icons.items():
    # Only replace when it's an icon property (icon:'...') or icon:"..."
    # We need to be careful not to replace emoji that appear in other contexts
    
    # Replace in icon: '...' pattern
    old = f"icon:'{emoji}'"
    new = f"icon:'{svg}'"
    if old in content:
        content = content.replace(old, new)
        count += 1
        count += 1
    
    # Replace in icon: "..." pattern  
    old2 = f'icon:"{emoji}"'
    new2 = f'icon:"{svg}"'
    if old2 in content:
        content = content.replace(old2, new2)
        count += 1

print(f"\nTotal replacements: {count}")

# Write back
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Done!")
