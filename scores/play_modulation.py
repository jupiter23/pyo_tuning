from context import src
import time
from src.instrument import Instrument
from pyo import *

starting_tonality = 333
server = Server().boot()
natural_tuned_instrument = Instrument(tuning_type = 'natural', initial_root_tonality_frequency = starting_tonality)

intrument_outputs = []
intrument_outputs.append(natural_tuned_instrument.out())
mix = Mix(intrument_outputs, voices = 2, mul = 0.3, add = 0).out()

major_chords = [(0, 'maj'), (5, 'maj'), (7, 'maj'), (0, 'maj'), (5, 'maj'), (9, 'min')]
minor_chords = [(0, 'min'), (5, 'min'), (7, 'min'), (0, 'min'), (5, 'min'), (11, 'dim')]
chords_to_play = major_chords
current_position = 0
time_to_retune_instrument = 0
original_duration = 0.33
current_duration = original_duration

# Play a 1 - 4 - 5 progression twice in two alternating tonalities.
def play_chord():
    global major_chords, minor_chords, chords_to_play, current_position, play_chord_pattern, original_duration
    global current_duration, natural_tuned_instrument, starting_tonality, time_to_retune_instrument
    if (time_to_retune_instrument == 6):
        if (natural_tuned_instrument.get_root_tonality_frequency() == starting_tonality):
            natural_tuned_instrument.set_root_tonality_frequency(starting_tonality * (4.0/5))
            chords_to_play = minor_chords
        else:
            natural_tuned_instrument.set_root_tonality_frequency(starting_tonality)
            chords_to_play = major_chords
        time_to_retune_instrument = 0

    if (current_position % 3 == 2):
        current_duration = original_duration * 3
        play_chord_pattern.setTime(current_duration)
    else:
        current_duration = original_duration
        play_chord_pattern.setTime(current_duration)

    values_to_play = chords_to_play[current_position]
    scale_position = values_to_play[0]
    chord_name = values_to_play[1]
    play_chord_natural_tuning(chord_name, scale_position, current_duration)
    current_position = (current_position + 1) % 6
    time_to_retune_instrument = (time_to_retune_instrument + 1) % 7

def play_chord_natural_tuning(chord_name, scale_position, duration):
    natural_tuned_instrument.set_chord(chord_name, scale_position)
    natural_tuned_instrument.play(duration * 0.6)

play_chord_pattern = Pattern(play_chord, original_duration)
play_chord_pattern.play()
server.gui(locals())
