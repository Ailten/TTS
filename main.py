

# DEMO.

from TTS.sylab import sentenceToSylab
from TTS.sanitize import sanitizeSentence

print(
    sentenceToSylab(
        sanitizeSentence(
            'bonjour, ceci est un test !'
        )
    )
)