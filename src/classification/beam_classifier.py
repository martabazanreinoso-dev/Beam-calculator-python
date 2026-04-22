def classify_cantilevers(beam_length, support_positions):
    support_positions = sorted(support_positions)

    left_cantilever = support_positions[0] > 0
    right_cantilever = support_positions[-1] < beam_length

    has_cantilever = left_cantilever or right_cantilever

    if left_cantilever and right_cantilever:
        cantilever_type = "doble_cantilever"

    elif left_cantilever:
        cantilever_type = "left_cantilever"

    elif right_cantilever:
        cantilever_type = "right_cantilever"

    else:
        cantilever_type = "no_cantilever"
    
    return has_cantilever, cantilever_type


def classify_supports(support_types):
    n = len(support_types)

    if n == 1:
        if support_types[0] == "fixed":
            return "single_fixed_support"
        return "single_support_unstable"

    if n == 2:
        supports = set(support_types)

        if supports == {"pinned", "roller"}:
            return "simply_supported"

        if supports == {"fixed"}:
            return "fixed_fixed"

        if supports == {"pinned"}:
            return "pinned_pinned"

        if supports == {"roller"}:
            return "roller_roller"

        if supports == {"fixed", "roller"}:
            return "fixed_roller"

        if supports == {"fixed", "pinned"}:
            return "fixed_pinned"

        return "two_supports_unknown"

    if n > 2:
        return "continuous"

    return "unknown"