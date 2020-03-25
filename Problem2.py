def blumBlumShub(p, q, seed, length):
    M = p * q
    sequence = str(getParity(seed))
    x = [seed]
    for i in range(1, length):
        x.append((x[i-1] ** 2) % M)
        sequence += str(getParity(x[i]))
    return sequence

def getParity(n):
    parity = 0
    while n:
        parity = ~parity
        n = n & (n - 1)
    return -parity

p = 1000003
q = 2001911
seed = 3
length = 100000

fourBitSequences = {
    '0000': 0,
    '0001': 0,
    '0010': 0,
    '0011': 0,
    '0100': 0,
    '0101': 0,
    '0110': 0,
    '0111': 0,
    '1000': 0,
    '1001': 0,
    '1010': 0,
    '1011': 0,
    '1100': 0,
    '1101': 0,
    '1110': 0,
    '1111': 0,
}

sequence = blumBlumShub(p, q, seed, length)
print("Generated pseudorandom sequence of length", length)

sum = 0
for i in range(length - 1000):
    subsequence = sequence[i:i+1000]
    count = 0
    for j in range(len(subsequence) - 1):
        if subsequence[j] == "0":
            count += 1
    sum += count

avg = sum / (length - 1000)
print("\nAverage number of zeros in 1000 bit subsequences:", avg)

for i in range(length - 3):
    subsequence = sequence[i:i+4]
    fourBitSequences[subsequence] += 1

print("\nFrequencies of each four bit sequence occuring:\n")
for seq in fourBitSequences:
    print(seq, ":", (fourBitSequences[seq] / (length - 3)) * 100, "%")
print("\n")
