import requests

url = "https://pokeapi.co/api/v2/pokemon/"

print('ポケモン図鑑番号を入れてください')
# 入力文字を取得
poke_id = input('>> ')

# バリデーションチェック
while True:
    judge = 0 <= int(poke_id) < 1025

    if not judge:
        # 存在しないIDを記述したら、再入力を求める
        print('存在しないポケモンIDを入力しています！再度入力してください。')
        poke_id = input('>> ')

    else:
        # 正しければループを抜ける
        break

# urlに図鑑IDを付与
url = url + poke_id

response = requests.get(url)
response = response.json()

# 名前
name = response['name']
# ID
id = response['id']
# ポケモン画像
image = response['sprites']['front_default']
# タイプ
types = response['types'][0]['type']['name']

def get_pokemon_japanese_name(english_name):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{english_name.lower()}")
    if response.ok:
        data = response.json()
        
        for name_info in data['names']:
            if name_info['language']['name'] == 'ja-Hrkt':
                return name_info['name']
        return "日本語名が見つかりません。"
    else:
        return "ポケモンの情報を取得できませんでした。"
print(id)
print(name)
japanese_name = get_pokemon_japanese_name(name)
print(japanese_name)
print(image)
print(types)