#¿QUÉ INCLUYE MAIN.PY?
#1.- La ejecución principal del programa
#2.- Entrada de datos del usuario
#3.- Llamada a validación
#4.- Llamada a clasificación
#5.- Llamada a reacciones, diagramas, etc.
#6.- Impresión de resultados en pantalla

from validation import validate_inputs
from beam_classifier import classify_cantilevers, classify_supports
from system_classifier import classify_system, classify_stability
from load_classifier import classify_load, get_required_load_data
from reactions import calculate_reactions
from diagrams import calculate_diagrams
from units import LENGTH_UNIT, FORCE_UNIT, MOMENT_UNIT, DISTRIBUTED_LOAD_UNIT

def main():
    # Input data
    beam_length = 10
    support_positions = [0]
    support_types = ["fixed"]

    # Validation
    validate_inputs(beam_length, support_positions, support_types)

    # Beam classification
    has_cantilever, cantilever_type = classify_cantilevers(beam_length, support_positions)
    support_type = classify_supports(support_types)

    # Structural system classification
    stability = classify_stability(support_types)

    if stability == "stable":
        system_type = classify_system(support_types)
    else:
        system_type = "not_applicable"
    
    # Loads
    load_types = ["point_load", "point_load"]

    classified_loads = []
    for load_type in load_types:
        classified_loads.append(classify_load(load_type))

    required_data = get_required_load_data(load_type)

    load_data = [
        {
            "magnitude": 5,
            "position": 2,
            "direction": "down"
        },
        {
            "magnitude": 3,
            "position": 6,
            "direction": "down"
        }
    ]

    # Reactions
    reactions = calculate_reactions(support_type, load_types, load_data)

    # Diagrams
    x = 2

    diagrams = calculate_diagrams(
        support_type,
        beam_length,
        load_types,
        load_data,
        x
    )

    # Results
    print("\nUNITS")
    print("Length unit:", LENGTH_UNIT)
    print("Force unit:", FORCE_UNIT)
    print("Moment unit:", MOMENT_UNIT)
    print("Distributed load unit:", DISTRIBUTED_LOAD_UNIT)

    print("\nBEAM DATA")
    print("Beam length:", beam_length, LENGTH_UNIT)
    print("Support positions:", support_positions)
    print("Support types:", support_types)

    print("\nBEAM CLASSIFICATION")
    print("Has cantilever?:", has_cantilever)
    print("Cantilever type:", cantilever_type)
    print("Support type:", support_type)

    print("\nSTRUCTURAL SYSTEM")
    print("Stability:", stability)
    print("System type:", system_type)

    # Loads
    print("\nLOADS")
    print("Load type:", classified_loads)
    print("Required data:", required_data)
    print("Load data:", load_data)

    # Reactions
    print("\nREACTIONS")
    print("Rx:", reactions["Rx"], FORCE_UNIT)
    print("Ry:", reactions["Ry"], FORCE_UNIT)
    print("M:", reactions["M"], MOMENT_UNIT)

    # Diagrams
    print("\nDIAGRAMS AT x =", x)
    print("N:", diagrams["N"])
    print("V:", diagrams["V"])
    print("M:", diagrams["M"])


if __name__ == "__main__":
    main()