ANALYSIS = 'D:/aaWorkspace/Wordle Solver/output.txt'
filer = open(ANALYSIS, 'r')
filew = open(ANALYSIS, 'w')

scores = {
    'a': 7.99000, 'b': 1.60000, 'c': 3.83000, 'd': 3.82000, 'e': 10.16000,
    'f': 1.75000, 'g': 3.00000, 'h': 2.46000, 'i': 5.55000, 'j': 0.45000,
    'k': 1.92000, 'l': 4.82000, 'm': 3.00000, 'n': 5.75000, 'o': 6.52000,
    'p': 3.15000, 'q': 0.21000, 'r': 6.89000, 's': 7.98000, 't': 6.61000,
    'u': 3.63000, 'v': 1.02000, 'w': 1.21000, 'x': 0.28000, 'y': 1.89000,
    'z': 0.31000
}

def computeScore(word):
    p = 0
    unique = 1
    letters = {}
    for letter in word:
        p += scores[letter]
        
        if letter not in letters:
            letters[letter] = 1
        else:
            letters[letter] += 1
    
    # if the word has letter frequency = 1 the better the suggestion
    for letter in letters:
        if letters[letter] > 1:
            unique = 0
    if unique == 1:
        p += 10

    return round(p, 2)

def sortScores(words, scores):
    i = j = 0

    for i in range(len(words)-1):
        for j in range(i+1, len(words)):
            if scores[i] < scores[j]:
                aux = scores[i]
                scores[i] = scores[j]
                scores[j] = aux

                aux = words[i]
                words[i] = words[j]
                words[j] = aux

def computeAnalysis(words, curAtts, filer, filew):
    # Numarul mediu de incercari
    line = filer.readline().strip().split()
    attempts = int(line[0])
    totalRuns = int(line[1])

    totalRuns += 1
    attempts = round(float((curAtts + attempts) / 2), 2)
    filew.write(f"Average attempts 'til solution: {attempts} with a total of {totalRuns} attempts")

    filew.close()


filer.close()
filew.close()