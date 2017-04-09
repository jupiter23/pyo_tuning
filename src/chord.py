from pyo import *
from tuner import Tuner

class Chord():
    """
    Class which provides a set of positions for a given chord.
    """

    def __init__(self, scale, root_frequency):
        self.set_scale(scale)
        self.set_root_frequency(root_frequency)

    def get_chord_frequencies(self, chord_name):
        root = self.root_frequency
        scale = self.scale
        if (chord_name == 'maj'):
            return [root * scale[0], root * scale[4], root * scale[7]]

        if (chord_name == 'min'):
            return [root * scale[0], root * scale[3], root * scale[7]]

        if (chord_name == 'aug'):
            return [root * scale[0], root * scale[4], root * scale[8]]

        if (chord_name == 'dim'):
            return [root * scale[0], root * scale[3], root * scale[6]]

        if (chord_name == 'maj6'):
            return [root * scale[0], root * scale[4], (2 * root * scale[7]), root * scale[9]]

        if (chord_name == 'min6'):
            return [root * scale[0], root * scale[3], (2 * root * scale[7]), root * scale[9]]

        if (chord_name == 'dom7'):
            return [root * scale[0], root * scale[4], root * scale[7], root * scale[10]]

        if (chord_name == 'maj7'):
            return [root * scale[0], root * scale[4], root * scale[7], root * scale[11]]

        if (chord_name == 'min7'):
            return [root * scale[0], root * scale[3], root * scale[7], root * scale[10]]

        if (chord_name == 'aug7'):
            return [root * scale[0], root * scale[4], root * scale[8], root * scale[10]]

        if (chord_name == 'dim7'):
            return [root * scale[0], root * scale[3], root * scale[6], root * scale[9]]

        if (chord_name == '07'):
            return [root * scale[0], root * scale[3], root * scale[6], root * scale[10]]

        if (chord_name == 'minmaj7'):
            return [root * scale[0], root *  scale[3], root * scale[7], root * scale[11]]

        if (chord_name == 'dom7_custom'):
            return [root * scale[0], root * scale[4], root * scale[7], root * scale[7] * scale[3]]

        raise ValueError('Unsuported chord was requested from Chord: ' + chord_name)

    def set_scale(self, scale):
        self.scale = scale

    def set_root_frequency(self, root_frequency):
        self.root_frequency = root_frequency
