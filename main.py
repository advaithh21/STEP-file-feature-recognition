import sys
import collections

FEATURE_START = 'DATA;'
CIRCUIT_END = 'ENDSEC;'


class Cylinder:
    def __init__(self):
        self.radius = None
        self.center = [None, None, None]
        self.height = None
        self.orientation = None

    def getData(self, features, idxNo):
        features[idxNo]


def get_circuit(content):
    """
    :return: Search for the circuit (if any) in content and return it.
    """

    # initiating parameter containing info about circuit
    circuit_start = circuit_end = False
    start_index = end_index = None

    # loop to traverse through content
    for line_index, line in enumerate(content):
        tokens = line.split()

        # Finding start of circuit
        if tokens and tokens[0] == FEATURE_START:
            # Giving error if we had already found circuit start command before
            if circuit_start is True:
                sys.exit(f"ERROR: More then one {FEATURE_START} found")
            else:
                # checking if there is any unwanted stuff after circuit start command
                if len(tokens) > 1 and tokens[1][0] != '#':
                    sys.exit(f"ERROR: Invalid text after {FEATURE_START} in line {line_index + 1}")
                circuit_start = True
                start_index = line_index

        # Finding end of circuit
        if tokens and tokens[0] == CIRCUIT_END:
            # Giving error if we had already found circuit end command before
            if len(tokens) > 1 and tokens[1][0] != '#':
                sys.exit(f"ERROR: Invalid text after {CIRCUIT_END} in line {line_index + 1}")
            circuit_end = True
            end_index = line_index



    # Exiting program if no circuit fond or if circuit block is not valid
    if circuit_start is False:
        sys.exit("Circuit start not Found")

    if circuit_end is False:
        sys.exit("ERROR: Circuit start found but end don't exist")

    if start_index > end_index:
        sys.exit(f"ERROR: Invalid circuit: {FEATURE_START} came after {CIRCUIT_END}")

    # returning the circuit portion
    return content[start_index+1:end_index]


def helper(line, i, j):
    if i > j:
        return []

    prevI, prevJ = i, j

    while i < j and line[i] != '(':
        i += 1

    while i < j and line[j] != ')':
        j -= 1

    if i == j:
        return line[prevI: prevJ + 1]
    return line[prevI:i] + [helper(line, i+1, j-1)] + line[j+1: prevJ+1]





f = open('Cylinder.STEP')
lines = get_circuit(f.readlines())
dict = {}
for line in lines:
    feature = line.replace("'", "").replace(',','').split()
    feature_no = feature[0]
    temp = helper(feature[2:-1], 0, len(feature[2:-1]) -1)
    dict[feature_no] = temp

for key in dict:
    print(f"{key}: {dict[key]}")



