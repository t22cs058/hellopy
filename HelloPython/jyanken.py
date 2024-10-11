# import random

# class Janken:
#     def __init__(self):
#         # 0: グー, 1: チョキ, 2: パー
#         self.choices = ["グー", "チョキ", "パー"]

#     def get_hand(self):
#         # ランダムに 0, 1, 2 のどれかを返す
#         return random.randint(0, 2)

#     def determine_winner(self, hand_A, hand_B):
#         if hand_A == hand_B:
#             return "引き分け"
        
#         # 勝敗のルール
#         if (hand_A == 0 and hand_B == 1) or \
#            (hand_A == 1 and hand_B == 2) or \
#            (hand_A == 2 and hand_B == 0):
#             return "Aの勝ち"
#         else:
#             return "Bの勝ち"

# def play_janken_round(game):
#     hand_A = game.get_hand()
#     hand_B = game.get_hand()

#     # 手を数値から対応する名前に変換
#     hand_A_name = game.choices[hand_A]
#     hand_B_name = game.choices[hand_B]

#     # 結果を表示
#     print(f"Aの手: {hand_A_name} v.s. Bの手: {hand_B_name}", end=" → ")

#     result = game.determine_winner(hand_A, hand_B)
#     print(result)
#     return result

# def play_best_of_three():
#     game = Janken()
#     a_wins = 0
#     b_wins = 0

#     # 3回勝負
#     for i in range(3):
#         print(f"\nラウンド {i+1}:")
#         result = play_janken_round(game)
#         if result == "Aの勝ち":
#             a_wins += 1
#         elif result == "Bの勝ち":
#             b_wins += 1

#     # 最終結果
#     print("\n最終結果:")
#     if a_wins > b_wins:
#         print(f"Aの勝ち数: {a_wins}, Bの勝ち数: {b_wins} → Aが全体の勝者です！")
#     elif b_wins > a_wins:
#         print(f"Aの勝ち数: {a_wins}, Bの勝ち数: {b_wins} → Bが全体の勝者です！")
#     else:
#         print(f"Aの勝ち数: {a_wins}, Bの勝ち数: {b_wins} → 引き分けです！")

# # 使用例
# play_best_of_three()

import random
from collections import Counter

class Janken:
    def __init__(self):
        # 0: グー, 1: チョキ, 2: パー
        self.choices = ["グー", "チョキ", "パー"]

    def get_hand(self):
        # ランダムに 0, 1, 2 のどれかを返す
        return random.randint(0, 2)

    def determine_winner(self, hands):
        # 各手のカウントを取得
        count = Counter(hands)
        print(f"手のカウント: {count}")
        
        # 勝敗判定
        if len(count) == 1:
            # すべて同じ手なら引き分け
            return "引き分け"
        elif len(count) == 3:
            # 全員が違う手を出した場合も引き分け
            return "引き分け"
        else:
            # 2種類の手が出ている場合、どちらが勝ちかを判定
            if count[0] > 0 and count[1] > 0 and count[2] == 0:
                # グー vs チョキ → グーが勝ち
                return "グーを出したプレイヤーの勝ち"
            elif count[1] > 0 and count[2] > 0 and count[0] == 0:
                # チョキ vs パー → チョキが勝ち
                return "チョキを出したプレイヤーの勝ち"
            elif count[2] > 0 and count[0] > 0 and count[1] == 0:
                # パー vs グー → パーが勝ち
                return "パーを出したプレイヤーの勝ち"

def play_janken(players):
    game = Janken()
    hands = []

    # 各プレイヤーの手をランダムに生成
    for i in range(players):
        hand = game.get_hand()
        hands.append(hand)
        print(f"プレイヤー {i+1} の手: {game.choices[hand]}")
    
    # 勝敗を判定
    result = game.determine_winner(hands)
    print(f"結果: {result}")

# 使用例
num_players = int(input("プレイヤーの人数を入力してください: "))
play_janken(num_players)
