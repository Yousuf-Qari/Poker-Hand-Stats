import playing_cards

def main():
    deck = playing_cards.build_deck()
    playing_cards.shuffle(deck)
    hand = []
    # print('\nHand dealt:\n')
    for card in range(len(deck)-47):
        card_dealt = deck[card]
        hand.append(card_dealt)
    # print (hand)
    hand_list = str('{0}\n{1}\n{2}\n{3}\n{4}')
    # print (hand_list.format(*hand))
    return (hand)

if __name__ == '__main__':
    main()

