
# need :
# pip install soundfile sounddevice

# DEMO.

from TTS import *

voice = loadVoice('Axo')

phonetic_sylabs = sentenceToSylab(
    sanitizeSentence(
        #'bonjour, comment ca va ?'
        'et on fait tourner les serviettes'
    )
)

playManyAudio(phonetic_sylabs, voice)