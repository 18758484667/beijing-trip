import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add phone to key shops
# 四季民福
content = content.replace(
    "{name:'四季民福烤鸭店', addr:'南池子大街11号（故宫东门旁）', price:'约150元/人', recommend:'烤鸭、鸭架汤、芥末鸭掌', lat:39.9090, lng:116.4150}",
    "{name:'四季民福烤鸭店', addr:'南池子大街11号（故宫东门旁）', price:'约150元/人', recommend:'烤鸭、鸭架汤、芥末鸭掌', lat:39.9090, lng:116.4150, phone:'010-65267331', website:'https://www.sijiminfu.com'}")

# 南门涮肉
content = content.replace(
    "{name:'南门涮肉', addr:'安定门东大街56号', price:'约100元/人', recommend:'手切鲜羊肉、麻酱烧饼、百叶', lat:39.8820, lng:116.4080}",
    "{name:'南门涮肉', addr:'安定门东大街56号', price:'约100元/人', recommend:'手切鲜羊肉、麻酱烧饼、百叶', lat:39.8820, lng:116.4080, phone:'010-64017030'}")

# 聚宝源
content = content.replace(
    "{name:'聚宝源（牛街）', addr:'牛街西里商业1号楼', price:'约110元/人', recommend:'手切鲜羊肉、烧饼、羊尾油', lat:39.8930, lng:116.3720}",
    "{name:'聚宝源（牛街）', addr:'牛街西里商业1号楼', price:'约110元/人', recommend:'手切鲜羊肉、烧饼、羊尾油', lat:39.8930, lng:116.3720, phone:'010-63520556'}")

# 海碗居
content = content.replace(
    "{name:'海碗居', addr:'甘家口大厦B1层', price:'约45元/人', recommend:'炸酱面、炸灌肠、麻豆腐', lat:39.9400, lng:116.3700}",
    "{name:'海碗居', addr:'甘家口大厦B1层', price:'约45元/人', recommend:'炸酱面、炸灌肠、麻豆腐', lat:39.9400, lng:116.3700, phone:'010-88370973'}")

# 胡大饭馆
content = content.replace(
    "{name:'胡大饭馆', addr:'簋街233号', price:'约150元/人', recommend:'麻辣小龙虾、馋嘴蛙、烤鱼', lat:39.9400, lng:116.4300}",
    "{name:'胡大饭馆', addr:'簋街233号', price:'约150元/人', recommend:'麻辣小龙虾、馋嘴蛙、烤鱼', lat:39.9400, lng:116.4300, phone:'010-64045921'}")

# 护国寺小吃总店
content = content.replace(
    "{name:'护国寺小吃总店', addr:'护国寺大街93号', price:'约25元/人', recommend:'豌豆黄、艾窝窝、糖火烧、豆汁', lat:39.9350, lng:116.3800}",
    "{name:'护国寺小吃总店', addr:'护国寺大街93号', price:'约25元/人', recommend:'豌豆黄、艾窝窝、糖火烧、豆汁', lat:39.9350, lng:116.3800, phone:'010-66181705'}")

# 门框胡同百年卤煮
content = content.replace(
    "{name:'门框胡同百年卤煮', addr:'门框胡同19号（前门附近）', price:'约35元/人', recommend:'卤煮火烧、炸灌肠、麻豆腐', lat:39.9350, lng:116.4000}",
    "{name:'门框胡同百年卤煮', addr:'门框胡同19号（前门附近）', price:'约35元/人', recommend:'卤煮火烧、炸灌肠、麻豆腐', lat:39.9350, lng:116.4000, phone:'010-63033116'}")

# 姚记炒肝
content = content.replace(
    "{name:'姚记炒肝', addr:'鼓楼东大街311号', price:'约30元/人', recommend:'炒肝、卤煮、炸酱面', lat:39.9450, lng:116.3950}",
    "{name:'姚记炒肝', addr:'鼓楼东大街311号', price:'约30元/人', recommend:'炒肝、卤煮、炸酱面', lat:39.9450, lng:116.3950, phone:'010-84031525'}")

# 铁手咖啡
content = content.replace(
    "{name:'铁手咖啡制造局', addr:'五道营胡同61号', price:'约45元/人', recommend:'手冲咖啡、澳白、胡同露台', lat:39.9420, lng:116.4100}",
    "{name:'铁手咖啡制造局', addr:'五道营胡同61号', price:'约45元/人', recommend:'手冲咖啡、澳白、胡同露台', lat:39.9420, lng:116.4100, phone:'010-84028670'}")

# Add phone to spot data
# 故宫
content = content.replace(
    "reservation:'提前7天20:00在「故宫博物院」小程序抢票', lat:39.9163, lng:116.3972,",
    "reservation:'提前7天20:00在「故宫博物院」小程序抢票', lat:39.9163, lng:116.3972, phone:'010-85007421', website:'https://www.dpm.org.cn',")

# 颐和园
content = content.replace(
    "reservation:'提前1-7天在「颐和园」公众号预约，60岁以上老人免票', lat:39.9996, lng:116.2755,",
    "reservation:'提前1-7天在「颐和园」公众号预约，60岁以上老人免票', lat:39.9996, lng:116.2755, phone:'010-62881144', website:'https://www.summerpalace-china.com',")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Phone/website data added successfully')
