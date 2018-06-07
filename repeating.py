from collections import defaultdict

input1 = '82156821568221'
input2 = '11111011110111011'
input3 = '98778912332145'
input4 = '124489903108444899'

inputs = [input1, input2, input3, input4]

def find_repeats(seq):
    sSeq = str(seq)
    length = len(seq)
    answer = defaultdict(int)

    for x in range(0, length - 1):
        for y in range(x+2, length + 1):
            answer[sSeq[x:y]] += 1
    print(answer)
    answered = ' '.join(x + ':' + str(y) for x,y in answer.items() if y > 1)
    if answered:
        return answered + '\n'
    return 0

# for i in inputs:
#     print(str(find_repeats(i)))
print(find_repeats(input1))