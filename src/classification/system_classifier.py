from constants import REACTIONS_PER_SUPPORT

def count_reactions(support_types):
    total_reactions = 0

    for support in support_types:
        total_reactions += REACTIONS_PER_SUPPORT[support]

    return total_reactions

def classify_stability(support_types):
    total_reactions = count_reactions(support_types)

    if total_reactions < 3:
        return "unstable"
    
    return "stable"

def classify_system(support_types):
    total_reactions = count_reactions(support_types)

    if total_reactions == 3:
        return "statically_determinate"
    
    if total_reactions > 3:
        return "statically_indeterminate"
    
    return "not_applicable"