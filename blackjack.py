import random

class Deck_of_cards:
    def __init__(self):
        self.deck = []
        self.deck += 4 * ['A']
        for i in range(2,11):
            self.deck += 4 * [i]
        self.deck += 4 * ['J'] + 4 * ['Q'] + 4 * ['K'] 
    
    def draw(self):
        card = self.deck.pop(random.randint(0, len(self.deck)-1))
        return card

class Hand:
    def __init__(self, deck):
        self.hand = [deck.draw(), deck.draw()]
        
    def point_total(self):
        points = 0
        for i in range(len(self.hand)):
            if self.hand[i] == 'A':
                points += 11
            elif self.hand[i] in ['J','Q','K']:
                points += 10
            else:
                points += self.hand[i]
        if points > 21:
            for x in [x for x in self.hand if x == 'A']:
                if points > 21:
                    points -= 10
                else:
                    break
        return points
    
    def hit(self, deck):
        self.hand += [deck.draw()]

class Player_hand(Hand):
    def __init__(self, deck):
        Hand.__init__(self, deck)
        print(f'Your hand is: {self.hand}')

    def hit(self, deck):
        Hand.hit(self,deck)
        print(f'Your hand is: {self.hand}')
    
    def stand(self):
        print(f'Your final hand is: {self.hand}')

class Dealer_hand(Hand):
    def __init__(self, deck):
        Hand.__init__(self, deck)
        print(f"The dealer's hand is: ['?', {self.hand[1]}]")
        
    def show_hand(self):
        print(f"The dealer's hand is: {self.hand}")   

class Player:
    def __init__(self, balance):
        self.balance = balance
        self.amount_owed = balance

    def add_money(self, new_amt):
        self.balance += new_amt
        self.amount_owed += new_amt
    
    def show_balance(self):
        print(f'${self.balance}')

    def play_game(self):
        while True:
            if self.balance <= 0:
                print("You have no money. Use the 'add_money' function if you would like to add more to your balance.")
                break
            while True:
                bet = int(input('What would you like to wager? (only put the number, no $) '))
                if bet > self.balance:
                    print('Insufficent Funds. Try a lower wager.')
                else:
                    break
            deck = Deck_of_cards()
            print('We are using a new deck.')
            player_hand = Player_hand(deck)
            dealer_hand = Dealer_hand(deck)
            while True:
                if player_hand.point_total() == 21:
                    if dealer_hand.point_total() == 21:
                        print('Double blackjack! Tie.')
                        outcome = 'tie'
                        break
                    else:
                        print('Natural blackjack! You win!')
                        outcome = 'win'
                        break
                while True:
                    choice = input('Would you like to hit or stand? ')
                    choice = choice.strip()
                    choice = choice.lower()
                    if choice == 'hit' or choice == 'h':
                        player_hand.hit(deck)
                        if player_hand.point_total() > 21:
                            break
                    elif choice == 'stand' or choice == 's':
                        player_hand.stand()
                        break
                    else:
                        print('Input Error. Try again.')
                if player_hand.point_total() > 21:
                    print('Bust! You lose.')
                    outcome = 'loss'
                    break
                dealer_hand.show_hand()
                while dealer_hand.point_total() < player_hand.point_total():
                    dealer_hand.hit(deck)
                    dealer_hand.show_hand()
                if dealer_hand.point_total() == player_hand.point_total() and dealer_hand.point_total() < 17:
                    dealer_hand.hit(deck)
                    dealer_hand.show_hand()
                if dealer_hand.point_total() > 21:
                    print('Dealer busts! You win!')
                    outcome = 'win'
                    break
                if dealer_hand.point_total() > player_hand.point_total():
                    print(f"The dealer's {dealer_hand.hand} beats your {player_hand.hand}. You lose.")
                    outcome = 'loss'
                    break
                elif dealer_hand.point_total() == player_hand.point_total():
                    print(f"The dealer's {dealer_hand.hand} ties your {player_hand.hand}. You tie.")
                    outcome = 'tie'
                    break
                elif dealer_hand.point_total() < player_hand.point_total():
                    print(f"Your {player_hand.hand} beats the dealer's {dealer_hand.hand}. You win!")
                    outcome = 'win'
                    break
            if outcome == 'win':
                self.balance += bet
                print(f'You won ${bet}. Your new balance is ${self.balance}.')
            elif outcome == 'tie':
                print(f'You did not gain or loss anything. Your balance is ${self.balance}.')
            elif outcome == 'loss':
                self.balance -= bet
                print(f'You lost ${bet}. Your new balance is ${self.balance}.')
            break
            


