import random
import os
os.system('clear')
print("************************************************************************************************************************************************\n")
print("                                                     \033[4;37;40mWelcome to ""MASTERMIND!!""\033[0;37;40m \n")
print("**  Ready to play  **\n")
print("  Level-1(4 letter words)")
print("  Level-2(5 letter words)")
print("  Level-3(6 letter words)\n")
while True:
        try:
            level = int(input("  Choose level you would like play? (1,2,3): "))
            break
        except (ValueError, KeyError):
            print("  That is not a number\n")

def file_inclusion(level):
    if level == 1:
        return 'four_letters.txt'
    elif level == 2:
        return 'five_letters.txt'
    else:
        return 'six_letters.txt'

def word_selection():
    line = open(file_inclusion(level)).read().splitlines()
    s = random.choice(line)
    words = s.split()
    return (random.choice(words))
#print (true_word)

def read_words():
    return [word for line in open(file_inclusion(level), "r") for word in line.strip().split()]

def commonletters(a, b):
    return len(set(a) & set(b))

def list_change(comp_guess, matched, filter_list):
    changed_list = [x for x in filter_list if commonletters(comp_guess, x) == matched]
    #print(changed_list)
    return changed_list

def guess_selection(list_name):
    guess = random.choice(list_name)
    return guess

def switch_mode(level):
    return (level + 3)
    
print("\n  Computer has already choosen its word and now its your turn to choose\n")
print("  Hope you have done it\n")
confirm = input("  Press ""y"" for confirmation: ")
if confirm.lower() == "y":
    print("\n  Thank you! Don't forget your word!\n")
    true_word = word_selection()
    new_cw = true_word
    #print("true word: {}".format(true_word))
words = read_words()
filter_list = []
comp_guess = random.choice(words)
print("  My guess is {}\n".format(comp_guess))

ccount = 1
m = int(input("  How many letters in matched? "))
if m == switch_mode(level):
    print("\n  Is {} your word?\n".format(comp_guess))
    correct = input("  If yes enter 'y': ")
    if correct == 'y':
        os.system('clear')
        print("                                                                         \033[5;32;47mI won the game!!\033[0;37;40m\n")
        print("                                                                 I guessed your word in {} attempts!!\n".format(ccount))
        print("                                                                 For your information my word is {}\n".format(true_word))
        exit()
    else:
        filter_list = [x for x in filter_list if commonletters(comp_guess, x) == switch_mode(level)]
        #print(filter_list)
        #continue

filter_list = [x for x in words if commonletters(comp_guess, x) == m]

while True:
    try:
        player2_word = input("\n  Enter your guess: ")
        if len(player2_word) != len(comp_guess):
            print("\n  Please enter {} letter words\n".format(len(comp_guess)))
            continue

        new_pw = player2_word
        count = 0
        for ch in new_pw:
            if ch in new_cw:
                count += 1
                new_str = player2_word.replace(ch, "")
                new_cw = true_word.replace(ch, "")
                #print(new_str)
        print("\n  {} characters matched \n".format(count))
        if player2_word == true_word:
            print("                                                \033[5;32;47mEureka!! You have won the game!\033[0;37;40m\n")
            print("                                                          You guessed my word in {} attempts!!\n".format(ccount))
            break
        comp_guess = guess_selection(filter_list)
        ccount += 1
        print("  My guess is: {}\n".format(comp_guess))
        k = int(input("  How many letters matched?: "))
        if k < m:
            filter_list = list_change(comp_guess, k, filter_list)
            #print(filter_list)
            continue
        elif k == switch_mode(level):
            print("\n  Is {} your word?\n".format(comp_guess))
            correct = input("  If yes enter 'y': ")
            if correct == 'y':
                os.system('clear')
                print("                                                                         \033[5;32;47mI won the game!!\033[0;37;40m\n")
                print("                                                                     I guessed your word in {} attempts!!\n".format(ccount))
                print("                                                                     For your information my word is {}\n".format(true_word))
                break
            else:
                filter_list = [x for x in filter_list if commonletters(comp_guess, x) == switch_mode(level)]
                #print(filter_list)
                continue
        elif k > m:
            filter_list = list_change(comp_guess, k, filter_list)
            #print(filter_list)
            m = k
            continue

    except (ValueError):
     print("  That is not a word\n")
