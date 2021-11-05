logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
import random

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  new_card = random.choice(cards)
  return new_card

def calculate_score(cards_log):
  if sum(cards_log) == 21 and len(cards_log) == 2:
    return 0
  if 11 in cards_log and sum(cards_log) > 21:
    cards_log.remove(11)
    cards_log.append(1)
  return sum(cards_log)

def compare(user_score, computer_score):
  if user_score == computer_score:
    return "Draw!"
  elif computer_score == 0:
    return "You lose! Opponent has a blackjack ♠️"
  elif user_score == 0:
    return "You win! You have a blackjack ♠️"
  elif user_score > 21:
    return "You lose! Score went over 21"
  elif computer_score > 21:
    return "You win! Opponent's score went over 21"
  elif user_score > computer_score:
    return "You win!"
  else:
    return "You lose!"

def play_game():
  is_game_over = False
  print(logo)
  user_cards = []
  computer_cards = []
  for _ in range(0, 2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")
    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      user_should_deal = input("Type 'y' to hit or 'n' to pass.: ")
      if user_should_deal == "y":
        user_cards.append(deal_card())
      else:
        is_game_over = True

  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(f"Your final hand: {user_cards}, your final score: {user_score}")
  print(f"Computer's final hand: {computer_cards}, computer's final score: {computer_score} ")
  print(compare(user_score, computer_score))

while input("Do you want to play a game of blackjack? Type 'y' or 'n': ") == 'y':
  play_game()

print("Goodbye.")