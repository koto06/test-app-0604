import random

# 日本国内の観光名所リスト
destinations = [
    "北海道・札幌", "青森・弘前城", "岩手・中尊寺", "宮城・松島", "秋田・角館", "山形・蔵王", "福島・会津若松",
    "東京・浅草寺", "神奈川・横浜中華街", "千葉・東京ディズニーリゾート", "埼玉・川越", "茨城・偕楽園", "栃木・日光東照宮", "群馬・草津温泉",
    "新潟・佐渡島", "富山・黒部ダム", "石川・兼六園", "福井・東尋坊", "山梨・富士山", "長野・松本城",
    "岐阜・白川郷", "静岡・伊豆", "愛知・名古屋城", "三重・伊勢神宮", "滋賀・彦根城", "京都・清水寺", "大阪・大阪城", "兵庫・姫路城", "奈良・東大寺", "和歌山・熊野古道",
    "鳥取・鳥取砂丘", "島根・出雲大社", "岡山・倉敷", "広島・厳島神社", "山口・角島大橋",
    "徳島・鳴門の渦潮", "香川・栗林公園", "愛媛・道後温泉", "高知・桂浜",
    "福岡・太宰府天満宮", "佐賀・吉野ヶ里遺跡", "長崎・グラバー園", "熊本・熊本城", "大分・別府温泉", "宮崎・高千穂峡", "鹿児島・桜島", "沖縄・首里城"
]

visited = set()

def pick_destination():
    available = [d for d in destinations if d not in visited]
    if not available:
        print("すべての観光地を訪れました！")
        return None
    choice = random.choice(available)
    visited.add(choice)
    return choice

if __name__ == "__main__":
    while True:
        dest = pick_destination()
        if dest is None:
            break
        print(f"今回の旅行先は: {dest}")
        ans = input("もう一度選びますか？（y/n）: ")
        if ans.lower() != "y":
            break