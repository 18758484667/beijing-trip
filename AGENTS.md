# 北京游旅游攻略小程序 / Web版

## 项目类型
- **微信小程序** (主项目) - `project.config.json` compileType: miniprogram, libVersion 3.7.1
- **Web单页应用** - `index.html` (含高德地图 + Supabase)

## 开发与预览
- **小程序**: 用微信开发者工具打开项目根目录 → 编译预览
- **Web版**: 直接用浏览器打开 `index.html`，或本地静态服务器 (`python -m http.server 8080`)

## 关键技术栈
| 层级 | 技术 |
|------|------|
| 小程序框架 | 原生微信小程序 (WXML/WXSS/JS) |
| Web地图 | 高德地图 JS API 2.0 (需Key) |
| 云存储/数据 | Supabase (index.html内直连) |
| 部署目标 | EdgeOne Pages (见 `.env`) |

## 项目结构
```
pages/           # 小程序5个Tab页 + 详情页
  index/         # 地图首页(景点)
  spot-detail/   # 景点详情
  food/          # 美食
  transport/     # 交通
  tips/          # 攻略
  budget/        # 预算
utils/data.js    # 静态数据(景点/美食/攻略等)
index.html       # Web版完整单页应用(含所有页面逻辑)
```

## 常用操作
- **新增页面**: 在 `pages/` 建目录 → 创建 `.js/.json/.wxml/.wxss` → 在 `app.json` 的 `pages` 数组注册
- **修改TabBar**: 改 `app.json` → `tabBar.list`
- **数据更新**: 改 `utils/data.js` (小程序端) 或 `index.html` 内 `DATA` 对象 (Web端)
- **Supabase配置**: `index.html` 顶部 `SUPABASE_URL` / `SUPABASE_KEY`

## 无以下工具链
- 无 package.json / npm scripts
- 无 ESLint / Prettier / TypeScript 配置
- 无单元测试框架
- 小程序代码直接在微信开发者工具中编译运行

## 注意事项
- 小程序 `appid` 为占位符 `wx0000000000000000`，发布前需替换真实 AppID
- Web版 `index.html` 内嵌高德Key和Supabase Key，**不要提交到公开仓库**
- 两端数据结构不完全同步，改动需双端维护