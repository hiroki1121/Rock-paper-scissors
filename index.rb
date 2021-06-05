# ＜じゃんけんゲーム＞
# 間違った番号を入れた場合のループ
def validate(player_hand, hands)
  if player_hand < 0 || player_hand > 2
    loop{
      puts "0~2の番号を選択してください"
      puts "0.#{hands[0]} 1.#{hands[1]} 2.#{hands[2]}"
      player_hand = gets.chomp.to_i
      if player_hand >= 0 && player_hand <= 2
        break
      end
    }
  end
end

# 入力フォーム
  hands = ["グー","チョキ","パー"]
  puts "__________________________"
  puts "名前を入力してください"
  player_name = gets.chomp
  puts "0.#{hands[0]} 1.#{hands[1]} 2.#{hands[2]}"
  puts "0~2の番号を選択してください"
  player_hand = gets.chomp.to_i
  validate(player_hand, hands)
  puts "#{player_name}さんの選択された手は#{hands[player_hand]}です。"

  # コンピュータとの勝敗判定
  program_hand = rand(3)
  if player_hand == program_hand
    puts "コンピュータの手は#{hands[program_hand]}あいこです"
  elsif (player_hand == 0 && program_hand == 1) || (player_hand == 1 && program_hand == 2) || (player_hand == 2 && program_hand == 0)
    puts "コンピュータの手は#{hands[program_hand]}で#{player_name}さんの勝ちです"
  else 
    puts "コンピュータの手は#{hands[program_hand]}で#{player_name}さんの負けです"
  end
