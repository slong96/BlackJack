"""
Sophanda Long.
The final assignment I decided to do
is the game blackjack.
"""

import random

print('Welcome to Blackjack!\n')

def main():

    # player and dealer
    player_in = True
    dealer_in = True

    # creating deck of cards
    deck = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K',
            'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K',
            'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K',
            'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']

    # creating player and dealer hand
    player_hand = []
    dealer_hand = []

    # dealing the cards
    # taking random cards from the deck
    def deal(turn):
        card = random.choice(deck)
        turn.append(card)
        deck.remove(card)

    # calculating the total of dealer hand and player hand
    def total(turn):
        total = 0
        # face cards that equals to 10
        face = ['J', 'Q', 'K']
        for card in turn:
            if card in range(1, 11):
                total += card
            elif card in face:
                total += 10
            else:
                # for the ACES
                if total > 11:
                    total += 1
                else:
                    total += 11
        return total

    # showing dealer hand
    def show_dealer_hand():
        if len(dealer_hand) == 2:
            return dealer_hand[0]
        elif len(dealer_hand) > 2:
            return dealer_hand[0], dealer_hand[1]

    # asking player to STAY or HIT
    # looping the game
    for _ in range(2):
        deal(dealer_hand)
        deal(player_hand)
    while player_in or dealer_in:
        print(f'Dealer has {show_dealer_hand()} and ?')
        print(f'You have {player_hand} = {total(player_hand)}')
        if player_in:
            stay_hit = input('Enter 1 to STAY\nEnter 2 to HIT\n1 or 2: ')
            print('\n')
        if total(dealer_hand) > 16:
            dealer_in = False
        else:
            deal(dealer_hand)
        if stay_hit == '1':
            player_in = False
        else:
            deal(player_hand)
        if total(player_hand) >= 21:
            break
        elif total(dealer_hand) >= 21:
            break

    # printing out the player hand, dealer hand, and winner
    if total(player_hand) == 21:
        print(f'\nYou have {player_hand} = {total(player_hand)}.')
        print(f'The dealer has {dealer_hand} = {total(dealer_hand)}.')
        print('Blackjack! You win!\n')
    elif total(dealer_hand) == 21:
        print(f'\nYou have {player_hand} = {total(player_hand)}.')
        print(f'The dealer has {dealer_hand} = {total(dealer_hand)}.')
        print('Blackjack! Dealer wins!\n')
    elif total(player_hand) > 21:
        print(f'\nYou have {player_hand} = {total(player_hand)}.')
        print(f'The dealer has {dealer_hand} = {total(dealer_hand)}.')
        print('You bust! Dealer wins!\n')
    elif total(dealer_hand) > 21:
        print(f'\nYou have {player_hand} = {total(player_hand)}.')
        print(f'The dealer has {dealer_hand} = {total(dealer_hand)}.')
        print('Dealer bust! You win!\n')
    elif 21 - total(dealer_hand) < 21 - total(player_hand):
        print(f'\nYou have {player_hand} = {total(player_hand)}.')
        print(f'The dealer has {dealer_hand} = {total(dealer_hand)}.')
        print('Dealer wins!\n')
    elif 21 - total(dealer_hand) > 21 - total(player_hand):
        print(f'\nYou have {player_hand} = {total(player_hand)}.')
        print(f'The dealer has {dealer_hand} = {total(dealer_hand)}.')
        print('You win!\n')

    # asking player if they want to continue
    restart = input('Play again? Enter y or n: ')
    if restart == 'y':
        print('\n')
        main()
    else:
        print('Thanks for playing!')
        exit()

# returning to the beginning
main()