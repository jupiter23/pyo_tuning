from context import src
import time
from src.instrument import Instrument
from pyo import *

server = Server(duplex=0).boot()
equal_tuned_instrument = Instrument('equal')
natural_tuned_instrument = Instrument('natural')

intrument_outputs = []
intrument_outputs.append(equal_tuned_instrument.out())
intrument_outputs.append(natural_tuned_instrument.out())
mix = Mix(intrument_outputs, voices = 2, mul = 0.3, add = 0).out()

scale_chords = [(0, 'maj'), (2, 'min'), (4, 'min'), (5, 'maj'), (7, 'maj'), (9, 'min'), (11, 'dim')]
current_position = 0
duration = 2.6
play_natural_next = False
def alternately_play_chords_from_each_tuning():
    global scale_chords, current_position, play_natural_next, duration
    values_to_play = scale_chords[current_position % 7]
    scale_position = values_to_play[0]
    chord_name = values_to_play[1]
    if (play_natural_next == True):
        print 'Natual'
        play_chord_natural_tuning(chord_name, scale_position, duration)
        play_natural_next = False
        current_position += 1
    else:
        print 'Equal'
        play_chord_equal_tuning(chord_name, scale_position, duration)
        play_natural_next = True


def play_chord_natural_tuning(chord_name, scale_position, duration):
    natural_tuned_instrument.set_chord(chord_name, scale_position)
    natural_tuned_instrument.play(duration * 0.6)

def play_chord_equal_tuning(chord_name, scale_position, duration):
    equal_tuned_instrument.set_chord(chord_name, scale_position)
    equal_tuned_instrument.play(duration * 0.6)

chord_pattern = Pattern(alternately_play_chords_from_each_tuning, duration)
equal_tuning_chord_pattern = Pattern(play_chord_equal_tuning, duration)

chord_pattern.play()
server.gui(locals())
