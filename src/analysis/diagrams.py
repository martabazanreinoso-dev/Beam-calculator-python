def calculate_diagrams(support_type, beam_length, load_types, load_data, x):
    # Send the diagram calculation to the correct structural case
    if support_type == "single_fixed_support":
        return calculate_single_fixed_support_diagrams(beam_length, load_types, load_data, x)
    
    raise ValueError("This support case is not supported yet.")

def calculate_single_fixed_support_diagrams(beam_length, load_types, load_data, x):
    # Case 1.1: cantilever beam with no loads
    if len(load_types) == 0:
        return {
            "N": 0,
            "V": 0,
            "M": 0,
        }
    
    if len(load_types) != len(load_data):
        raise ValueError("load_types and load_data must have the same length.")
    
    # Start with zero internal forces and add the contribution of each load
    total_diagrams = {
        "N": 0,
        "V": 0,
        "M": 0,
    }

    for i in range(len(load_types)):
        load_type = load_types[i]
        data = load_data[i]

        load_diagram = calculate_single_load_cantilever_diagram(
            beam_length, load_type, data, x
        )

        total_diagrams["N"] += load_diagram["N"]
        total_diagrams["V"] += load_diagram["V"]
        total_diagrams["M"] += load_diagram["M"]

    return total_diagrams

def calculate_single_load_cantilever_diagram(beam_length, load_type, load_data, x):
    if load_type == "point_load":
        return calculate_cantilever_point_load_diagram(load_data, x)
    
    raise ValueError(f"Load type not supported yet: {load_type}")

def get_signed_point_load(magnitude, direction):
    # Upward loads are positive, downward loads are negative
    if direction == "up":
        return magnitude
    
    if direction == "down":
        return -magnitude
    
    raise ValueError(f"Invalid point load direction: {direction}")


def calculate_cantilever_point_load_diagram(load_data, x):
    magnitude = load_data["magnitude"]
    position = load_data["position"]
    direction = load_data["direction"]

    # Convert magnitude and direction into a signed load
    signed_magnitude = get_signed_point_load(magnitude, direction)

    # There is no axial force in this case
    normal_force = 0

    # Before the load, the section resists the load
    if x < position:
        shear_force = - signed_magnitude
        bending_moment = -signed_magnitude * (position - x)
    else:
        shear_force = 0
        bending_moment = 0

    return {
        "N": normal_force,
        "V": shear_force,
        "M": bending_moment,
    }
