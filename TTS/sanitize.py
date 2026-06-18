
from unidecode import unidecode
import re

def sanitizeSentence(sentence: str) -> str:
    """
    Sanitize a string : replace accent / special char, and remove space before and after.
    """

    # sanitize space before and after.
    sentence = sentence.strip()

    # simplify phonetic sentence.
    sentence = replacePhonetic(sentence)

    # replace accent (and special char).
    sentence = unidecode(sentence)

    # replace upper char.
    sentence = sentence.lower()

    return sentence

def replacePhonetic(sentence: str) -> str:
    """
    Replace some phonetic sylab to other more generic.
    """

    sentence = re.sub(r'\b(les)\b', r'lai', sentence)  # words.
    sentence = re.sub(r'\b(est|es)\b', r'ai', sentence)

    #sentence = re.sub(r'([dstx])\b', '', sentence)
    sentence = re.sub(r'(tion)', 'sion', sentence)
    sentence = re.sub(r'(é|è|ez|ais|ait)', 'ai', sentence)
    sentence = re.sub(r'(er)\b', 'ai', sentence)
    sentence = re.sub(r'(e)([^un])', r'ai\2', sentence)
    sentence = re.sub(r'(en)', 'an', sentence)
    sentence = re.sub(r'(au)', 'o', sentence)

    sentence = re.sub(r'(ph)', 'f', sentence)  # ordered.
    sentence = re.sub(r'(sh)', 'ch', sentence)
    sentence = re.sub(r'(c)([^h])', r'k\2', sentence)
    sentence = re.sub(r'(ç)', 's', sentence)
    sentence = re.sub(r'(c)([ei])', r's\2', sentence)
    sentence = re.sub(r'(g)([ei])', r'j\2', sentence)
    sentence = re.sub(r'(qu)', 'k', sentence)
    sentence = re.sub(r'(eau)', 'au', sentence)
    sentence = re.sub(r'(oin|oing)', 'ouin', sentence)
    sentence = re.sub(r'(œu|oeu)', 'eu', sentence)
    sentence = re.sub(r'(ain|ein|im|aim|ym)', 'in', sentence)
    sentence = re.sub(r'(en|am|em)', 'an', sentence)
    sentence = re.sub(r'(om)', 'on', sentence)
    #sentence = re.sub(r'c(?=[aou])', 'k', sentence)  # need verify.
    #sentence = re.sub(r'(c(?=[eéiiy])|ç)', 's', sentence)  # need verify.
    #sentence = re.sub(r'g(?=[aou])', 'g', sentence)
    #sentence = re.sub(r'g(?=[eéiiy])', 'j', sentence)
    #sentence = re.sub(r'ge([aou])', r'j\1', sentence)
    #sentence = re.sub(r'(?<=[aeiouy])s(?=[aeiouy])', 'z', sentence)
    sentence = re.sub(r'\b(x)', 'gz', sentence)
    sentence = re.sub(r'(x)', 'ks', sentence)
    sentence = re.sub(r'(y)', 'i', sentence)
    sentence = re.sub(r'(.)\1+', r'\1', sentence)

    return sentence






