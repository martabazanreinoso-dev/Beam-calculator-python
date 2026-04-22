# Valid load types for the first version of the program
VALID_LOAD_TYPES = [
    "point_load",
    "uniform_distributed_load",
    "moment",
]


def classify_load(load_type):
    if load_type not in VALID_LOAD_TYPES:
        raise ValueError(f"Invalid load type: {load_type}")

    return load_type


def classify_loads(load_types):
    classified_loads = []

    for load_type in load_types:
        classified_load = classify_load(load_type)
        classified_loads.append(classified_load)

    return classified_loads


def get_required_load_data(load_type):
    # Point load needs magnitude, position and direction
    if load_type == "point_load":
        return ["magnitude", "position", "direction"]

    #Uniform load needs intensity, range and direction
    if load_type == "uniform_distributed_load":
        return ["magnitude", "start_position", "end_position", "direction"]

    # Applied moment needs magnitude, position and direction
    if load_type == "moment":
        return ["magnitude", "position", "direction"]

    raise ValueError(f"Invalid load type: {load_type}")

def get_valid_directions(load_type):
    if load_type == "poin_load":
        return ["up", "down"]
    
    if load_type == "uniform_distributed_load":
        return ["up", "down"]
    
    if load_type == "moment":
        return ["cloackwise", "counterclockwise"]
    
    raise ValueError(f"Invalid load type: {load_type}")
