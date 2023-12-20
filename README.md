# Hanoi Tower
AI learning how to solve Hanoi Tower problem.

# Project Structure
HanoiTowerProject/
│
├── src/
│   ├── common/
│   │   └── constants.py  # Common constants used across the project
│   │
│   ├── hanoi_logic/
│   │   ├── __init__.py
│   │   └── hanoi_solver.py  # Core logic for the Hanoi Tower problem
│   │
│   ├── cli/
│   │   ├── __init__.py
│   │   └── hanoi_cli.py  # CLI interface for interacting with the game
│   │
│   ├── ai/
│   │   ├── __init__.py
│   │   ├── ai_solver.py  # AI model for solving the Hanoi Tower
│   │   └── training/
│   │       ├── __init__.py
│   │       └── train_model.py  # Script for training the AI model
│   │
│   └── gui/
│       ├── __init__.py
│       └── hanoi_gui.py  # GUI application for the Hanoi Tower simulation
│
├── tests/
│   ├── hanoi_logic_tests.py
│   ├── cli_tests.py
│   ├── ai_tests.py
│   └── gui_tests.py
│
├── notebooks/
│   └── ai_experiments.ipynb  # Jupyter notebooks for AI experiments and visualizations
│
├── docs/
│   └── documentation.md  # Project documentation and user guide
│
├── requirements.txt  # Python dependencies required for the project
├── setup.py  # Setup script for the project
└── README.md  # Overview and instructions for the project
