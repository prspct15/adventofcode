def main():
    with open('input.txt', 'r') as f:
        data = f.read().split("\n")

    print(p1(data))
    print(p2(data))


def p1(data):
    score = 0
    for line in data:
        part1 = line[:len(line)//2]
        part2 = line[len(line)//2:]
        set1 = {charToScore(char) for char in part1}
        set2 = {charToScore(char) for char in part2}
        score += list(set1.intersection(set2))[0]

    return score
    
def p2(data):
    score = 0
    start = 0
    end = len(data)
    step = 3
    for i in range(start, end, step):
        slice = data[i:i+step]
        set1 = {charToScore(char) for char in slice[0]}
        set2 = {charToScore(char) for char in slice[1]}
        set3 = {charToScore(char) for char in slice[2]}
        score += list(set1.intersection(set2, set3))[0]
    return score


    
def charToScore(char):
    # return 1 for a, 26 for z, 27 for A and 52 for Z
    if(char.isalpha()):
        if(char.isupper()):
            return ord(char) - 64 + 26
        else:
            return ord(char) - 96



if __name__ == "__main__":
    main()

