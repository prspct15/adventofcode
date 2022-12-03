
def part1(data):
    data = max([sum([int(j) for j in i.split()]) for i in data])
    print(data)
    
def part2(data):
    data = [sum([int(j) for j in i.split()]) for i in data]
    data.sort(reverse=True)
    data = sum(data[:3])
    print(data)

if __name__ == "__main__":
    with open('input.txt', 'r') as f:
            data = f.read().split('\n\n')
    part1(data)
    part2(data)
