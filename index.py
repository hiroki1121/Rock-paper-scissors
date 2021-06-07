# ＜じゃんけんゲーム＞
import random
# 間違った番号を入れた場合のループ
def validate(player_hand, hands):
  if player_hand < 0 and player_hand > 2:
    while player_hand != 0 or player_hand != 1 or player_hand != 2:
      print ('0~2の番号を選択してください')
      player_hand = int(input(f'0.{hands[0]} 1.{hands[1]} 2.{hands[2]}'))
      if player_hand >= 0 and player_hand <= 2:
        break

# 入力フォーム
hands = ['グー','チョキ','パー']
print ('__________________________')
print ('名前を入力してください')
player_name = input('')
print (f"0.{hands[0]} 1.{hands[1]} 2.{hands[2]}")
print ('0~2の番号を選択してください')
player_hand = int(input(''))
validate(player_hand, hands)
print (f'{player_name}さんの選択された手は{hands[player_hand]}です。')

# コンピュータとの勝敗判定
program_hand = random.randint(0,2)
if player_hand == program_hand:
  print (f'コンピュータの手は{hands[program_hand]}あいこです')
elif (player_hand == 0 and program_hand == 1) or (player_hand == 1 and program_hand == 2) or (player_hand == 2 and program_hand == 0):
  print (f'コンピュータの手は{hands[program_hand]}で{player_name}さんの勝ちです')
else :
  print (f'コンピュータの手は{hands[program_hand]}で{player_name}さんの負けです')
