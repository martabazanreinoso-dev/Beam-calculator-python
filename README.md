# Beam-calculator-python
This project is a Python-based tool for the classification and basic analysis of beams in structural engineering.

It identifies beam types based on support conditions and detects features such as cantilevers, helping automate early-stage structural analysis.

FEATURES.
- 
- Beam classification based on supports.
- Detection of left and right cantilevers.
- Identification of structural stability (stable / unstable /hyperstatic).
- Modular and scalable Python code.

HOW IT WORKS.
- 
The program takes:
- Beam length.
- Support positions and types.
- Loads and types.
It then:
1. Sorts support positions.
2. Detects cantilevers.
3. Classifies the beam system.

PROJECT STRUCTURE.
-
beam-analysis/
│
├── main.py
├── README.md
├── beam_classifier.py
├── beam_options.py
├── beam_visualization.py
├── constants.py
├── diagrams.py
├── load_classifier.py
├── reactions.py
├── system_classifier.py
├── units.py
├── validation.py

📈 Future Improvements
Load cases (point loads, distributed loads)
Shear force and bending moment diagrams
Visualization of beam systems
Integration with engineering tools
🛠️ Technologies
Python 3
👨‍💻 Author

Marta Jimenez

🌍

This project is part of my journey to build practical engineering tools and transition into remote technical work and freelancing.
