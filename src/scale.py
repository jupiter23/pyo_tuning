class Scale():
    """
    Class which generates tuning ratios for a 12 step scale.
    This is a "Western Tuner", and can only produce rations for 12 step scales.
    """
    def get_natural_scale_ratios(self):
        return [1, 16.0/15, 9.0/8, 6.0/5, 5.0/4, 4.0/3, 64.0/45, 3.0/2, 8.0/5, 5.0/3, 16.0/9, 15.0/8]

    def get_pythagorean_scale_ratios(self):
        return [1, 256/243, 9/8, 32/27, 81/64, 4/3, 729/512, 3/2, 128/81, 27/16, 16/9, 243/128]

    def get_equal_temperament_ratios(self, num_tones=12):
        return [(2.**(i/float(num_tones))) for i in range(0, num_tones)]

    def get_ratios(self, scale = 'natural'):
        if (scale == 'natural'):
            return self.get_natural_scale_ratios()

        if (scale == 'pythagorean'):
            return self.get_pythagorean_scale_ratios()

        if (scale == 'equal'):
            return self.get_equal_temperament_ratios()

        raise ValueError('Unsuported scale was requested from Scale: ' + scale)
