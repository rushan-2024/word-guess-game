import random
name=input("What is Your Name : ")
print("Good Luck!",name)
words=['rainbow','computer','science','programming','python','mathematics','player',
       'condition','reverse','water','board','geeks','apple', 'river', 'train', 'cloud', 'ocean', 'music', 'light', 'glass', 'bread', 'tiger',
    'holiday', 'library', 'science', 'picture', 'diamond', 'journey', 'monster', 'country', 'weather', 'fiction',
    'astronaut', 'microscope', 'volcanoes', 'republican', 'algorithm', 'mysterious', 'electricity', 'discovery', 'adventure', 'philosophy',
    'python', 'java', 'android', 'laptop', 'firewall', 'internet', 'server', 'compile', 'debugger', 'function',
    'zombie', 'banana', 'jungle', 'pirate', 'wizard', 'dragon', 'rainbow', 'puzzle', 'bicycle', 'shadow']
word=random.choice(words)
print("Guess the Characters : ")
guesses=''
turns=12
while turns>0:
    failed=0
    for char in word:
        if char in guesses:
            print(char,end=' ')
        else:
            print("_",end=" ")
            failed+=1
    print()
    if failed==0:
        print("You Win")
        print("The Word is :",word)
        break
    guess=input("guess a chracter: ")
    guesses+=guess
    if guess not in word:
        turns-=1
        print("wrong")
        print("You have",turns,'more guesses')
    
    if turns ==0:
        print("You Lose!")
        print("The word was : ",word)


