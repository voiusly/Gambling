import random

class Blackjack:
    def __init__(self):
        self.balance = 100
        self.deck = [i for i in range(1, 12)] * 4

    def deal_card(self):
        return random.choice(self.deck)

    def calculate_hand(self, hand):
        if sum(hand) > 21 and 11 in hand:
            hand[hand.index(11)] = 1
        return sum(hand)

    def play_round(self):
        bet = int(input("Enter your bet (1-{}): ".format(self.balance)))
        if bet < 1 or bet > self.balance:
            print("Invalid bet. Please try again.")
            return

        player_hand = [self.deal_card(), self.deal_card()]
        dealer_hand = [self.deal_card(), self.deal_card()]

        print("Your hand: {} ({})".format(player_hand, self.calculate_hand(player_hand)))
        print("Dealer's up card: {} ({})".format([dealer_hand[0]], self.calculate_hand([dealer_hand[0]])))

        while True:
            action = input("Do you want to 'hit' or 'stand'? ")
            if action.lower() == 'hit':
                player_hand.append(self.deal_card())
                print("Your hand: {} ({})".format(player_hand, self.calculate_hand(player_hand)))
                print("Dealer's up card: {} ({})".format([dealer_hand[0]], self.calculate_hand([dealer_hand[0]])))
                if self.calculate_hand(player_hand) > 21:
                    print("You busted! Dealer wins.")
                    self.balance -= bet
                    return
            elif action.lower() == 'stand':
                break
            else:
                print("Invalid action. Please try again.")

        while self.calculate_hand(dealer_hand) < 17:
            dealer_hand.append(self.deal_card())

        print("Your hand: {} ({})".format(player_hand, self.calculate_hand(player_hand)))
        print("Dealer's hand: {} ({})".format(dealer_hand, self.calculate_hand(dealer_hand)))

        player_score = self.calculate_hand(player_hand)
        dealer_score = self.calculate_hand(dealer_hand)

        if dealer_score > 21:
            print("WINNER WINNER CHICKEN DINNER")
            self.balance += bet
        elif player_score > dealer_score:
            print("WINNER")
            self.balance += bet
        elif player_score < dealer_score:
            print("YOU LOSE")
            self.balance -= bet
        else:
            print("Push. Your bet is returned.")

        print("Your new balance: {}".format(self.balance))

    def play_game(self):
        while self.balance > 0:
            self.play_round()
        print("Your broke lol")

game = Blackjack()
game.play_game()

