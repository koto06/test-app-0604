import random

# ダミーの選手名リスト（実在しそうな名前を50人分用意）
names = [
    "佐藤健", "鈴木大輔", "高橋翔", "田中優", "伊藤誠", "渡辺亮", "山本直樹", "中村悠斗", "小林大地", "加藤翼",
    "吉田航", "山田陸", "佐々木駿", "山口拓海", "松本健太", "井上悠真", "木村颯太", "林大和", "斎藤優斗", "清水悠人",
    "山崎蓮", "森大輝", "池田陽斗", "橋本颯", "阿部悠生", "石川大智", "山下悠真", "中島颯太", "小川大和", "前田陸斗",
    "藤田悠斗", "後藤颯", "岡田大輔", "村上健太", "遠藤陸", "青木翔", "坂本大地", "福田優", "西村大和", "太田陸斗",
    "三浦颯太", "藤井悠斗", "岡本大輝", "松田陸", "中野大智", "原田悠生", "田村大和", "竹内翔", "金子健太", "和田陸"
]

# 選手データ生成
runners = []
for name in names:
    age = random.randint(10, 50)
    time = round(random.uniform(9.56, 12.99), 2)
    runners.append({"name": name, "age": age, "time": time})

# タイムが良い順（昇順）に並び替え
runners_sorted = sorted(runners, key=lambda x: x["time"])

# 結果表示
print("順位 | 名前      | 年齢 | タイム(秒)")
print("-" * 30)
for i, runner in enumerate(runners_sorted, 1):
    print(f"{i:2d}位 | {runner['name']:8s} | {runner['age']:2d}歳 | {runner['time']:5.2f}")

# ファイル保存（必要なら）
# with open("runner100_result.txt", "w", encoding="utf-8") as f:
#     f.write("順位 | 名前      | 年齢 | タイム(秒)\n")
#     f.write("-" * 30 + "\n")
#     for i, runner in enumerate(runners_sorted, 1):
#         f.write(f"{i:2d}位 | {runner['name']:8s} | {runner['age']:2d}歳 | {runner['time']:5.2f}\n")