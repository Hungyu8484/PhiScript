#!/usr/bin/env python3
"""
New Problem 1-10 Experiment: 3 runs per problem, unified prompt format
"""

import openai
import time
import json
import statistics
import random
import re
from typing import Dict, List
from datetime import datetime
import os

class NewProblem1To10Experiment:
    """New Problem 1-10 Experiment Class"""
    
    def __init__(self, api_key: str = None):
        if api_key:
            openai.api_key = api_key
        else:
            openai.api_key = os.getenv('OPENAI_API_KEY')
            
        self.baseline_time = 0.0
        
    def establish_baseline(self, num_samples: int = 5) -> float:
        """Establish baseline response time"""
        print("🔧 Establishing baseline...")
        
        simple_prompts = ["hello", "hi", "ok", "yes", "1"]
        times = []
        
        for i in range(num_samples):
            prompt = simple_prompts[i % len(simple_prompts)]
            start_time = time.time()
            
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=10,
                    temperature=0.0
                )
                end_time = time.time()
                times.append(end_time - start_time)
                print(f"   Baseline sample {i+1}: {end_time - start_time:.3f}s")
            except Exception as e:
                print(f"   Baseline sample {i+1} failed: {e}")
                continue
                
            time.sleep(0.3)
        
        if times:
            self.baseline_time = statistics.mean(times)
            print(f"✅ Baseline established: {self.baseline_time:.3f}s")
            return self.baseline_time
        else:
            print("❌ Baseline establishment failed")
            return 0.0

    def create_linear_prompt(self, problem: Dict) -> str:
        """Create linear language prompt - unified format"""
        return f"""
Solve this physics problem:

{problem['linear_text']}

Provide only the numerical answer with units.
Format: "XX.X unit"
"""

    def create_nonlinear_prompt(self, problem: Dict) -> str:
        """Create nonlinear language prompt - unified format"""
        return f"""
Solve this physics problem using the structured format:

GIVEN: {problem['given']}
FORMULA: {problem['formula']}
TARGET: {problem['target']}

Provide only the numerical answer with units.
Format: "XX.X unit"
"""

    def extract_numerical_answer(self, response_text: str) -> Dict:
        """Extract numerical answer - simplified version"""
        text = response_text.strip()
        
        # Find numerical value + unit pattern
        patterns = [
            # Standard format: "XX.X unit"
            r'([+-]?[0-9,]+\.?[0-9]*(?:[eE][+-]?[0-9]+)?)\s*([a-zA-Z/%²³°]+)',
            # Pure number
            r'([+-]?[0-9,]+\.?[0-9]*(?:[eE][+-]?[0-9]+)?)'
        ]
        
        for pattern in patterns:
            matches = re.findall(pattern, text)
            if matches:
                match = matches[-1]  # Take the last match
                if isinstance(match, tuple) and len(match) >= 2:
                    value_str = match[0].replace(',', '')
                    unit = match[1] if match[1] else ''
                else:
                    value_str = str(match).replace(',', '')
                    unit = ''
                
                try:
                    value = float(value_str)
                    return {
                        'success': True,
                        'value': value,
                        'unit': unit,
                        'raw_text': response_text
                    }
                except ValueError:
                    continue
        
        return {
            'success': False,
            'value': None,
            'unit': None,
            'raw_text': response_text
        }

    def calculate_accuracy(self, extracted: Dict, expected_value: float, expected_unit: str) -> Dict:
        """Calculate accuracy"""
        if not extracted['success']:
            return {
                'accurate': False,
                'value_accurate': False,
                'unit_match': False,
                'relative_error': float('inf'),
                'extracted_value': None,
                'expected_value': expected_value,
                'extracted_unit': None,
                'expected_unit': expected_unit
            }
        
        # Check numerical accuracy
        extracted_value = extracted['value']
        value_accurate = abs(extracted_value - expected_value) / expected_value < 0.05  # 5% tolerance
        
        # Check unit matching
        unit_variants = {
            'km/h': ['km/h', 'kmh', 'km/hr'],
            'm': ['m', 'meters', 'meter'],
            'N': ['N', 'newtons', 'newton'],
            'J': ['J', 'joules', 'joule'],
            'm/s²': ['m/s²', 'm/s^2', 'm/s2', 'm/s/s'],
            'L': ['L', 'l', 'liters', 'liter'],
            's': ['s', 'seconds', 'second']
        }
        
        expected_variants = unit_variants.get(expected_unit, [expected_unit])
        unit_match = extracted['unit'].lower() in [v.lower() for v in expected_variants]
        
        relative_error = abs(extracted_value - expected_value) / expected_value if expected_value != 0 else float('inf')
        
        return {
            'accurate': value_accurate and unit_match,
            'value_accurate': value_accurate,
            'unit_match': unit_match,
            'relative_error': relative_error,
            'extracted_value': extracted_value,
            'expected_value': expected_value,
            'extracted_unit': extracted['unit'],
            'expected_unit': expected_unit
        }

    def run_single_test(self, prompt: str, problem: Dict, format_type: str, run_num: int) -> Dict:
        """Run single test"""
        start_time = time.time()
        
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a physics expert. Provide precise numerical answers only."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=50,   # Strictly limit tokens to force concise answers
                temperature=0.1
            )
            
            end_time = time.time()
            raw_time = end_time - start_time
            thinking_time = max(0, raw_time - self.baseline_time)
            
            response_text = response.choices[0].message.content.strip()
            
            # Extract numerical answer
            extracted = self.extract_numerical_answer(response_text)
            
            # Calculate accuracy
            accuracy = self.calculate_accuracy(
                extracted, 
                problem['expected_value'], 
                problem['expected_unit']
            )
            
            return {
                'problem_id': problem['id'],
                'format_type': format_type,
                'run_number': run_num,
                'raw_time': raw_time,
                'thinking_time': thinking_time,
                'response': response_text,
                'extracted_answer': extracted,
                'accuracy_analysis': accuracy,
                'tokens_used': response.usage.total_tokens,
                'success': True,
                'timestamp': datetime.now().isoformat()
            }
            
        except Exception as e:
            end_time = time.time()
            return {
                'problem_id': problem['id'],
                'format_type': format_type,
                'run_number': run_num,
                'raw_time': end_time - start_time,
                'thinking_time': 0,
                'response': str(e),
                'extracted_answer': {'success': False, 'value': None, 'unit': None},
                'accuracy_analysis': {'accurate': False, 'value_accurate': False, 'unit_match': False},
                'tokens_used': 0,
                'success': False,
                'timestamp': datetime.now().isoformat()
            }

    def load_problems_1_to_10(self) -> List[Dict]:
        """Load problems 1-10"""
        return [
            {
                'id': 1,
                'linear_text': 'Jessica drives her car from home to school, covering a distance of 120 km. The trip takes exactly 2 hours due to morning traffic. Calculate Jessica\'s average speed during this journey.',
                'given': 'Distance = 120 km, Time = 2 hours',
                'formula': 'v = d/t',
                'target': 'average speed',
                'expected_value': 60.0,
                'expected_unit': 'km/h'
            },
            {
                'id': 2,
                'linear_text': 'During a physics demonstration, Mr. Chen drops a tennis ball from the school roof. The ball falls freely for 3.0 seconds before hitting the ground. Calculate the height of the school building. (Take g = 9.8 m/s²)',
                'given': 'Time = 3.0 s, g = 9.8 m/s²',
                'formula': 'h = ½gt²',
                'target': 'height',
                'expected_value': 44.1,
                'expected_unit': 'm'
            },
            {
                'id': 3,
                'linear_text': 'A delivery truck with mass 1500 kg needs to accelerate at 5.0 m/s² to merge safely into highway traffic. What net force must the engine provide to achieve this acceleration?',
                'given': 'Mass = 1500 kg, Acceleration = 5.0 m/s²',
                'formula': 'F = ma',
                'target': 'net force',
                'expected_value': 7500.0,
                'expected_unit': 'N'
            },
            {
                'id': 4,
                'linear_text': 'In the school laboratory, Sarah compresses a spring with spring constant k = 200 N/m by a distance of 0.10 m using a force meter. Calculate the elastic potential energy stored in the compressed spring.',
                'given': 'k = 200 N/m, x = 0.10 m',
                'formula': 'PE = ½kx²',
                'target': 'elastic potential energy',
                'expected_value': 1.0,
                'expected_unit': 'J'
            },
            {
                'id': 5,
                'linear_text': 'A chemistry student needs to heat 2.0 kg of water from 20°C to 30°C for an experiment. How much thermal energy must be supplied to the water? (Specific heat capacity of water = 4200 J/kg·°C)',
                'given': 'm = 2.0 kg, ΔT = 10°C, c = 4200 J/kg·°C',
                'formula': 'Q = mcΔT',
                'target': 'thermal energy',
                'expected_value': 84000.0,
                'expected_unit': 'J'
            },
            {
                'id': 6,
                'linear_text': 'A hockey puck with mass 0.16 kg slides across the ice with a constant velocity of 8.0 m/s. Calculate the kinetic energy of the moving puck.',
                'given': 'm = 0.16 kg, v = 8.0 m/s',
                'formula': 'KE = ½mv²',
                'target': 'kinetic energy',
                'expected_value': 5.12,
                'expected_unit': 'J'
            },
            {
                'id': 7,
                'linear_text': 'A cyclist starts from rest and accelerates uniformly, reaching a speed of 20 m/s after 4.0 seconds. Calculate the cyclist\'s acceleration during this period.',
                'given': 'v₀ = 0 m/s, v = 20 m/s, t = 4.0 s',
                'formula': 'a = (v - v₀)/t',
                'target': 'acceleration',
                'expected_value': 5.0,
                'expected_unit': 'm/s²'
            },
            {
                'id': 8,
                'linear_text': 'A sealed balloon contains gas at 27°C (300 K) with a volume of 2.0 L. The balloon is heated at constant pressure until the temperature reaches 177°C (450 K). Find the new volume of the gas in the balloon.',
                'given': 'T₁ = 300 K, V₁ = 2.0 L, T₂ = 450 K',
                'formula': 'V₁/T₁ = V₂/T₂ (Charles\'s Law)',
                'target': 'new volume',
                'expected_value': 3.0,
                'expected_unit': 'L'
            },
            {
                'id': 9,
                'linear_text': 'An astronaut\'s equipment has a mass of 15 kg on Earth. Calculate the weight (gravitational force) acting on this equipment at Earth\'s surface. (g = 9.8 m/s²)',
                'given': 'm = 15 kg, g = 9.8 m/s²',
                'formula': 'W = mg',
                'target': 'weight',
                'expected_value': 147.0,
                'expected_unit': 'N'
            },
            {
                'id': 10,
                'linear_text': 'A soccer ball is kicked horizontally from a cliff with an initial speed of 25 m/s. The cliff is 20 m high above the beach below. How long will the ball remain in the air before hitting the sand?',
                'given': 'v₀ = 25 m/s, h = 20 m, g = 9.8 m/s²',
                'formula': 'h = ½gt²',
                'target': 'time of flight',
                'expected_value': 2.02,
                'expected_unit': 's'
            }
        ]

    def run_full_experiment(self) -> Dict:
        """Run full experiment (3 runs per problem)"""
        print("🚀 Starting new Problem 1-10 experiment...")
        
        # Establish baseline
        self.establish_baseline()
        
        # Load problems
        problems = self.load_problems_1_to_10()
        
        results = {
            'experiment_info': {
                'timestamp': datetime.now().isoformat(),
                'total_problems': len(problems),
                'runs_per_problem': 3,
                'baseline_time': self.baseline_time,
                'model': 'gpt-3.5-turbo',
                'max_tokens': 50,
                'temperature': 0.1
            },
            'linear': [],
            'nonlinear': []
        }
        
        for problem in problems:
            print(f"\n📝 Testing problem {problem['id']}: {problem['target']}")
            
            # Linear language test - 3 runs
            for run in range(3):
                linear_prompt = self.create_linear_prompt(problem)
                linear_result = self.run_single_test(linear_prompt, problem, 'linear', run + 1)
                results['linear'].append(linear_result)
                print(f"   Linear Run {run+1}: {linear_result['response'][:30]}...")
                
                time.sleep(0.5)  # Avoid rate limit
            
            # Nonlinear language test - 3 runs
            for run in range(3):
                nonlinear_prompt = self.create_nonlinear_prompt(problem)
                nonlinear_result = self.run_single_test(nonlinear_prompt, problem, 'nonlinear', run + 1)
                results['nonlinear'].append(nonlinear_result)
                print(f"   Nonlinear Run {run+1}: {nonlinear_result['response'][:30]}...")
                
                time.sleep(0.5)  # Avoid rate limit
        
        # Save results
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"new_problem_1_10_results_{timestamp}.json"
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
        
        print(f"\n✅ Experiment completed! Results saved to: {filename}")
        
        # 分析結果
        self.analyze_results(results)
        
        return results

    def analyze_results(self, results: Dict):
        """分析experiment結果"""
        print("\n📊 結果分析:")
        
        for format_type in ['linear', 'nonlinear']:
            format_results = results[format_type]
            
            # 計算各項指標
            avg_time = statistics.mean([r['thinking_time'] for r in format_results])
            success_rate = sum(1 for r in format_results if r['success']) / len(format_results)
            accuracy_rate = sum(1 for r in format_results if r['accuracy_analysis']['accurate']) / len(format_results)
            
            # 計算一致性（3 runs per problem回答的一致性）
            consistency_scores = []
            for problem_id in range(1, 11):
                problem_responses = [r['response'] for r in format_results if r['problem_id'] == problem_id]
                consistency = len(set(problem_responses)) / len(problem_responses) if problem_responses else 0
                consistency_scores.append(consistency)
            
            avg_consistency = statistics.mean(consistency_scores)
            
            # 計算平均token使用量
            avg_tokens = statistics.mean([r['tokens_used'] for r in format_results if r['success']])
            
            print(f"\n{format_type.upper()} 格式:")
            print(f"  平均思考時間: {avg_time:.3f}秒")
            print(f"  成功率: {success_rate:.1%}")
            print(f"  準確率: {accuracy_rate:.1%}")
            print(f"  一致性: {avg_consistency:.1%}")
            print(f"  平均token使用: {avg_tokens:.1f}")
            
            # 顯示每題的詳細結果
            print(f"  各題結果:")
            for problem_id in range(1, 11):
                problem_results = [r for r in format_results if r['problem_id'] == problem_id]
                if problem_results:
                    responses = [r['response'] for r in problem_results]
                    accuracies = [r['accuracy_analysis']['accurate'] for r in problem_results]
                    times = [r['thinking_time'] for r in problem_results]
                    
                    print(f"    問題{problem_id}: 準確率={sum(accuracies)/len(accuracies):.1%}, "
                          f"平均時間={statistics.mean(times):.3f}s, "
                          f"回答={responses[0][:20]}...")

if __name__ == "__main__":
    experiment = NewProblem1To10Experiment()
    results = experiment.run_full_experiment()
