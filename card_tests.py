import deal_and_test

def is_pair (hand):
#should return true if there are exactly 2 hand of the same value
    face_list = []
    for a in range(len(hand)):
        card = hand[a]
        face_list.append(card['face'])
    # print (face_list)
    face_pair_list = dict()
    for face in face_list:
        if face not in face_pair_list:
            face_pair_list[face] = 1
        else:
            face_pair_list[face] += 1
    # print (face_pair_list)
    vals = face_pair_list.values()
    is_pair_list = []
    for value in vals:
        if value >= 2:
            is_pair_list.append(value)
    # print (is_pair_list)
    return len(is_pair_list) == 1 and is_pair_list[0] == 2

#count how many times it appears in list, if exactly 2 return false

def is_2_pair(hand):
# should return true if there is one set of 2 hand with a common value and a second set of 2 hand
#   with a different common value
    face_list = []
    for a in range(len(hand)):
        card = hand[a]
        face_list.append(card['face'])
    # print (face_list)
    face_pair_list = dict()
    for face in face_list:
        if face not in face_pair_list:
            face_pair_list[face] = 1
        else:
            face_pair_list[face] += 1
    # print (face_pair_list)
    vals = face_pair_list.values()
    is_pair_list = []
    for value in vals:
        if value == 2:
            is_pair_list.append(value)
    # print (is_pair_list)
    return len(is_pair_list) == 2

def is_3_of_a_kind(hand):
# returns true if there are exactly 3 hand with a common value
    face_list = []
    for a in range(len(hand)):
        card = hand[a]
        face_list.append(card['face'])
    # print (face_list)
    face_pair_list = dict()
    for face in face_list:
        if face not in face_pair_list:
            face_pair_list[face] = 1
        else:
            face_pair_list[face] += 1
    # print (face_pair_list)
    vals = face_pair_list.values()
    is_pair_list = []
    for value in vals:
        if value >= 3:
            is_pair_list.append(value)
        # print (is_pair_list)
        if len(is_pair_list) == 1:
            return is_pair_list[0] == 3
        else:
            return False

def is_4_of_a_kind(hand):
# returns true if there are exactly 4 hand with a common value
    face_list = []
    for a in range(len(hand)):
        card = hand[a]
        face_list.append(card['face'])
    # print (face_list)
    face_pair_list = dict()
    for face in face_list:
        if face not in face_pair_list:
            face_pair_list[face] = 1
        else:
            face_pair_list[face] += 1
    # print (face_pair_list)
    vals = face_pair_list.values()
    for value in vals:
        return 4 in vals

def is_full_house(hand): 
#returns true if there are 3 hand with a common value and the other hand share a different 
# common value
    face_list = []
    for a in range(len(hand)):
        card = hand[a]
        face_list.append(card['face'])
    # print (face_list)
    face_pair_list = dict()
    for face in face_list:
        if face not in face_pair_list:
            face_pair_list[face] = 1
        else:
            face_pair_list[face] += 1
    # print (face_pair_list)
    vals = face_pair_list.values()
    is_pair_list = []
    for value in vals:
        if value >=2:
            is_pair_list.append(value)
        # print (is_pair_list)
    if len(is_pair_list) == 2:
        if is_pair_list[0] == 3 and is_pair_list[1] == 2 or \
        is_pair_list[1] == 3 and is_pair_list[0] == 2:
            return True
        else:
                return False
    else:
        return False


def is_flush(hand):
#if the five hand all have the same suit
    value_list = []
    for a in range(len(hand)):
        card = hand[a]
        value_list.append(card['value'])
    for index in range(len(value_list)):
        if index == 0:
            first_value = (value_list[index])
            second_value = (value_list[index+1])
            third_value = (value_list[index+2])
            fourth_value = (value_list[index+3])
            fifth_value = (value_list[index+4])
            is_a_straight = (first_value + 1) == second_value and (first_value + 2) == third_value \
                and (first_value + 3) == fourth_value and (first_value + 4) == fifth_value
    suit_list = []
    for a in range(len(hand)):
        card = hand[a]
        suit_list.append(card['suit'])
    # print (suit_list)
    five_suit_list = dict()
    for face in suit_list:
        if face not in five_suit_list:
            five_suit_list[face] = 1
        else:
            five_suit_list[face] += 1
    # print (five_suit_list)
    vals = five_suit_list.values()
    is_pair_list = []
    for value in vals:
        if value == 5:
            is_pair_list.append(value)
        # print (is_pair_list)
        if len(is_pair_list) == 1:
            is_a_flush = is_pair_list[0] == 5
        else:
            return False
    if is_a_flush == True and is_a_straight != True:
        return True
    else:
        return False
    

def is_straight(hand): 
# returns true if the value of the five hand form a sequence which increases by 1 in each case.
#  For instance (2,"hearts"). (3,"spades"), (4, "diamonds"), (5,"hearts"), (6,"clubs")
    value_list = []
    for a in range(len(hand)):
        card = hand[a]
        value_list.append(card['value'])
    for index in range(len(value_list)):
        if index == 0:
            first_value = (value_list[index])
            second_value = (value_list[index+1])
            third_value = (value_list[index+2])
            fourth_value = (value_list[index+3])
            fifth_value = (value_list[index+4])
            is_a_straight = (first_value + 1) == second_value and (first_value + 2) == third_value \
                and (first_value + 3) == fourth_value and (first_value + 4) == fifth_value
    suit_list = []
    for a in range(len(hand)):
        card = hand[a]
        suit_list.append(card['suit'])
    # print (suit_list)
    five_suit_list = dict()
    for face in suit_list:
        if face not in five_suit_list:
            five_suit_list[face] = 1
        else:
            five_suit_list[face] += 1
    # print (five_suit_list)
    vals = five_suit_list.values()
    is_pair_list = []
    for value in vals:
        if value == 5:
            is_pair_list.append(value)
        # print (is_pair_list)
        if len(is_pair_list) == 1:
            is_a_flush = is_pair_list[0] == 5
        else:
            return False
    
    if is_a_flush != True and is_a_straight == True:
        return True
    else:
        return False

def is_straight_flush(hand):
# returns true if the value of the five hand form a sequence which increases by 1 in each case 
# and each card has the same suit. 
# For instance (2,"hearts"). (3,"hearts"), (4, "hearts"), (5,"hearts"), (6,"hearts")')
    value_list = []
    for a in range(len(hand)):
        card = hand[a]
        value_list.append(card['value'])
    for index in range(len(value_list)):
        if index == 0:
            first_value = (value_list[index])
            second_value = (value_list[index+1])
            third_value = (value_list[index+2])
            fourth_value = (value_list[index+3])
            fifth_value = (value_list[index+4])
            (first_value + 1) == second_value and (first_value + 2) == third_value \
                and (first_value + 3) == fourth_value and (first_value + 4) == fifth_value
    suit_list = []
    for a in range(len(hand)):
        card = hand[a]
        suit_list.append(card['suit'])
    # print (suit_list)
    five_suit_list = dict()
    for face in suit_list:
        if face not in five_suit_list:
            five_suit_list[face] = 1
        else:
            five_suit_list[face] += 1
    # print (five_suit_list)
    vals = five_suit_list.values()
    is_pair_list = []
    for value in vals:
        if value == 5:
            is_pair_list.append(value)
        # print (is_pair_list)
        if len(is_pair_list) == 1:
            return (first_value + 1) == second_value and (first_value + 2) == third_value \
                and (first_value + 3) == fourth_value and (first_value + 4) == fifth_value and \
                    is_pair_list[0] == 5
        else:
            return False
    
def is_high_card (hand):
# should return true if there are no hand with matching faces, and the hand do not increase in 
# value (no straight) and do not have a matching suit (no flush). 
# This hand is also known as nothing.')
    if is_full_house != True and is_pair != True and is_2_pair != True and is_3_of_a_kind != True and is_4_of_a_kind!= True \
        and is_flush != True and is_straight != True and is_straight_flush != True:
        return True
    else:
        False


def main():
    hand = (deal_and_test.main())
    test_hand = (
    {'value': 9,'face': 9, 'suit': 'Diamonds'},
    {'value': 10,'face': 10, 'suit': 'Diamonds'},
    {'value': 9,'face': 9, 'suit': 'Diamonds'},
    {'value': 12,'face': 12, 'suit': 'Diamonds'},
    {'value': 13,'face': 13, 'suit': 'Diamonds'})
    # print(card)
    if (is_straight_flush(hand)):
        return('straight flush')
    elif is_pair(hand):
        return ('pair')
    elif (is_2_pair(hand)):
        return('two pairs')
    elif (is_3_of_a_kind(hand)):
        return('three of a kind')
    elif (is_4_of_a_kind(hand)):
        return('four of a kind')
    elif (is_full_house(hand)):
        return('full house')
    elif (is_flush(hand)):
        return('flush')
    elif (is_straight(hand)):
        return('straight')
    elif is_high_card(hand):
        return ('high card')

if __name__ == '__main__':
    main()
