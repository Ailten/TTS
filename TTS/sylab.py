
sylabs = {
    "a","i","o","u",
    "ai","eu", 
    "ou","oi",
    "on","an","in",

    "b","c","d","f","g",
    "j","k","l","m","n",
    "p","r","s","t","v","z",

    "ch",

    #"e",
    #"au",

    #"gn",
    #"ill",

    #"ph",
    #"qu",

    #"ui",
    #"y",

    #"oin",
    #"ion"

}

import re

def sentenceToSylab(sentence: str) -> list[str]:

    output = []

    sylabs_regex = { (sylab, re.compile(sylab+r'[^a-z]*')) for sylab in sylabs }

    i = 0
    while i < len(sentence):

        biger_match = None
        range_match = None
        for sylab_regex in sylabs_regex:
            sylab_match = sylab_regex[1].match(sentence, i)
            if sylab_match == None:
                continue
            if biger_match == None or len(sylab_regex[0]) > len(biger_match):
                biger_match = sylab_regex[0]
                range_match = sylab_match.group(0)

        if biger_match == None:
            raise Exception(f'can\'t find more sylab match at : "{sentence}"')
        
        output.append(biger_match)
        i += len(range_match)

    return output


