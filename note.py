import numpy as np
from bound import BoundingBox

class Note(object):
    NOTES = {
        -4: ("g5", 79),
        -3: ("f5", 77),
        -2: ("e5", 76),
        -1: ("d5", 74),
        0: ("c5", 72),
        1: ("b4", 71),
        2: ("a4", 69),
        3: ("g4", 67),
        4: ("f4", 65),
        5: ("e4", 64),
        6: ("d4", 62),
        7: ("c4", 60),
        8: ("b3", 59),
        9: ("a3", 57),
        10: ("g3", 55),
        11: ("f3", 53),
        12: ("e3", 52),
        13: ("d3", 50),
        14: ("c3", 48),
        15: ("b2", 47),
        16: ("a2", 45),
        17: ("f2", 53)
    }

    def __init__(self, label, pitch, box):
        self.label = label
        self.pitch = pitch
        self.duration = None
        self.box = box

    def __repr__(self):
        return "({}: {})".format(self.label, self.pitch)
