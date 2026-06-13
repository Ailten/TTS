
import soundfile
import sounddevice

import os
from pathlib import Path


def loadVoice(voice_name: str) -> dict:
    """
    Load a dict of tuple ready to be played.
    """

    output = dict()

    voice_path = f'TTS/Voices/{voice_name}'

    for file in os.listdir(voice_path):
        sylab = Path(file).stem
        output[sylab] = soundfile.read(f'{voice_path}/{file}')

    return output


def playAnAudio(audio: tuple):
    """
    Play one audio (by sending a tuple loaded).
    """
    sounddevice.play(audio[0], audio[1])
    sounddevice.wait()


def playManyAudio(sylabs: list[str], audio_dico: dict[str, tuple]):
    """
    Play a list of sylabs (str), based on a dico audio (loaded).
    """
    for sylab in sylabs:
        audio_tuple = audio_dico.get(sylab)
        if audio_tuple == None:
            raise Exception(f'the Voice load has no audio file for the sylab : "{sylab}" !')
        playAnAudio(audio_dico[sylab])


    