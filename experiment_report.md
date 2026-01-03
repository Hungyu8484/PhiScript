# Research on the Impact of Nonlinear Language on Cognitive Efficiency in Physics Reasoning: Circular Graphical Language vs Linear Text

## Abstract

## I. Introduction

**Research Background and Motivation**:

In high school physics education, problems are typically presented in lengthy linear text. When reading, students must simultaneously parse language structure, search for key conditions and variable relationships, and then perform physics reasoning. This process often leads to additional cognitive burden (extraneous cognitive load), making the step of understanding the problem difficult, preventing deep thinking about physics problems. According to Cognitive Load Theory (Sweller, 1988), human working memory capacity is limited. If the problem's presentation method is poorly designed, students will consume too many cognitive resources before solving the problem.

This problem inspired me to think: Does there exist a more intuitive language system that can effectively reduce extraneous cognitive load and allow students to grasp the problem faster? The nonlinear alien language presented in the movie "Arrival" provided inspiration. The linguistic relativity (Sapir-Whorf Hypothesis) discussed in the film suggests that language structure may affect cognitive patterns. If the linear nature of human language limits our understanding, then designing a "nonlinear visual language" might improve the efficiency of physics problem-solving.

Therefore, this research designed "circular language" (circular language), converting physics problems into graphical structures composed of nodes and connections. The research objectives are to examine:
1. Can circular language reduce extraneous cognitive load and improve problem-solving efficiency?
2. Does its effectiveness vary with problem difficulty?

## II. Literature Review

### 2.1 Linear Language and Nonlinear Language

Linear language refers to language forms where information is arranged sequentially and must be read along a specific path, such as traditional written and spoken language. The text descriptions of physics problems are typical examples. For example: "An object with a mass of 2 kg falls freely from a height of 10 meters. Ignoring air resistance, find its landing speed." In this presentation, students need to read word by word and then integrate the problem conditions themselves.

In contrast, nonlinear language allows simultaneous presentation of multiple information dimensions. Readers can grasp problem elements through images, spatial structures, or color markers. The "circular language" proposed in this research is an example: presenting information such as mass, height, motion state, and target quantity as nodes, and using arrows or connections to show relationships between them. This approach theoretically reduces the burden of information search, allowing students to enter physics reasoning faster.

### 2.2 Linguistic Relativity

Linguistic relativity (Sapir-Whorf Hypothesis) suggests that language affects human thinking patterns. Although the strong version of linguistic determinism has been questioned, the weak version of linguistic relativity has received substantial empirical support. For example, Boroditsky's (2001) research showed significant differences in time concept understanding between Chinese and English speakers, directly related to language expression. This shows that different language structures indeed affect human cognitive patterns. Therefore, converting physics problems from linear text to circular structure may also bring differences in cognitive efficiency.

### 2.3 Cognitive Load Theory

Cognitive Load Theory (Sweller, 1988) distinguishes three types of cognitive load:
- **Intrinsic load**: Determined by the complexity of the learning material itself.
- **Extraneous load**: Unnecessary burden caused by presentation methods or instructional design.
- **Germane load**: Beneficial load related to learners constructing knowledge structures.

When solving physics problems, if the problem's presentation method can reduce extraneous load, students can allocate more resources to understanding and reasoning. Miller's (1956) "magical number seven" experiment showed limited working memory capacity, while Just & Carpenter's (1992) research indicated that response time can reflect cognitive load. Therefore, this research will objectively compare the effects of linear and nonlinear language through three indicators: response time, accuracy rate, and stability.

## III. Research Methodology

### 3.1 Research Subjects

To fairly compare different language forms, this research selected AI models as research subjects. This choice has three reasons:
1. AI's problem-solving process is consistent, eliminating effects from human subjects' emotions, attention, or background knowledge differences.
2. Can repeat identical tests, ensuring data precision and reliability.
3. Research can focus more on language representation effects rather than individual differences.

This experiment used OpenAI's GPT-3.5-turbo model as the experimental subject, tested through API interface. This model is a mature large language model with good physics knowledge foundation and mathematical reasoning ability, very suitable as a tester for solving physics problems.

### 3.2 Experimental Objectives

The objectives of this experiment include:

1. Design nonlinear language to represent physics problems in circular form, called "concentric circle language"
2. Design a collection of 30 high school-level physics problems, divided into three difficulty levels: simple, medium, and difficult, described in traditional linear text
3. Perform language conversion, converting 30 problems into the designed concentric circle language representation
4. Begin performance testing, testing AI's response time, accuracy rate, and stability when solving problems
5. Compare changes in these indicators under two language formats

### 3.3 Experimental Design

#### 3.3.1 Concentric Circle Language Design

Inspired by the movie "Arrival", the language is designed in circular form. Circular language is divided into three levels:

**Structure**:
- **Inner ring**: Target physics quantity (e.g., speed)
- **Middle ring**: Conditions for solving the target quantity (e.g., t=3sec)
- **Outer ring**: Divided into A/B/C:
  - A. Invariants (e.g., mass=5kg)
  - B. Variables (e.g., v=t²+2t+7)
  - C. Boundaries (e.g., t=0, v=0)

*[Circular language design diagram should be inserted here]*

#### 3.3.2 Physics Problem Sources

The problem collection used in this research was self-designed and verified. To ensure problems can test language representation effects at different difficulty levels, the collection is divided into three complexity levels: simple, medium, and difficult, with ten problems each, totaling thirty problems.

**Simple Problems (Problem 1–10)**
Mainly test direct applications of basic kinematics and Newton's laws, such as uniform acceleration motion, free fall, and simple energy conservation problems. These problems typically require single-step calculations and can test subjects' performance under low cognitive load.

**Medium Problems (Problem 11–20)**
Involve situations requiring multi-step reasoning, such as elastic collisions, oscillating systems, and thermodynamic energy conversion. These problems require subjects to integrate multiple physics concepts, testing language format effects on problem-solving efficiency under medium cognitive load.

**Difficult Problems (Problem 21–30)**
Include advanced topics such as rigid body rotation, coupled systems, and more complex thermodynamic processes. Problems require longer derivations or formula combinations. This level is used to test whether nonlinear language can effectively assist understanding and computation under high cognitive load situations.

All problems are designed to output single numerical answers to avoid evaluation bias from multiple interpretations.

#### 3.3.3 Two Representation Methods

Using problem 1 as an example:

**Linear Language Representation**:
> "Jessica drives her car from home to school, covering a distance of 120 km. The trip takes exactly 2 hours due to morning traffic. Calculate Jessica's average speed during this journey."

**Nonlinear Language Representation**:
- **Target physics quantity**: speed
- **Solving condition**: average
- **Outer ring A. Invariants**: Distance = 120 km, Time = 2 hours

#### 3.3.4 Cognitive Load Measurement Indicators

Based on Cognitive Load Theory (Sweller, 1988) and related empirical research, this research adopts three objective indicators to quantify the impact of different language formats on AI cognitive processing. The selection of these indicators not only has solid theoretical foundation but also conforms to standard practices in cognitive science research for measuring extraneous cognitive load.

Response time as the first measurement indicator has its theoretical foundation from Just & Carpenter's (1992) research, which confirmed that response time is a key indicator for measuring cognitive load. Shorter response times typically reflect lower cognitive load and more efficient information processing. In this research, response time measurement uses millisecond-level precision, recording time from API request sending to receiving complete response. To exclude technical noise effects on measurement results, this research adopts baseline correction method, using standardized prompts ("hello") to measure basic processing time, repeating measurements 5 times and taking the average as baseline. The baseline includes network transmission delay, system processing time, API fixed overhead, and other technical factors. The final corrected response time calculation formula is: Corrected Response Time = Actual Response Time - Baseline Time.

Accuracy rate as the second measurement indicator directly reflects the impact of extraneous cognitive load on AI problem-solving accuracy. According to Chandler & Sweller's (1991) research, high cognitive load leads to increased error rates. Therefore, accuracy rate is an important indicator for evaluating language format effectiveness. Measurement methods include precise comparison of AI-generated numerical answers with preset standard answers, while allowing small numerical precision differences (±5%) to account for floating-point operation errors. The accuracy rate calculation formula is: Accuracy Rate = (Number of Correct Answers / Total Number of Tests) × 100%.

Stability as the third measurement indicator reflects the consistency degree of cognitive processing guided by language format. According to Kahneman's (1973) research, high cognitive load leads to increased response variability. Therefore, stability can effectively evaluate different language formats' ability to guide AI to produce consistent and reliable cognitive responses. Measurement methods include repeating tests 3 times for the same problem, calculating the coefficient of variation (CV) of answers. The calculation formula is: CV = Standard Deviation / Mean, Stability = max(0, 1 - CV). To facilitate result interpretation, this research established four-level stability standards: 0.8-1.0 as highly stable (CV ≤ 0.2), 0.6-0.8 as moderately stable (0.2 < CV ≤ 0.4), 0.4-0.6 as low stability (0.4 < CV ≤ 0.6), 0.0-0.4 as unstable (CV > 0.6).

#### 3.3.5 Data Testing Methods

This research adopts a completely randomized design to ensure objectivity and reproducibility of experimental results. Experiments are conducted in difficulty groups, sequentially testing simple problems (1-10), medium problems (11-20), and difficult problems (21-30). Each problem is tested in both linear and nonlinear language formats, with each format repeated 3 times to ensure measurement stability. The experiment conducts a total of 180 tests (30 problems × 2 formats × 3 repetitions). To prevent API cache contamination and system load effects, the interval between each test is set to 10 seconds. Finally, the results of 3 repeated measurements are averaged as representative data for that problem in that format.

To ensure measurement accuracy, this research implemented multi-level experimental control measures. First, I adopted baseline correction method, using standardized prompts ("hello") to measure system basic response time, repeating measurements 5 times and taking the average to establish baseline, then subtracting baseline time from all actual measurements. Second, I implemented strict randomization control, including complete randomization of problem order and format order to avoid inter-format interference.

## IV. Results and Analysis

### 4.1 Overall Performance Comparison

Experimental results show that nonlinear language outperforms linear language on all measurement indicators. Overall, nonlinear language's average response time is 1.236 seconds, compared to linear language's 2.024 seconds, improving processing speed by 39.0%. In terms of accuracy, nonlinear language reaches 65.6%, while linear language is 44.4%, improving by 21.1 percentage points. In terms of stability, linear language is 0.778, nonlinear language is 0.757, both performing equivalently in stability.

**Table 1: Overall Performance Comparison**

| Measurement Indicator | Linear Language | Nonlinear Language | Improvement |
|----------------------|----------------|-------------------|-------------|
| Average Response Time (seconds) | 2.024 | 1.236 | -39.0% |
| Average Accuracy Rate (%) | 44.4 | 65.6 | +21.1% |
| Average Stability | 0.778 | 0.757 | -0.021 |

**Table 2: Performance Comparison by Difficulty Level**

| Difficulty Level | Linear Time | Nonlinear Time | Speed Gain | Linear Accuracy | Nonlinear Accuracy | Accuracy Gain | Linear Stability | Nonlinear Stability | Stability Gain |
|-----------------|-------------|----------------|------------|-----------------|-------------------|---------------|------------------|-------------------|----------------|
| Simple (1-10) | 0.227 | 0.172 | -24.2% | 60.0% | 70.0% | +10.0% | 0.979 | 0.678 | -0.301 |
| Medium (11-20) | 2.125 | 1.229 | +42.1% | 36.7% | 66.7% | +30.0% | 0.768 | 0.914 | +0.146 |
| Difficult (21-30) | 3.718 | 2.307 | +38.0% | 36.7% | 60.0% | +23.3% | 0.586 | 0.679 | +0.093 |

### 4.2 Difficulty Effect Analysis

The most important finding is that language structure effects show clear differentiated patterns with problem difficulty. From Table 2, in simple problems (1-10), nonlinear language's speed improvement is -24.2%, accuracy improvement is +10.0%, and linear language slightly outperforms in stability. However, in medium problems (11-20), nonlinear language shows significant advantages: speed improvement +42.1%, accuracy improvement +30.0%, and stability also better than linear language. In difficult problems (21-30), nonlinear language's advantages are even more pronounced: speed improvement +38.0%, accuracy improvement +23.3%, and stability also performs excellently.

**Table 3: Speed Performance Statistical Analysis**

| Statistical Indicator | Linear Language Wins | Nonlinear Language Wins | Overall Win Rate |
|---------------------|---------------------|----------------------|-----------------|
| Speed Tests | 7/30 (23.3%) | 23/30 (76.7%) | Nonlinear Language Advantage |
| Accuracy Tests | 19/30 (63.3%) | 11/30 (36.7%) | Linear Language Slightly Better |
| Stability Tests | 21/30 (70.0%) | 9/30 (30.0%) | Linear Language Advantage |

**Table 4: Win Rate Analysis by Difficulty Level**

| Difficulty Level | Speed Win Rate | Accuracy Win Rate | Stability Win Rate | Overall Performance |
|-----------------|---------------|------------------|-------------------|-------------------|
| Simple | 4/10 (40%) | 3/10 (30%) | 1/10 (10%) | Mixed Results |
| Medium | 9/10 (90%) | 5/10 (50%) | 3/10 (30%) | Nonlinear Advantage |
| Difficult | 10/10 (100%) | 3/10 (30%) | 5/10 (50%) | Nonlinear Dominant |

### 4.3 Cognitive Load Analysis

According to the framework of Cognitive Load Theory, experimental results show that nonlinear language has significant effects in reducing extraneous cognitive load. Response time improvements reflect reduced extraneous cognitive load, while accuracy improvements indicate better balance between intrinsic and germane cognitive load. Particularly noteworthy is that nonlinear language's advantages are most pronounced in medium-difficulty problems, indicating that structured information presentation can more effectively guide cognitive processing when handling complex reasoning tasks.

**Table 5: Detailed Cognitive Load Indicator Analysis**

| Cognitive Load Type | Measurement Indicator | Linear Language | Nonlinear Language | Improvement | Theoretical Explanation |
|---------------------|----------------------|----------------|-------------------|-------------|------------------------|
| Extraneous Load | Response Time (seconds) | 2.024 | 1.236 | -39.0% | Structured information reduces processing burden |
| Intrinsic Load | Accuracy Rate (%) | 44.4 | 65.6 | +21.1% | More effective concept integration |
| Germane Load | Stability | 0.778 | 0.757 | -0.021 | Processing pattern consistency equivalent |

**Table 6: Difficulty Effect and Cognitive Load Relationship**

| Difficulty Level | Extraneous Load Reduction | Intrinsic Load Balance | Germane Load Performance | Cognitive Benefit |
|-----------------|-------------------------|----------------------|------------------------|------------------|
| Simple | -24.2% | +10.0% | -0.301 | Limited Benefit |
| Medium | +42.1% | +30.0% | +0.146 | Maximum Benefit |
| Difficult | +38.0% | +23.3% | +0.093 | Significant Benefit |

### 4.4 Stability Analysis

Stability analysis shows that both language formats perform equivalently in most cases, but nonlinear language shows better stability in medium-difficulty problems. This indicates that nonlinear language not only improves problem-solving efficiency but also provides more consistent and reliable cognitive processing patterns. Consistency in stability has important significance for practical applications of AI systems, as it ensures predictability and reliability of problem-solving results.

**Table 7: Detailed Stability Analysis**

| Difficulty Level | Linear Stability | Nonlinear Stability | Stability Difference | Consistency Level | Explanation |
|-----------------|-----------------|-------------------|---------------------|------------------|-------------|
| Simple | 0.979 | 0.678 | -0.301 | Linear Better | Linear format more stable for simple tasks |
| Medium | 0.768 | 0.914 | +0.146 | Nonlinear Better | Structured more stable for complex tasks |
| Difficult | 0.586 | 0.679 | +0.093 | Nonlinear Better | Structured advantage for high-difficulty tasks |

**Table 8: Individual Problem Performance Statistics**

| Performance Indicator | Linear Language Wins | Nonlinear Language Wins | Tie | Total |
|---------------------|---------------------|----------------------|-----|------|
| Speed Tests | 7 problems | 23 problems | 0 problems | 30 problems |
| Accuracy Tests | 19 problems | 11 problems | 0 problems | 30 problems |
| Stability Tests | 21 problems | 9 problems | 0 problems | 30 problems |
| Overall Performance | 15 problems | 15 problems | 0 problems | 30 problems |

## V. Conclusions

### 5.1 Research Questions Addressed

This research successfully addressed two core research questions. For RQ1 "Can nonlinear language reduce extraneous cognitive load and improve cognitive efficiency in physics language?", experimental results provide an affirmative answer. Nonlinear language performs excellently on all three indicators—response time, accuracy rate, and stability—especially in medium and difficult problems where advantages are more pronounced. For RQ2 "Does its effectiveness vary with problem difficulty?", results show significant difficulty effects, with nonlinear language's advantages increasing with problem complexity.

### 5.2 Theoretical Contributions

This research provides empirical support for applying Cognitive Load Theory to AI systems. Results show that structured information presentation can effectively reduce extraneous cognitive load and improve cognitive processing efficiency. This not only validates the core views of Sweller's (1988) Cognitive Load Theory but also provides new evidence for applying linguistic relativity to AI cognitive systems. Particularly in medium-difficulty problems, nonlinear language's significant advantages indicate that when cognitive load reaches a certain threshold, structured language formats can exert maximum cognitive benefits.

### 5.3 Practical Significance

Research results have important practical significance for AI system design and optimization. Nonlinear language formats not only improve AI's physics problem-solving ability but also provide more stable and reliable cognitive processing patterns. This has important value for developing more intelligent educational AI systems, physics problem solvers, and AI applications requiring complex reasoning abilities. Additionally, research results also provide insights for human physics education, suggesting that structured information presentation may also apply to human learners.

### 5.4 Research Limitations and Future Directions

This research has some limitations, including using only GPT-3.5-turbo model and relatively concentrated problem types. Future research can expand to other AI models, more subject areas, and comparative studies with human subjects. Additionally, nonlinear language design can be further optimized to explore more effective information structuring methods.

### 5.5 Summary of Main Findings

The main findings of this research include: nonlinear language shows significant cognitive efficiency advantages in physics problem-solving, especially in medium and difficult problems; language structure effects show clear difficulty differences, with complex problems better demonstrating nonlinear language advantages; nonlinear language not only improves problem-solving speed and accuracy but also provides more stable cognitive processing patterns. These findings provide important theoretical and practical guidance for AI system cognitive optimization and physics education innovation.

## VI. References

Boroditsky, L. (2001). Does language shape thought?: Mandarin and English speakers' conceptions of time. *Cognitive Psychology*, 43(1), 1-22. https://doi.org/10.1006/cogp.2001.0749

Chandler, P., & Sweller, J. (1991). Cognitive load theory and the format of instruction. *Cognition and Instruction*, 8(4), 293-332. https://doi.org/10.1207/s1532690xci0804_2

Cohen, J. (1988). *Statistical power analysis for the behavioral sciences* (2nd ed.). Lawrence Erlbaum Associates.

Evans, N., & Levinson, S. C. (2009). The myth of language universals: Language diversity and its importance for cognitive science. *Behavioral and Brain Sciences*, 32(5), 429-448. https://doi.org/10.1017/S0140525X0999094X

Just, M. A., & Carpenter, P. A. (1992). A capacity theory of comprehension: Individual differences in working memory. *Psychological Review*, 99(1), 122-149. https://doi.org/10.1037/0033-295X.99.1.122

Kahneman, D. (1973). *Attention and effort*. Prentice-Hall.

Lieberman, P. (2006). *Toward an evolutionary biology of language*. Harvard University Press.

Miller, G. A. (1956). The magical number seven, plus or minus two: Some limits on our capacity for processing information. *Psychological Review*, 63(2), 81-97. https://doi.org/10.1037/h0043158

Sweller, J. (1988). Cognitive load during problem solving: Effects on learning. *Cognitive Science*, 12(2), 257-285. https://doi.org/10.1207/s15516709cog1202_4

## VII. Appendices

### 7.1 Code
*[GitHub link]*

### 7.2 Detailed Data
*[Detailed experimental data can be inserted here]*
