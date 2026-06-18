
# need :
# pip install soundfile sounddevice

# DEMO.

from TTS import *

voice = loadVoice('Cylia')

phonetic_sylabs = sentenceToSylab(
    sanitizeSentence(
        'Au clair matin'
        #'un brave garçon chantonne doucement'
        #'dans un vieux jardin près du fleuve'
        #'tandis que la pluie fine glisse'
        #'sur les toits gris de la ville.'
    )
)
print(''.join(phonetic_sylabs))

playManyAudio(phonetic_sylabs, voice)
