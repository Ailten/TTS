
# need :
# pip install soundfile sounddevice

# DEMO.

from TTS import *

voice = loadVoice('Axo')

phonetic_sylabs = sentenceToSylab(
    sanitizeSentence(
        'bonjour, comment ca va ?'
    )
)

playManyAudio(phonetic_sylabs, voice)
