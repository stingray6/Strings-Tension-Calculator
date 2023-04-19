TENSION_FACTOR = 386.4 # Const value used in equations
STANDARD_SCALE_LENGTH = 25.5 # default guitar"s scale length

# Notes" pitch information (FORMAT -> note : frequency [Hz])
PITCH = {
        "C0" : "16.35",
        "C#0" : "17.32",
        "D0" : "18.35",
        "D#0" : "19.45",
        "E0" : "20.60",
        "F0" : "21.83",
        "F#0" : "23.12",
        "G0" : "24.50",
        "G#0" : "25.96",
        "A0" : "27.50",
        "A#0" : "29.14",
        "B0" : "30.87",
        "C1" : "32.70",
        "C#1" : "34.65",
        "D1" : "36.71",
        "D#1" : "38.89",
        "E1" : "41.20",
        "F1" : "43.65",
        "F#1" : "46.25",
        "G1" : "49.00",
        "G#1" : "51.91",
        "A1" : "55.00",
        "A#1" : "58.27",
        "B1" : "61.74",
        "C2" : "65.41",
        "C#2" : "69.30",
        "D2" : "73.42",
        "D#2" : "77.78",
        "E2" : "82.41",
        "F2" : "87.31",
        "F#2" : "92.50",
        "G2" : "98.00",
        "G#2" : "103.83",
        "A2" : "110.00",
        "A#2" : "116.54",
        "B2" : "123.47",
        "C3" : "130.81",
        "C#3" : "138.59",
        "D3" : "146.83",
        "D#3" : "155.56",
        "E3" : "164.81",
        "F3" : "174.61",
        "F#3" : "185.00",
        "G3" : "196.00",
        "G#3" : "207.65",
        "A3" : "220.00",
        "A#3" : "233.08",
        "B3" : "246.94",
        "C4" : "261.63",
        "C#4" : "277.18",
        "D4" : "293.66",
        "D#4" : "311.13",
        "E4" : "329.63",
        "F4" : "349.23",
        "F#4" : "369.99",
        "G4" : "392.00",
        "G#4" : "415.30",
        "A4" : "440.00",
        "A#4" : "466.16",
        "B4" : "493.88",
        "C5" : "523.25",
        "C#5" : "554.37",
        "D5" : "587.33",
        "D#5" : "622.25",
        "E5" : "659.25",
        "F5" : "698.46",
        "F#5" : "739.99",
        "G5" : "783.99",
        "G#5" : "830.61",
        "A5" : "880.00",
        "A#5" : "932.33",
        "B5" : "987.77",
        "C6" : "1046.50",
        "C#6" : "1108.73",
        "D6" : "1174.66",
        "D#6" : "1244.51",
        "E6" : "1318.51",
        "F6" : "1396.91",
        "F#6" : "1479.98",
        "G6" : "1567.98",
        "G#6" : "1661.22",
        "A6" : "1760.00",
        "A#6" : "1864.66",
        "B6" : "1975.53",
        "C7" : "2093.00",
        "C#7" : "2217.46",
        "D7" : "2349.32",
        "D#7" : "2489.02",
        "E7" : "2637.02",
        "F7" : "2793.83",
        "F#7" : "2959.96",
        "G7" : "3135.96",
        "G#7" : "3322.44",
        "A7" : "3520.00",
        "A#7" : "3729.31",
        "B7" : "3951.07",
        "C8" : "4186.01",
        "C#8" : "4434.92",
        "D8" : "4698.63",
        "D#8" : "4978.03",
        "E8" : "5274.04",
        "F8" : "5587.65",
        "F#8" : "5919.91",
        "G8" : "6271.93",
        "G#8" : "6644.88",
        "A8" : "7040.00",
        "A#8" : "7458.62",
        "B8" : "7902.13"
    }

# Guitar Tunings Pitch Mapping
STANDARD_TUNING = {
    "E-1" : PITCH["E4"],
    "B-2" : PITCH["B3"],
    "G-3" : PITCH["G3"],
    "D-4" : PITCH["D3"],
    "A-5" : PITCH["A2"],
    "E-6" : PITCH["E2"]
}

DROP_D_TUNING = {
    "E-1" : PITCH["E4"],
    "B-2" : PITCH["B3"],
    "G-3" : PITCH["G3"],
    "D-4" : PITCH["D3"],
    "A-5" : PITCH["A2"],
    "E-6" : PITCH["D2"]
}

D_SHARP_TUNING = {
    "E-1" : PITCH["D#4"],
    "B-2" : PITCH["A#3"],
    "G-3" : PITCH["F#3"],
    "D-4" : PITCH["C#3"],
    "A-5" : PITCH["G#2"],
    "E-6" : PITCH["D#2"]
}

D_TUNING = {
    "E-1" : PITCH["D4"],
    "B-2" : PITCH["A3"],
    "G-3" : PITCH["F3"],
    "D-4" : PITCH["C3"],
    "A-5" : PITCH["G2"],
    "E-6" : PITCH["D2"]
}

C_SHARP_TUNING = {
    "E-1" : PITCH["C#4"],
    "B-2" : PITCH["G#3"],
    "G-3" : PITCH["E3"],
    "D-4" : PITCH["B3"],
    "A-5" : PITCH["F#2"],
    "E-6" : PITCH["C#2"]
}

C_TUNING = {
    "E-1" : PITCH["C4"],
    "B-2" : PITCH["G3"],
    "G-3" : PITCH["D#3"],
    "D-4" : PITCH["A#3"],
    "A-5" : PITCH["F2"],
    "E-6" : PITCH["C2"]
}

DROP_C_TUNING = {
    "E-1" : PITCH["D4"],
    "B-2" : PITCH["A3"],
    "G-3" : PITCH["F3"],
    "D-4" : PITCH["C3"],
    "A-5" : PITCH["G2"],
    "E-6" : PITCH["C2"]
}

# Representation of single guitar string
class GuitarString:
    def __init__(self, string_name, diameter, tension): 
        self.string_name = string_name
        self.diameter = diameter
        self.unit_weight = self._calculate_unit_weight(STANDARD_TUNING[string_name], tension)

    # Finding Unit Weight needed for Tension equation
    def _calculate_unit_weight(self, frequency, tension):
        unit_weight = (tension * TENSION_FACTOR) / (2 * STANDARD_SCALE_LENGTH * float(frequency)) ** 2
        return unit_weight

    # Finding Tension for another tunings
    def calculate_tension(self, target_frequency, length):
        tension = (self.unit_weight * (2 * length * float(target_frequency)) ** 2) / TENSION_FACTOR
        return tension     

# Representation of electric guitar stringset
class StringSet:
    def __init__(self, name, strings, length):
        self.name = name
        self.strings = strings
        self.length = length
      
    def calculate_tension(self, string_name, target_frequency):
        guitar_string = next(x for x in self.strings if x.string_name == string_name)
        return guitar_string.calculate_tension(target_frequency, self.length)
     
    def print_tensions(self, tuning):
        total_tension = 0
        print(self.name)
        for string_name, frequency in tuning.items():
            tension = self.calculate_tension(string_name, frequency)
            total_tension += tension
            print(f"Struna {string_name}: {round(tension,1)}")
        print(f"Łączna siła [lbs]: {round(total_tension)}")


# Entering data from manufacturer's reference tables using GuitarString class
SUPER_LIGHT_STRINGS = [
    GuitarString("E-1", 0.009, 13),
    GuitarString("B-2", 0.011, 11),
    GuitarString("G-3", 0.016, 15),
    GuitarString("D-4", 0.024, 16),
    GuitarString("A-5", 0.032, 16),
    GuitarString("E-6", 0.042, 15)
]

LIGHT_STRINGS = [
    GuitarString("E-1", 0.010, 16),
    GuitarString("B-2", 0.013, 15),
    GuitarString("G-3", 0.017, 17),
    GuitarString("D-4", 0.026, 18),
    GuitarString("A-5", 0.036, 20),
    GuitarString("E-6", 0.046, 17)
]

MEDIUM_STRINGS = [
    GuitarString("E-1", 0.011, 20),
    GuitarString("B-2", 0.014, 18),
    GuitarString("G-3", 0.018, 19),
    GuitarString("D-4", 0.028, 21),
    GuitarString("A-5", 0.038, 22),
    GuitarString("E-6", 0.049, 20) 
]

HEAVY_STRINGS = [
    GuitarString("E-1", 0.012, 23),
    GuitarString("B-2", 0.016, 23),
    GuitarString("G-3", 0.024, 28),
    GuitarString("D-4", 0.032, 28),
    GuitarString("A-5", 0.042, 26),
    GuitarString("E-6", 0.052, 22) 
]

# Simple example of use
# Finding out the tension that strings would have if "Light Strings" were tuned to "Drop C" Tuning

# Choose desired tuning name from "Guitar Tunings Pitch Mapping"
tuning_chosen = DROP_C_TUNING

# Create an object for desired stringset and scale length
stringset_chosen = StringSet("Light Strings", LIGHT_STRINGS, 25.5)

# Call the printing method on the object passing the tuning information as an argument
stringset_chosen.print_tensions(tuning_chosen)