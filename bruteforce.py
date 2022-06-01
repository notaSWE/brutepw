from tqdm import tqdm
import itertools, random, string, time

startTime = int(time.time())

alphabet = string.ascii_lowercase

def generateRandPw(charLength):
    outStr = ''
    while len(outStr) < charLength:
        outStr += random.choice(alphabet)
    return outStr

def bruteForce(pwToBrute):
    estimatedTime = int((alphabet.index(pwToBrute[0]) / len(alphabet)) * (len(alphabet) ** len(pwToBrute)))
    pwTuple = tuple(pwToBrute)
    charList = [[x for x in alphabet]] * len(pwToBrute)

    for combination in tqdm(itertools.product(*charList), total = estimatedTime):
        if combination == pwTuple:
            return combination

if __name__=="__main__":
    randPw = generateRandPw(6)
    print(f"Attempting to brute force {randPw}")
    result = bruteForce(randPw)
    endTime = int(time.time())
    print(f"Bruteforced password {result} in {endTime - startTime} seconds")
