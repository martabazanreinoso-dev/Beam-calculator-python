def calculate_reactions(support_type, load_types, load_data):
    # Send the calculation to the correct structural case
    if support_type == "single_fixed_support":
        return calculate_single_fixed_support_reactions(load_types, load_data)
    
    raise ValueError("This support case is no supported yet.")


def calculate_single_fixed_support_reactions(load_types, load_data):
    # Case 1.1: cantilever beam with no loads
    if len(load_types) == 0:
        return {
            "Rx": 0,
            "Ry": 0,
            "M" : 0,
        }
    
    if len(load_types) != len(load_data):
        raise ValueError("load_types and load_data must have the same lenght.")
    
    # Start with zero reactions and add the contribution of each load
    total_reactions = {
        "Rx": 0,
        "Ry": 0,
        "M": 0,
    }
    
    for i in range(len(load_types)):
        load_type = load_types[i]
        data = load_data[i]

        load_reactions = calculate_single_load_cantilever_reactions(load_type, data)

        total_reactions["Rx"] += load_reactions["Rx"]
        total_reactions["Ry"] += load_reactions["Ry"]
        total_reactions["M"] += load_reactions["M"]
    
    return total_reactions
    

def calculate_single_load_cantilever_reactions(load_type, load_data):
    if load_type == "point_load":
        return calculate_cantilever_point_load_reactions(load_data)
        
    if load_type == "uniform_distributed_load":
        return calculate_cantilever_udl_reactions(load_data)
        
    if load_type == "moment":
        return calculate_cantilever_moment_reactions(load_data)
        
    raise ValueError(f"Load type not supported yet: {load_type}")
    

def get_signed_point_load(magnitude, direction):
    # Upward loads are positive, downward loads are negative
    if direction == "up":
        return magnitude
    
    if direction == "down":
        return -magnitude
    
    raise ValueError(f"Invalid point load direction: {direction}")


def get_signed_distributed_load(intensity, direction):
    # Upward distributed loads are positive, downward distributed loads are negative
    if direction == "up":
        return intensity
    
    if direction == "down":
        return intensity
    
    raise ValueError(f"Invalid distributed load direction: {direction}")


def get_signed_moment(magnitude, direction):
    # Counterclockwise moments are positive, clockwise moments are negative
    if direction == "counterclockwise":
        return magnitude
    
    if direction == "clockwise":
        return -magnitude
    
    raise ValueError(f"Invalid moment direction: {direction}")


def calculate_cantilever_point_load_reactions(load_data):
    magnitude = load_data["magnitude"]
    position = load_data["position"]
    direction = load_data["direction"]

    # Convert magnitude and direction into a signed vertical load
    signed_magnitude = get_signed_point_load(magnitude, direction)

    # Reactions are obtained from equilibrium
    reactions = {
        "Rx": 0,
        "Ry": -signed_magnitude,
        "M": -signed_magnitude * position,
    }

    return reactions


def calculate_cantilever_udl_reactions(load_data):
    intensity = load_data["intensity"]
    start_position = load_data["start_position"]
    end_position = load_data["end_position"]
    direction = load_data["direction"]

    # Convert intensity and direction into a signed distributed load
    signed_intensity = get_signed_distributed_load(intensity, direction)

    #Replace the distributed load by its equivalent resultant
    loaded_length = end_position - start_position
    total_load = signed_intensity * loaded_length
    resultant_position = (start_position + end_position) / 2

    # Reactions are obtained from equilibrium
    reactions = {
        "Rx": 0,
        "Ry": -total_load,
        "M": -total_load * resultant_position,
    }

    return reactions


def calculate_cantilever_moment_reactions(load_data):
    magnitude = load_data["magnitude"]
    direction = load_data["direction"]

    # Convert magnitude and direction into a signed moment
    signed_moment = get_signed_moment(magnitude, direction)

    # An applied moment does not create vertical or horizontal force
    reactions = {
        "Rx": 0,
        "Ry": 0,
        "M": -signed_moment,
    }

    return reactions