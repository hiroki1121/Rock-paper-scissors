import random

GU, CHOKI, PA = 'グー', 'チョキ', 'パー'
HANDS = {'1': GU, '2': CHOKI, '3': PA}
STRONGER_THAN = {GU: PA, CHOKI: GU, PA: CHOKI}

def input_player_hand(name):
  hand = None
  while hand is None:
    print(f'番号を選択してください：(1:{GU}, 2:{CHOKI}, 3:{PA})')
    hand = HANDS.get(input())
    return hand

def main():
  print('__________________________')
  print('名前を入力してください')
  player_name = input()
  player_hand = input_player_hand(player_name)
  computer_hand = random.choice((GU, CHOKI, PA))
  print(F'{player_name}さんの選択された手は{player_hand}です。')
  if player_hand == computer_hand:
    print(f'コンピュータの手は{computer_hand}であいこです')
  elif player_hand == STRONGER_THAN[computer_hand]:
    print(f'コンピュータの手は{computer_hand}で{player_name}さんの勝ちです')
  else:
    print(f'コンピュータの手は{computer_hand}で{player_name}さんの負けです')

if __name__ == '__main__':
  main()