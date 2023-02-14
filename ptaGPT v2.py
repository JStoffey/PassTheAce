"""
@version: 2
implemented passing the deck to the next player after the round

fix: last player in rotation needs to trade with the dealer, instead of the
first player in rotation
"""
import random

def pass_the_ace(players, deck):
    random.shuffle(deck)

    hands = {player: [] for player in players}
    for player in players:
        hands[player].append(deck.pop())
    dealer_card = deck.pop()

    for player in players:
        print(f"{player} has {hands[player][0]}")
    print(f"The dealer has {dealer_card}\n")

    for player in players:
        if hands[player][0] == 2:
            print(f"{player} has a King and is safe for this round.")
        else:
            print(f"{player} has the option to trade with the player to their left.")
            choice = input(f"{player}, do you want to trade? (yes/no)").lower()
            print("\n")
            if choice == "yes":
                left_player = players[(players.index(player) + 1) % len(players)]
                if hands[left_player][0] == 2:
                    print(f"{player} you cannot trade with {left_player} because they have a king.")
                else:
                    hands[player][0], hands[left_player][0] = hands[left_player][0], hands[player][0]
                    print(f"{player} traded with {left_player}")
        
        for player in players:
            print(f"{player} has {hands[player][0]}")
        print(f"The dealer has {dealer_card}\n")

    dealer_choice = input("Dealer, do you want to trade? (yes/no)").lower()
    if dealer_choice == "yes":
        dealer_card = deck.pop()
        print(f"The dealer drew a new card: {dealer_card}\n")

    max_card = max([max(hand) for hand in hands.values()])
    losers = [player for player, hand in hands.items() if max(hand) == max_card]
    for player in losers:
        print(f"{player} loses this round.")
    return losers

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] * 4
players = ["player1", "player2", "player3", "player4"]

while len(players) > 1:
    losers = pass_the_ace(players, deck)
    for player in losers:
        players.remove(player)
    players = players[1:] + [players[0]]
    deck = deck[1:] + [deck[0]]

print(f"{players[0]} is the winner!")