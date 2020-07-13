import random
from collections import Counter



def main():
#someWords = Words you will be adding in the game.
    someWords = '''memory script file input output boolean integer loop html python java
pycharm coding programming software data computer virtual source command'''

    someWords = someWords.split(' ')
    word = random.choice(someWords)



    if __name__ == '__main__':
        print('Guess the word! HINT: words are programming and computer related')

        for i in word:
            print('_', end=' ')
        print()

        playing = True
        letterGuessed = ''
        chances = len(word) + 2 #Chances = length of the word characters plus 2.
        correct = 0
        flag = 0
        try:
            while (chances != 0) and flag == 0:
                print()
                chances -= 1

                try:
                    guess = str(input('Enter a letter to guess: '))
                except:
                    print('Enter only a letter!')
                    continue

                if not guess.isalpha():
                    print('Enter only a LETTER')
                    continue
                elif len(guess) > 1:
                    print('Enter only ONE letter')
                    continue
                elif guess in letterGuessed:
                    print('You have already guessed that letter')
                    continue

                if guess in word:
                    k = word.count(guess)
                    for _ in range(k):
                        letterGuessed += guess

                for char in word:
                    if char in letterGuessed and (Counter(letterGuessed) != Counter(word)):
                        print(char, end=' ')
                        correct +- 1
                    elif (Counter(letterGuessed) == Counter(word)):
                        print("The word is: ", end=' ')
                        print(word)
                        flag = 1
                        print('Congratulations, You Win!')
                        break
                        break
                    else:
                        print('_', end= ' ')

            if chances <= 0 and (Counter(letterGuessed) != Counter(word)):
                print()
                print('You Lose Jedi!')
                print('The Word was {}'.format(word))
        except KeyboardInterrupt:
            print()
            print('Bye!')
            exit()

    restart = input("Do you want to restart? [yes/no] >")
    if restart == 'yes':
        main()
    else:
        print('Thank you, Goodbye.')
        exit

main()