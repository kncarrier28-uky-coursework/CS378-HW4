q = {
    'A' : 8.12,
    'B' : 1.49,
    'C' : 2.71,
    'D' : 4.32,
    'E' : 12.0,
    'F' : 2.30,
    'G' : 2.03,
    'H' : 5.92,
    'I' : 7.31,
    'J' : 0.10,
    'K' : 0.69,
    'L' : 3.98,
    'M' : 2.61,
    'N' : 6.95,
    'O' : 7.68,
    'P' : 1.82,
    'Q' : 0.11,
    'R' : 6.02,
    'S' : 6.28,
    'T' : 9.10,
    'U' : 2.88,
    'V' : 1.11,
    'W' : 2.09,
    'X' : 0.17,
    'Y' : 2.11,
    'Z' : 0.07
}

def findRepeatedSubstrings(cipher, length):
    repeatedSequences = {}
    for i in range(len(cipher) - length):
        substring = cipher[i:i+length]
        for j in range(i + 1, len(cipher ) - 3):
            if cipher[j:j+length] == substring:
                if substring in repeatedSequences.keys():
                    repeatedSequences[substring] += 1
                else:
                    repeatedSequences[substring] = 2
    return repeatedSequences

def findSpacing(cipher, substrings):
    spacing = {}
    for substring in substrings:
        spacing[substring] = []
        i = cipher.find(substring)
        while(i != -1):
            nextIndex = cipher.find(substring, i+1, len(cipher) - 1)
            if nextIndex != -1:
                spacing[substring].append(nextIndex - i)
            i = nextIndex
    return spacing

def createSet(dict):
    newSet = set()
    for key in dict:
        for item in dict[key]:
            newSet.add(item)
    return newSet

def factorDistances(distances):
    factors = []
    for value in distances:
        for i in range(2, 7):
            if value % i == 0:
                factors.append(i)
    return factors

def separateCipher(cipher, keyLength):
    separateStrings = []
    for i in range(keyLength):
        newString = ""
        for j in range(i, len(cipher) - 1, keyLength):
            newString += cipher[j]
        separateStrings.append(newString)
    return separateStrings

def calcFreqLetters(string):
    frequencies =  {
        'A' : 0,
        'B' : 0,
        'C' : 0,
        'D' : 0,
        'E' : 0,
        'F' : 0,
        'G' : 0,
        'H' : 0,
        'I' : 0,
        'J' : 0,
        'K' : 0,
        'L' : 0,
        'M' : 0,
        'N' : 0,
        'O' : 0,
        'P' : 0,
        'R' : 0,
        'Q' : 0,
        'S' : 0,
        'T' : 0,
        'U' : 0,
        'V' : 0,
        'W' : 0,
        'X' : 0,
        'Y' : 0,
        'Z' : 0
    }
    for i in range(len(string) - 1):
        frequencies[string[i].upper()] += 1
    return frequencies

def findMaximumK(string, q, p):
    alphabet = list(q)
    maxK = ""
    maxKValue = 0
    for k in range(26):
        sum = 0
        for i in range(26):
            sum += (q[alphabet[i]] * p[alphabet[(i + k) % 26]])
        if sum > maxKValue:
            maxK = alphabet[k]
            maxKValue = sum
    return maxK

def decryptVigenere(cipher, key):
    alphabet = list(q)
    plain = ""
    for i in range(len(cipher) - 1):
        plainIndex = (alphabet.index(cipher[i].upper()) - alphabet.index(key[i % len(key)])) % 26
        plain += alphabet[plainIndex]
    return plain

cipher = open("./vig2.txt").read().replace('\n', '')
repeats = findRepeatedSubstrings(cipher, 3)
print(repeats)
spacing = findSpacing(cipher, repeats)
print(spacing)
factors = factorDistances(createSet(spacing))
print(factors)

numberOccurence = {}
for factor in set(factors):
    numberOccurence[factor] = factors.count(factor)

print(numberOccurence)

# This can be used to test multiple key lengths. I removed it to save computational time since 4 was the most likely key length
# for factor in sorted(numberOccurence, key=numberOccurence.get, reverse=True):

sepCipher = separateCipher(cipher, 4)
likelyKey = []
for string in sepCipher:
    p = calcFreqLetters(string)
    likelyKey.append(findMaximumK(string, q, p))

print(likelyKey)

print(decryptVigenere(cipher, likelyKey))
