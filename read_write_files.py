import json

with open('./data/learning.txt', 'w') as f:
    f.write("Learning how to interact with files.\nPython is super interesting")
f.closed

with open('./data/learning.txt', 'r') as f:
    for line in f:
        print(line, end='')
f.closed

with open('./data/dump.json', 'w') as f:
    simple_list = ["hello", "world"]
    json.dump(simple_list, f)
f.closed

with open('./data/dump.json', 'r') as f:
    some_list = json.load(f)
    print('\n', some_list)
f.closed