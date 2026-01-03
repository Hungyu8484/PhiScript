# Nonlinear Language Design: A Cognitive Science Study on Improving AI Physics Reasoning Efficiency


## 🎯 Project Overview

This is a **cross-disciplinary cognitive science research project** exploring whether nonlinear structured language can improve AI cognitive efficiency in physics problem-solving.

**Core Problem**: Traditional linear text problems require simultaneous processing of language parsing, information extraction, and physics reasoning, resulting in excessive cognitive load. Can we design a nonlinear visual language system to reduce extraneous cognitive load?

**Innovation**:
- 🎬 Inspired by the movie "Arrival", designed "Circular Language"
- 🤖 Innovatively used GPT-3.5-turbo as a cognitive efficiency test subject
- 📊 Multi-dimensional measurement: response time, accuracy, stability

---

## 🔬 Key Findings

### Problem 1-10 (Simple Difficulty) Experimental Results

| Metric | Linear Language | Nonlinear Language | Improvement |
|--------|----------------|-------------------|-------------|
| **Response Time** | 0.996s | 0.417s | **↓ 58.2%** ⚡ |
| **Accuracy** | 86.7% | 100.0% | **↑ 13.3%** 🎯 |
| **Stability** | 100% | 100% | Equivalent 📈 |

**Main Conclusions**:
- ✅ Nonlinear language significantly outperforms linear language in time efficiency (58.2% improvement)
- ✅ Nonlinear language performs excellently in accuracy (achieving 100% accuracy)
- ✅ Both formats perform equivalently in stability

---

## 🚀 Quick Start

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Set API Key

```bash
export OPENAI_API_KEY="your-api-key-here"
```

Or modify the `config.py` file.

### Run Experiments

```bash
# Run Problem 1-10 experiment (recommended starting point)
python new_problem_1_10_experiment.py

# Run Problem 11-20 experiment
python problem_11_20_experiment.py

# Run Problem 21-30 experiment
python problem_21_30_experiment.py
```

### Analyze Results

```bash
# Complete analysis (with stability)
python complete_experimental_results_analysis_with_stability.py

# Three-level analysis
python complete_three_level_analysis.py
```

---

## 📁 Project Structure

```
experiment_language/
├── Core Experiment Scripts
│   ├── new_problem_1_10_experiment.py      # Problem 1-10 experiment (final version)
│   ├── problem_11_20_experiment.py          # Problem 11-20 experiment
│   └── problem_21_30_experiment.py         # Problem 21-30 experiment
│
├── Data Analysis
│   ├── complete_experimental_results_analysis_with_stability.py
│   └── complete_three_level_analysis.py
│
├── Problem Data
│   ├── physics_problems_collection.py      # 30 linear language problems
│   └── nonlinear_problem_1.md              # 30 nonlinear language problems
│
├── Configuration
│   ├── config.py                           # Experiment configuration
│   └── requirements.txt                    # Dependencies
│
└── Documentation
    ├── experiment_report.md                # Complete research report
    ├── experiment_methodology_log.md      # Methodology documentation
    └── MIT_Maker_Portfolio_project_description.md  # MIT Portfolio description
```

---

## 🔬 Research Methodology

### Experimental Design

- **Research Subjects**: 30 high school physics problems (10 simple, 10 medium, 10 difficult)
- **Test Format**: Each problem presented in both linear text and nonlinear structured format
- **AI Model**: GPT-3.5-turbo
- **Test Frequency**: 3 runs per problem per format

### Measurement Metrics

1. **Response Time**: Time from API request to response (excluding network delay)
2. **Accuracy**: Proportion of correct answers
3. **Stability**: Consistency of results across multiple runs

### Technical Challenges and Solutions

#### Challenge 1: Inconsistent Response Format
- **Problem**: AI sometimes provides explanations instead of pure numerical answers
- **Solution**: Lower token limits, strengthen prompts, automate format validation

#### Challenge 2: Inaccurate Time Measurement
- **Problem**: Actual response time includes network delay
- **Solution**: Establish baseline, subtract baseline from actual time

#### Challenge 3: Experiment Contamination
- **Problem**: Consecutive tests may cause AI to remember previous problems
- **Solution**: Randomize test order, add delays, batch testing

---

## 💻 Technical Implementation

### Core Functions

```python
class PhysicsLanguageExperiment:
    """Physics Language Experiment Class"""
    
    def establish_baseline(self):
        """Establish baseline, exclude network delay"""
        
    def create_linear_prompt(self, problem):
        """Create linear language prompt"""
        
    def create_nonlinear_prompt(self, problem):
        """Create nonlinear language prompt (structured format)"""
        
    def run_experiment(self):
        """Run complete experiment, including randomization and data validation"""
```

### Experiment Parameters

```python
MODEL_NAME = 'gpt-3.5-turbo'
MAX_TOKENS = 50          # Force concise answers
TEMPERATURE = 0.1        # Reduce randomness
NUM_RUNS_PER_PROBLEM = 3 # Improve reliability
```

---

## 📊 Results Display

### Problem 1-10 Complete Results

For detailed results, see:
- `problem_1_10_complete_summary.txt` - Text summary
- `new_problem_1_10_detailed_analysis_*.json` - JSON analysis results

### Visualization Charts

- `Correctness_%.pdf` - Accuracy comparison chart
- `Time_sec.pdf` - Response time comparison chart
- `Stability_%.pdf` - Stability analysis chart

---

## 🎓 Theoretical Foundation

### Cognitive Load Theory

This research is based on Sweller's (1988) Cognitive Load Theory, distinguishing three types of cognitive load:
- **Intrinsic Load**: Determined by the complexity of the learning material itself
- **Extraneous Load**: Unnecessary burden caused by presentation methods
- **Germane Load**: Beneficial load related to constructing knowledge structures

### Sapir-Whorf Hypothesis

The weak version of the Sapir-Whorf Hypothesis suggests that language structure affects cognitive patterns. This research validates the applicability of this hypothesis in AI systems.

---

## 🔍 Personal Contribution

### Independently Completed

- ✅ Original design of circular language system
- ✅ Complete experimental design
- ✅ Independently wrote all code
- ✅ Solved multiple technical challenges
- ✅ Conducted in-depth statistical analysis

### Innovation Points

- 🎬 Transformed movie concept into actual research
- 🤖 Used AI as cognitive efficiency test subject
- 📐 Designed structured nonlinear language format

---

## 📅 Project Timeline

This project evolved through multiple iterations, demonstrating continuous improvement and problem-solving:

### Phase 1: Initial Design (September 2024)
- **Concept Development**: Inspired by the movie "Arrival", designed the circular language system
- **Problem Collection**: Created 30 physics problems across three difficulty levels
- **Initial Framework**: Built basic experiment structure with OpenAI API integration
- **Key Challenge**: Establishing reliable measurement methods for cognitive efficiency

### Phase 2: Problem Identification & Optimization (September 15, 2024 - Morning)
- **Issue Discovery**: Identified inconsistent AI response formats and inaccurate time measurements
- **Solutions Implemented**:
  - Reduced token limits to force concise answers
  - Strengthened system prompts
  - Implemented automated format validation
  - Developed baseline measurement system to exclude network delay
- **Result**: More reliable data collection methodology

### Phase 3: Core Experiments - Problems 1-10 (September 15, 2024 - Afternoon)
- **Experiment Execution**: Ran comprehensive tests on simple difficulty problems
- **Iterative Refinement**: 
  - Multiple versions to fix non-numerical responses
  - Corrected thinking time calculations
  - Implemented randomization to prevent experiment contamination
- **Key Achievement**: Achieved 100% accuracy with nonlinear language format

### Phase 4: Extended Experiments - Problems 11-30 (September 15, 2024 - Afternoon)
- **Scale Expansion**: Extended testing to medium and difficult problems
- **Validation**: Confirmed results across different difficulty levels
- **Data Collection**: Gathered comprehensive dataset for statistical analysis

### Phase 5: Analysis & Documentation (September 15, 2024 - Evening)
- **Statistical Analysis**: Performed multi-dimensional analysis (time, accuracy, stability)
- **Results Validation**: Verified findings and calculated improvement metrics
- **Documentation**: Created comprehensive methodology logs and research reports

### Phase 6: Portfolio Preparation (January 2025)
- **Code Refinement**: Translated all documentation to English for international accessibility
- **Repository Organization**: Structured codebase for GitHub publication
- **Documentation**: Created professional README and supporting materials

**Total Development Time**: ~4 months (concept to completion)  
**Key Learning**: Iterative development and systematic problem-solving led to robust experimental design

---

## 📈 Future Directions

1. **Extend to Human Testing**: Validate whether results apply to human learners
2. **Different Model Comparison**: Test different models like GPT-4, Claude
3. **More Disciplines**: Extend to mathematics, chemistry, and other subjects
4. **Practical Applications**: Develop educational tools or learning platforms

---

## 📚 Related Documentation

- **Complete Research Report**: `experiment_report.md`
- **Methodology Documentation**: `experiment_methodology_log.md`
- **MIT Portfolio Description**: `MIT_Maker_Portfolio_project_description.md`
- **Research Process**: `research_process_reconstruction_guide.md`

---

## 🤝 Contributing

This is a personal research project. Questions and suggestions are welcome!

---

## 📄 License

MIT License

---

## 👤 Author

Eve Wang

---

## 🙏 Acknowledgments

- Inspired by the movie "Arrival"
- Based on OpenAI's GPT-3.5-turbo model
- References Cognitive Load Theory and Sapir-Whorf Hypothesis

---

## 📧 Contact

For questions or suggestions, please contact via:
- GitHub Issues

---

**⭐ If this project is helpful to you, please give it a Star!**
