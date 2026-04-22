
# Valid support types for the beam model
VALID_SUPPORTS = ["fixed", "pinned", "roller"]

# Number og reaction components provided by each suppport in 2D
REACTIONS_PER_SUPPORT = {
    "fixed": 3,
    "pinned": 2,
    "roller": 1
}