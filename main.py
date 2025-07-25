import compute
import random

FILE = 'D:/aaWorkspace/Wordle Solver/dictionary.txt'
ANALYSIS = 'D:/aaWorkspace/Wordle Solver/output.txt'
filer = open(ANALYSIS, 'r')
filew = open(ANALYSIS, 'w')
dictionary = open(FILE, 'r')
lines = dictionary.readlines()
words = []
scores = []
words_probabilities = {}

for line in lines:
    line = line.strip()
    score = compute.computeScore(line)
    words.append(line)
    scores.append(score)

compute.sortScores(words, scores)

# Scorurile cuvintelor
#for i in range(len(words)):
 #   out.write(words[i] + ' ' + str(scores[i]) + '\n')

dictionary.close()

gray = set()
yellow = {}
green = set()
suggestion = ""

def deepSearch(gray, yellow, green):
    global suggestion
    i = 0
    
    while i < len(words):
        ok = 1
        currentWord = words[i]

        for letter in gray:
            if letter in currentWord:
                ok = 0
        
        for el in yellow:
            if el not in currentWord:
                ok = 0
            else:
                for pos in yellow[el]:
                    if currentWord[pos] == el:
                        ok = 0
        
        for tup in green:
            letter = tup[0]
            pos = tup[1]
            if currentWord[pos] != letter:
                ok = 0

        if ok == 0:
            words.pop(i)
            scores.pop(i)
            i -= 1 
        i += 1

    print(f"Candidate: {words[0]} with a score of {scores[0]}")
    suggestion = words[0]
    

def solve():
    global words, scores, gray, yellow, green, suggestion
    step = 1

    while step < 7:
        if not words:
            print("No more words available!")
            break

        if step == 1:
            randIndex = random.randint(0, 49)
            suggestion = words[randIndex]
            scoreSuggestion = scores[randIndex]
            print(f'Suggestion - {suggestion} with a score of {scoreSuggestion}')
        else:
            result = input("Enter result: ")
            i = 0

            if result == '22222':
                print(f'Congrats! The solution was {suggestion}')
                compute.computeAnalysis(words, step, filer, filew)
                break

            # daca o litera trece de la galben la verde o scoatem de la galben si o trecem la verde
            while i < 5:
                if result[i] == '0':
                    gray.add(suggestion[i])
                elif result[i] == '1':
                    if suggestion[i] not in yellow:
                        yellow[suggestion[i]] = [i]
                    else:
                        yellow[suggestion[i]].append(i)
                else:
                    if suggestion[i] in yellow:
                        yellow.pop(suggestion[i])
                    green.add((suggestion[i], i))

                i += 1
            deepSearch(gray, yellow, green)
        step += 1





print('Welcome to the Wordle solver - made by Tanase Stefan-Daniel')
print('How to use:')
print('1. Open a Wordle game in the browser')
print('2. Run this script')
print('3. The program will generate a first word suggestion')
print('4. Input this word into the Wordle game')
print('5. After submitting the word, enter the feedback from Wordle using:')
print('   - 0: Letter is not in the word (gray)')
print('   - 1: Letter is in the word but in the wrong position (yellow)')
print('   - 2: Letter is in the correct position (green)')
print('Example: 01002')
print('6. The program will generate the next best word based on the results')
print('7. Repeat the process until you solve the Wordle!')
print('Type START to begin:')

decision = input().strip().upper()

if decision == 'START':
    solve()
else:
    print('Please type START to begin.')
