from context import src
import time
from src.instrument import Instrument
from pyo import *

server = Server().boot()
initial_frequency = 440
equal_tuned_instrument = Instrument(tuning_type = 'equal', initial_root_tonality_frequency = initial_frequency)
natural_tuned_instrument = Instrument(tuning_type = 'natural', initial_root_tonality_frequency = initial_frequency)
#pythagorean_tuned_instrument = Instrument('pythagorean')

intrument_outputs = []
intrument_outputs.append(equal_tuned_instrument.out())
intrument_outputs.append(natural_tuned_instrument.out())
mix = Mix(intrument_outputs, voices = 2, mul = 0.5, add = 0).out()

chords = ['major_third']

chord_progression = 0
duration = 3
next_instrument_to_play = 'natural'
def alternate_between_instruments():
    global next_instrument_to_play, chord_progression, duration, chords
    chord_name = chords[chord_progression%len(chords)]
    if (next_instrument_to_play == 'natural'):
        print chord_name + ' - ' + 'natural tuning'
        natural_tuned_instrument.set_chord(chord_name)
        natural_tuned_instrument.play(duration * 0.5)
        next_instrument_to_play = 'equal'

    elif (next_instrument_to_play == 'equal'):
        print chord_name + ' - ' + 'equal tuning'
        equal_tuned_instrument.set_chord(chord_name)
        equal_tuned_instrument.play(duration * 0.5)
        next_instrument_to_play = 'natural'
        chord_progression += 1

alternance_pattern = Pattern(alternate_between_instruments, duration)

alternance_pattern.play()
server.gui(locals())
