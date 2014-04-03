# Takes your input and gives you a result
# credit to http://www.dinodictionary.com/azdict_index.asp

from collections import Counter
import random

def say_hello(name):
    print "Hello %s!\nEnter a command or type 'exit' to leave forever."  % name

def parse(text, things):
    mf = most_frequent(text)
    try:
        thingy = random.choice(things[mf])
    except KeyError:
        thingy = 'Watermelon'
    print 'I say %s to that' %thingy

def most_frequent(string):
    if len(string) < 1:
        return
    chars = list(string)
    mf = Counter(chars).most_common()
    res = mf[0][0].lower()
    return res

def parse_dinos(dinos):
    dinodict = {None:'silly, you need to type something'}
    for dino in dinos:
        dino = dino.strip()
        if len(dino) < 1:
            continue
        key = dino[0].lower()
        val = dinodict.get(key, [])
        val.append(dino)
        dinodict[key] = val
    return dinodict


results = {}
with open('dinodict.txt','r') as dinofile:
    results = parse_dinos(dinofile)

say_hello(raw_input("Hi. I'm Bb. What's your name?  "))

text = raw_input('>')
while text != 'exit':
    parse(text, results)
    text = raw_input('>')