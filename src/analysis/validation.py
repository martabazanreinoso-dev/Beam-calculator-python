from constants import VALID_SUPPORTS


def validate_inputs(beam_length, support_positions, support_types):
    if beam_length <= 0:
        raise ValueError("Beam length must be greater than 0.")

    if len(support_positions) == 0:
        raise ValueError("You must enter at least one support.")

    if len(support_positions) != len(support_types):
        raise ValueError("support_positions and support_types must have the same length.")

    for support_type in support_types:
        if support_type not in VALID_SUPPORTS:
            raise ValueError(f"Invalid support type: {support_type}")

    for position in support_positions:
        if position < 0 or position > beam_length:
            raise ValueError(f"Support position {position} is outside the beam.")

    sorted_positions = sorted(support_positions)

    for i in range(len(sorted_positions) - 1):
        if sorted_positions[i] == sorted_positions[i + 1]:
            raise ValueError(f"Repeated support position: {sorted_positions[i]}")

    return True
