import random

class DeckOfCards:
    __cards = []
   
    SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
    RANKS = [
        "Ace",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "Jack",
        "Queen",
        "King",
    ]

    def __init__(self):
        self.create_deck()

    def create_deck(self):
        card_tuple = ()
        for suit in self.SUITS:
            for rank in self.RANKS:             #ranks are already sorted,  but supopse they weren't  
                card_tuple += (rank, suit)
                self.__cards.append(card_tuple)
               
    def shuffle_deck(self):
        random.shuffle(self.__cards)

    def deal_card(self):
        print()
        self.__cards.pop(0)
        print(self.__cards)

    # don't touch below this line

    def __str__(self):
        return f"The deck has {len(self.__cards)} cards"

