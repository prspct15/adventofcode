
ROCK = 1
PAPER = 2
SCISSORS = 3

LOSS = 10
TIE = 20
WIN = 30

def main():
    with open('input.txt', 'r') as f:
        data = f.read().split("\n")

    print(p1(data))
    print(p2(data))
    
def p1(data):
    score = 0
    for line in data:
        char = line.split()
        leftMove = charToMove(char[0])
        rightMove = charToMove(char[1])
        moveScore = moveToScore(rightMove)
        if (leftMove == rightMove):
            score += 3 + moveScore
        elif (leftMove == ROCK and rightMove == SCISSORS) or (leftMove == PAPER and rightMove == ROCK) or (leftMove == SCISSORS and rightMove == PAPER):
            score += moveScore
        else:
            score += 6 + moveScore

    return score

def p2(data):
    score = 0
    for line in data:
        char = line.split()
        leftMove = charToMove(char[0])
        wantedOutcome = charToOutcome(char[1])

        if(wantedOutcome == LOSS):
            if(leftMove == ROCK):
                rightMove = SCISSORS
            elif(leftMove == PAPER):
                rightMove = ROCK
            elif(leftMove == SCISSORS):
                rightMove = PAPER
        elif(wantedOutcome == TIE):
            rightMove = leftMove
        elif(wantedOutcome == WIN):
            if(leftMove == ROCK):
                rightMove = PAPER
            elif(leftMove == PAPER):
                rightMove = SCISSORS
            elif(leftMove == SCISSORS):
                rightMove = ROCK
        
        moveScore = moveToScore(rightMove)
        if (leftMove == rightMove):
            score += 3 + moveScore
        elif (leftMove == ROCK and rightMove == SCISSORS) or (leftMove == PAPER and rightMove == ROCK) or (leftMove == SCISSORS and rightMove == PAPER):
            score += moveScore
        else:
            score += 6 + moveScore

    return score

def charToOutcome(char):
    if char == "X":
        return LOSS
    elif char == "Y":
        return TIE
    elif char == "Z":
        return WIN

def moveToScore(i):
    if i == ROCK:
        return 1
    elif i == PAPER:
        return 2
    elif i == SCISSORS:
        return 3

def charToMove(char):
    if char == "A" or char == "X":
        return ROCK
    elif char == "B" or char == "Y":
        return PAPER
    elif char == "C" or char == "Z":
        return SCISSORS

if __name__ == "__main__":
    main()
    