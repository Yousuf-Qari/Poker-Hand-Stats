import math
import card_tests
import time
import csv

def difference_finder(hand_probabilities, hand_percents, possible_hands):
    hand_differences = dict ()
    for (hand, prob,percent) in zip(possible_hands, hand_probabilities, hand_percents):
        difference = round ((math.fabs(hand_probabilities[prob]-hand_percents[percent])),4)
        hand_differences [hand]= difference
    return (hand_differences)

def percent_finder(iterations, hand_results, possible_hands):
    hand_percents = dict ()
    for hand in possible_hands:
        percent = round (((hand_results[hand]/iterations)*100),2)
        hand_percents [hand] = percent
    return (hand_percents)

def counter(current_count,iterations,possible_hands):
    hand_result = dict()
    while current_count < iterations :
        result = card_tests.main()
        # print (result + str(current_count))
        if result not in hand_result:
            hand_result[result] = 1
        elif result in hand_result:
            hand_result[result] += 1
        current_count += 1
    for hand in possible_hands:
        if hand not in hand_result:
            hand_result[hand] = 0
    # print (hand_result)
    return (hand_result)

def main():
    try:
        iterations = int(input('\nHow many times would you like to draw?\n'))
        current_count = 0
        possible_hands = ['high card', 'pair', 'two pairs', 'three of a kind', 'four of a kind', 'full house', 'flush',\
         'straight', 'straight flush']
        hand_results = counter(current_count, iterations, possible_hands)
        hand_percents = percent_finder (iterations, hand_results, possible_hands)

        hand_probabilities = dict()
        high_card_prob = round(float((1302540 / 2598960)*100),4)
        pair_prob = round(float((1098240 / 2598960)*100),4)
        two_pair_prob = round(float((123552 / 2598960)*100),4)
        three_prob = round(float((54912 / 2598960)*100),4)
        four_prob = round(float((624 / 2598960)*100),4)
        full_house_prob = round(float((3744 / 2598960)*100),4)
        flush_prob = round(float((5108 / 2598960)*100),4)
        straight_prob = round(float((10200 / 2598960)*100),4)
        straight_flush_prob = round(float((40 / 2598960)*100),4)
        probabilities = [high_card_prob, pair_prob, two_pair_prob, three_prob, four_prob,\
            full_house_prob, flush_prob, straight_prob, straight_flush_prob]
        separator = ','
        separator.join(possible_hands)
        hand_probabilities = dict(zip(possible_hands, probabilities))

        # print (hand_probabilities)

        hand_differences = difference_finder (hand_probabilities, hand_percents, possible_hands)

        file_name = input('Please name a file:')

        try:
            with open (file_name, 'w', newline='') as csv_file:
                fieldnames = ['Hand','Occurences','Percent','Expected','Difference']
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerow({'Hand' : possible_hands[0], 'Occurences': hand_results['high card'], 'Percent' : hand_percents['high card'],\
                'Expected' : hand_probabilities['high card'], 'Difference' : hand_differences['high card']})
                writer.writerow({'Hand' : possible_hands[1], 'Occurences': hand_results['pair'], 'Percent' : hand_percents['pair'],\
                'Expected' : hand_probabilities['pair'], 'Difference' : hand_differences['pair']})
                writer.writerow({'Hand' : possible_hands[2], 'Occurences': hand_results['two pairs'], 'Percent' : hand_percents['two pairs'],\
                'Expected' : hand_probabilities['two pairs'], 'Difference' : hand_differences['two pairs']})
                writer.writerow({'Hand' : possible_hands[3], 'Occurences': hand_results['three of a kind'], 'Percent' : hand_percents['three of a kind'],\
                'Expected' : hand_probabilities['three of a kind'], 'Difference' : hand_differences['three of a kind']})
                writer.writerow({'Hand' : possible_hands[4], 'Occurences': hand_results['four of a kind'], 'Percent' : hand_percents['four of a kind'],\
                'Expected' : hand_probabilities['four of a kind'], 'Difference' : hand_differences['four of a kind']})
                writer.writerow({'Hand' : possible_hands[5], 'Occurences': hand_results['full house'], 'Percent' : hand_percents['full house'],\
                'Expected' : hand_probabilities['full house'], 'Difference' : hand_differences['full house']})
                writer.writerow({'Hand' : possible_hands[6], 'Occurences': hand_results['flush'], 'Percent' : hand_percents['flush'],\
                'Expected' : hand_probabilities['flush'], 'Difference' : hand_differences['flush']})
                writer.writerow({'Hand' : possible_hands[7], 'Occurences': hand_results['straight'], 'Percent' : hand_percents['straight'],\
                'Expected' : hand_probabilities['straight'], 'Difference' : hand_differences['straight']})
                writer.writerow({'Hand' : possible_hands[8], 'Occurences': hand_results['straight flush'], 'Percent' : hand_percents['straight flush'],\
                'Expected' : hand_probabilities['straight flush'], 'Difference' : hand_differences['straight flush']})

            with open(file_name, 'r', newline= '') as csv_file:
                reader = csv.DictReader(csv_file)
                print ('{:<20} {:<10} {:<10} {:<10} {:<10}'.format('Hand','Occurences','Percent','Expected','Difference'))
                for row in reader:
                    formatted = "{:<20} {:<10} {:<10} {:<10} {:<10}"
                    print (formatted.format (row['Hand'],row['Occurences'],row['Percent'],row['Expected'],row['Difference']))
            csv_file.close()
        except PermissionError:
            print("Cannot open file for writing")
    except ValueError:
        print ('Please print a whole number')


if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()-start_time
    print('--- {} seconds ---'.format(end_time))