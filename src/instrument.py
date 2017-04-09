from pyo import *
from scale import Scale
from chord import Chord

class Instrument():
    """
    Class which generates sounds from numerical frequency values.
    """

    def __init__(self, tuning_type = 'equal', initial_duration = 1, initial_root_tonality_frequency = 440):
        self.duration = initial_duration
        self.set_root_tonality_frequency(initial_root_tonality_frequency)
        self.scale = Scale().get_ratios(tuning_type)
        intervals = [0 for i in range(5)]
        self.synths = [self.synthesize(freq=(self.root_tonality_frequency * interval)) for interval in intervals]
        self.set_envelope(self.duration)
        self.chord_generator = Chord(self.scale, self.root_tonality_frequency)

    def out(self):
        mix = Mix(self.synths, voices = 2, mul = 0.7, add = 0)
        disto = Disto(mix, drive=0.01, slope=0.7, mul=self.envelope, add=0)
        verb = WGVerb(disto, feedback=0.5, cutoff=5000, bal=0.55, mul=1, add=0)
        return verb

    def set_root_tonality_frequency(self, frequency):
        self.root_tonality_frequency = frequency

    def get_root_tonality_frequency(self):
        return self.root_tonality_frequency

    def set_chord(self, chord_name = 'maj', scale_position = 1):
        self.chord_generator.set_root_frequency(self.scale[scale_position] * self.root_tonality_frequency)
        freqs = self.chord_generator.get_chord_frequencies(chord_name)
        number_of_frequencies_in_chord = len(freqs)
        for x in range(5):
            if ((x + 1) <= number_of_frequencies_in_chord):
                self.synths[x].setFreq(freqs[x])
            else:
                self.synths[x].setFreq(0)

    def play(self, duration):
        self.set_envelope_duration(duration)
        self.envelope.play()

    def set_envelope_duration(self, duration):
        if (self.duration == duration):
            return
        d = duration
        self.envelope.setDur(d)
        self.envelope.setAttack(d * .05)
        self.envelope.setDecay(d * .25)
        self.envelope.setSustain(d * .6)
        self.envelope.setRelease(d * .1)

    def set_envelope(self, duration):
        d = duration
        self.envelope = Adsr(attack=d*.05, decay=d*.25, sustain=d*.6, release=d*.1, dur=d, mul=.5)
    
    def play_chord(self, chord_name, duration):
        #self.synths = 
        self.envelope.setDur(duration)
        self.envelope.play()

    def synthesize(self, freq):
        return Sine(freq=[freq * n for n in range(1, 8)], mul=[0.39, 0.55, 0.65, 0.5, 0.15, 0.09, 0.05, 0.02])
