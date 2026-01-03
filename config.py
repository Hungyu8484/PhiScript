"""
Experiment Configuration File
"""

import os

# OpenAI API Settings
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', 'your_api_key_here')

# Model Parameters
MODEL_NAME = 'gpt-3.5-turbo'
MAX_TOKENS = 1500
TEMPERATURE = 0.1

# Experiment Parameters
NUM_EXPERIMENT_RUNS = 3
DELAY_BETWEEN_REQUESTS = 1  # seconds

# File Paths
LINEAR_PROBLEMS_FILE = 'physics_problems_collection.py'
NONLINEAR_PROBLEMS_FILE = 'nonlinear_problem_1.md'

# Results Storage
RESULTS_DIR = 'experiment_results'
SAVE_DETAILED_RESPONSES = True
