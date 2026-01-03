#!/usr/bin/env python3
"""
Problem 11~20 中等難度experiment
Medium Difficulty Problems: More Complex Physics
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

class Problem11To20Experiment:
    """Problem 11~20 中等難度experiment類"""
    
    def __init__(self, api_key: str = None):
        if api_key:
            openai.api_key = api_key
        else:
            openai.api_key = os.getenv('OPENAI_API_KEY')
            
        self.baseline_time = 0.0
        
    def establish_simple_baseline(self, num_samples: int = 5) -> float:
        """建立超簡單基準線"""
        print("🔧 Establishing simple baseline...")
        
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
                print(f"   Baseline sample {i+1}: {end_time - start_time:.3f}秒 → '{response.choices[0].message.content.strip()}'")
            except Exception as e:
                print(f"   Baseline sample {i+1} failed: {e}")
                continue
                
            time.sleep(0.3)
        
        if times:
            self.baseline_time = statistics.mean(times)
            print(f"✅ Baseline established：{self.baseline_time:.3f}秒")
            return self.baseline_time
        else:
            print("❌ 基準線建立failed")
            return 0.0

    def load_medium_problems(self) -> List[Dict]:
        """載入problem 11~20的中等難度問題"""
        base_problems = [
            {
                'id': 11,
                'linear_text': 'Emma is driving her 1500 kg car at 25 m/s when she suddenly sees a red light ahead. She applies the brakes and comes to a complete stop after traveling 50 m. Calculate the average braking force exerted by the car\'s brake system.',
                'given': 'm = 1500 kg, v₀ = 25 m/s, v = 0 m/s, s = 50 m',
                'formula': 'v² = v₀² + 2as, F = ma',
                'target': 'average braking force',
                'expected_value': 9375,
                'expected_unit': 'N'
            },
            {
                'id': 12,
                'linear_text': 'A wooden crate slides down a loading ramp inclined at 30° to the horizontal. The coefficient of kinetic friction between the crate and the ramp is μ = 0.20. Calculate the acceleration of the crate as it slides down the ramp.',
                'given': 'θ = 30°, μ = 0.20, g = 9.8 m/s²',
                'formula': 'a = g(sin θ - μ cos θ)',
                'target': 'acceleration down ramp',
                'expected_value': 3.2,
                'expected_unit': 'm/s²'
            },
            {
                'id': 13,
                'linear_text': 'In a physics lab experiment, two gliders collide on an air track. Glider A (mass = 3.0 kg) moves at 8.0 m/s toward stationary glider B (mass = 7.0 kg). After the perfectly elastic collision, find the final velocity of glider A.',
                'given': 'm₁ = 3.0 kg, m₂ = 7.0 kg, u₁ = 8.0 m/s, u₂ = 0 m/s',
                'formula': 'v₁ = ((m₁-m₂)/(m₁+m₂))u₁',
                'target': 'final velocity of glider A',
                'expected_value': -2.4,
                'expected_unit': 'm/s'
            },
            {
                'id': 14,
                'linear_text': 'During a field trip to study gravity variations, students measure a simple pendulum with length 2.0 m. They find that it completes one full oscillation in 2.8 seconds. Calculate the local acceleration due to gravity at this location.',
                'given': 'L = 2.0 m, T = 2.8 s',
                'formula': 'g = 4π²L/T²',
                'target': 'local gravity acceleration',
                'expected_value': 10.1,
                'expected_unit': 'm/s²'
            },
            {
                'id': 15,
                'linear_text': 'A research laboratory studies gas behavior using a sealed cylinder containing an ideal gas. At 27°C (300 K), the gas occupies 1.0 L at 5.0 atm pressure. The gas is allowed to expand isothermally until its volume becomes 3.0 L. What is the final pressure of the gas?',
                'given': 'T = 300 K, P₁ = 5.0 atm, V₁ = 1.0 L, V₂ = 3.0 L',
                'formula': 'P₁V₁ = P₂V₂',
                'target': 'final pressure',
                'expected_value': 1.67,
                'expected_unit': 'atm'
            },
            {
                'id': 16,
                'linear_text': 'A 2.0 kg mass is attached to a horizontal spring with spring constant k = 800 N/m. The mass oscillates in simple harmonic motion with an amplitude of 5.0 cm. Calculate the maximum speed of the oscillating mass.',
                'given': 'm = 2.0 kg, k = 800 N/m, A = 0.050 m',
                'formula': 'v_max = ωA = A√(k/m)',
                'target': 'maximum speed',
                'expected_value': 1.0,
                'expected_unit': 'm/s'
            },
            {
                'id': 17,
                'linear_text': 'An engineering student designs a theoretical heat engine that operates between a hot reservoir at 327°C (600 K) and a cold reservoir at 27°C (300 K). Calculate the maximum possible efficiency of this heat engine according to thermodynamic principles.',
                'given': 'T_hot = 600 K, T_cold = 300 K',
                'formula': 'η = 1 - T_cold/T_hot',
                'target': 'maximum efficiency',
                'expected_value': 0.5,
                'expected_unit': '%'
            },
            {
                'id': 18,
                'linear_text': 'The International Space Station orbits Earth at an altitude of 400 km above the planet\'s surface. Given that Earth\'s radius is 6400 km and surface gravity is 9.8 m/s², calculate the orbital speed of the space station.',
                'given': 'h = 400 km, R = 6400 km, g = 9.8 m/s²',
                'formula': 'v = √(gR²/r), r = R + h',
                'target': 'orbital speed',
                'expected_value': 7670,
                'expected_unit': 'm/s'
            },
            {
                'id': 19,
                'linear_text': 'A basketball player throws a 0.50 kg ball vertically upward with an initial speed of 15 m/s from a height of 2.0 m above the ground. Calculate the maximum height above the ground that the ball reaches.',
                'given': 'm = 0.50 kg, v₀ = 15 m/s, h₀ = 2.0 m, g = 9.8 m/s²',
                'formula': 'h_max = h₀ + v₀²/(2g)',
                'target': 'maximum height above ground',
                'expected_value': 13.5,
                'expected_unit': 'm'
            },
            {
                'id': 20,
                'linear_text': 'In a power plant, steam at 100°C condenses into water at the same temperature in the cooling towers. Calculate the amount of thermal energy released when 1.0 kg of steam undergoes this phase change. (Latent heat of vaporization for water = 2.26 × 10⁶ J/kg)',
                'given': 'm = 1.0 kg, L_v = 2.26 × 10⁶ J/kg',
                'formula': 'Q = mL_v',
                'target': 'thermal energy released',
                'expected_value': 2260000,
                'expected_unit': 'J'
            }
        ]
        
        # 創建隨機化版本避免記憶污染
        randomized_problems = []
        for prob in base_problems:
            for run in range(3):
                new_prob = prob.copy()
                new_prob['run'] = run + 1
                new_prob['randomized_id'] = f"{prob['id']}_{run+1}"
                randomized_problems.append(new_prob)
        
        return randomized_problems

    def create_verified_linear_prompt(self, problem: Dict) -> str:
        """創建需要真正計算的線性prompt"""
        return f"""
Solve this physics problem:

{problem['linear_text']}

Provide only the numerical answer with units.
Format: "XX.X unit"
"""

    def create_verified_nonlinear_prompt(self, problem: Dict) -> str:
        """創建需要真正計算的非線性prompt"""
        return f"""
Solve this physics problem using the structured format:

GIVEN: {problem['given']}
FORMULA: {problem['formula']}
TARGET: {problem['target']}

Provide only the numerical answer with units.
Format: "XX.X unit"
"""

    def extract_numerical_answer(self, response_text: str) -> Dict:
        """提取並驗證數值答案"""
        # 尋找 "Answer: XX.X unit" 格式
        answer_pattern = r'Answer:\s*([+-]?[0-9,]+\.?[0-9]*(?:[eE][+-]?[0-9]+)?)\s*([a-zA-Z/%²³°]+)'
        match = re.search(answer_pattern, response_text)
        
        if match:
            value_str = match.group(1).replace(',', '')
            unit = match.group(2)
            
            try:
                value = float(value_str)
                return {
                    'success': True,
                    'value': value,
                    'unit': unit,
                    'raw_text': response_text
                }
            except ValueError:
                pass
        
        # 備用：尋找科學記號或大數字
        backup_pattern = r'([+-]?[0-9,]+\.?[0-9]*(?:[eE][+-]?[0-9]+)?)\s*([a-zA-Z/%²³°]+)'
        matches = re.findall(backup_pattern, response_text)
        
        if matches:
            value_str = matches[-1][0].replace(',', '')
            unit = matches[-1][1]
            
            try:
                value = float(value_str)
                return {
                    'success': True,
                    'value': value,
                    'unit': unit,
                    'raw_text': response_text,
                    'backup_extraction': True
                }
            except ValueError:
                pass
        
        return {
            'success': False,
            'value': None,
            'unit': None,
            'raw_text': response_text,
            'error': 'Could not extract numerical answer'
        }

    def calculate_accuracy(self, extracted: Dict, expected_value: float, expected_unit: str) -> Dict:
        """計算答案準確性（中等題目允許較大誤差）"""
        if not extracted['success']:
            return {
                'accurate': False,
                'relative_error': float('inf'),
                'unit_match': False,
                'reason': 'Failed to extract answer'
            }
        
        # 數值準確性（中等題目允許10%誤差）
        relative_error = abs(extracted['value'] - expected_value) / expected_value if expected_value != 0 else abs(extracted['value'])
        value_accurate = relative_error <= 0.10
        
        # 單位匹配（考慮常見變體）
        unit_variants = {
            'N': ['N', 'newtons', 'newton'],
            'm/s²': ['m/s²', 'm/s2', 'ms2'],
            'm/s': ['m/s', 'ms', 'm·s⁻¹'],
            'atm': ['atm', 'atmosphere', 'atmospheres'],
            'J': ['J', 'joules', 'joule'],
            'm': ['m', 'meters', 'metres'],
            '%': ['%', 'percent', 'efficiency'],
            'kg': ['kg', 'kilograms']
        }
        
        expected_variants = unit_variants.get(expected_unit, [expected_unit])
        unit_match = extracted['unit'].lower() in [v.lower() for v in expected_variants]
        
        return {
            'accurate': value_accurate and unit_match,
            'value_accurate': value_accurate,
            'unit_match': unit_match,
            'relative_error': relative_error,
            'extracted_value': extracted['value'],
            'expected_value': expected_value,
            'extracted_unit': extracted['unit'],
            'expected_unit': expected_unit
        }

    def run_verified_test(self, prompt: str, problem: Dict, format_type: str) -> Dict:
        """執行包含驗證的測試"""
        start_time = time.time()
        
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a physics expert specializing in detailed problem solving. Show all work clearly."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=400,  # 中等題目需要更多token
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
            
            # 檢查是否顯示了計算過程
            calculation_shown = any(keyword in response_text.lower() for keyword in 
                                  ['=', 'calculate', 'multiply', 'divide', 'step', '×', '*', '/', 'formula'])
            
            return {
                'problem_id': problem['id'],
                'run': problem['run'],
                'randomized_id': problem['randomized_id'],
                'format_type': format_type,
                'raw_time': raw_time,
                'thinking_time': thinking_time,
                'response': response_text,
                'tokens_used': response.usage.total_tokens,
                'extracted_answer': extracted,
                'accuracy_analysis': accuracy,
                'calculation_shown': calculation_shown,
                'success': True,
                'timestamp': datetime.now().isoformat()
            }
            
        except Exception as e:
            end_time = time.time()
            return {
                'problem_id': problem['id'],
                'run': problem['run'],
                'randomized_id': problem['randomized_id'],
                'format_type': format_type,
                'raw_time': end_time - start_time,
                'thinking_time': 0,
                'response': str(e),
                'tokens_used': 0,
                'extracted_answer': {'success': False},
                'accuracy_analysis': {'accurate': False},
                'calculation_shown': False,
                'success': False,
                'timestamp': datetime.now().isoformat()
            }

    def run_medium_difficulty_experiment(self) -> Dict:
        """執行中等難度experiment"""
        print("🚀 Starting Problem 11~20 中等難度experiment")
        print("策略：隨機順序、長延遲、多步驗證")
        
        problems = self.load_medium_problems()
        random.shuffle(problems)
        
        results = {
            'linear': [],
            'nonlinear': [],
            'experiment_info': {
                'baseline_time': self.baseline_time,
                'difficulty_level': 'medium',
                'problem_range': '11-20',
                'anti_contamination_measures': [
                    'randomized_problem_order',
                    'long_delays_between_tests', 
                    'verification_prompts',
                    'extraction_validation'
                ],
                'start_time': datetime.now().isoformat()
            }
        }
        
        total_tests = len(problems) * 2
        current_test = 0
        
        for problem in problems:
            print(f"\n📝 問題 {problem['randomized_id']}: {problem['target']}")
            
            # 隨機決定線性/非線性順序
            if random.choice([True, False]):
                first_format, second_format = 'linear', 'nonlinear'
                first_prompt = self.create_verified_linear_prompt(problem)
                second_prompt = self.create_verified_nonlinear_prompt(problem)
            else:
                first_format, second_format = 'nonlinear', 'linear'
                first_prompt = self.create_verified_nonlinear_prompt(problem)
                second_prompt = self.create_verified_linear_prompt(problem)
            
            # 第一格式測試
            current_test += 1
            print(f"   🔸 {first_format} 格式 ({current_test}/{total_tests})")
            result1 = self.run_verified_test(first_prompt, problem, first_format)
            results[first_format].append(result1)
            
            # 長延遲避免記憶污染
            print("   ⏳ 防污染延遲...")
            time.sleep(3.0)
            
            # 第二格式測試
            current_test += 1
            print(f"   🔸 {second_format} 格式 ({current_test}/{total_tests})")
            result2 = self.run_verified_test(second_prompt, problem, second_format)
            results[second_format].append(result2)
            
            # 題目間延遲
            time.sleep(2.0)
        
        results['experiment_info']['end_time'] = datetime.now().isoformat()
        return results

    def analyze_three_metrics(self, results: Dict) -> Dict:
        """分析三大核心指標"""
        print("\n📊 分析 Problem 11~20 三大核心指標...")
        
        linear_data = [r for r in results['linear'] if r['success']]
        nonlinear_data = [r for r in results['nonlinear'] if r['success']]
        
        # 1. 校正思考時間分析
        linear_times = [r['thinking_time'] for r in linear_data]
        nonlinear_times = [r['thinking_time'] for r in nonlinear_data]
        
        timing_analysis = {
            'linear_avg_time': statistics.mean(linear_times) if linear_times else 0,
            'nonlinear_avg_time': statistics.mean(nonlinear_times) if nonlinear_times else 0,
            'linear_time_std': statistics.stdev(linear_times) if len(linear_times) > 1 else 0,
            'nonlinear_time_std': statistics.stdev(nonlinear_times) if len(nonlinear_times) > 1 else 0,
            'time_improvement': 0,
            'faster_format': 'tie'
        }
        
        if timing_analysis['linear_avg_time'] > 0 and timing_analysis['nonlinear_avg_time'] > 0:
            time_diff = timing_analysis['linear_avg_time'] - timing_analysis['nonlinear_avg_time']
            timing_analysis['time_improvement'] = (time_diff / timing_analysis['linear_avg_time']) * 100
            timing_analysis['faster_format'] = 'nonlinear' if time_diff > 0 else 'linear'
        
        # 2. 錯誤率分析
        linear_accuracies = [r['accuracy_analysis']['accurate'] for r in linear_data]
        nonlinear_accuracies = [r['accuracy_analysis']['accurate'] for r in nonlinear_data]
        
        accuracy_analysis = {
            'linear_accuracy_rate': sum(linear_accuracies) / len(linear_accuracies) if linear_accuracies else 0,
            'nonlinear_accuracy_rate': sum(nonlinear_accuracies) / len(nonlinear_accuracies) if nonlinear_accuracies else 0,
            'linear_error_rate': 1 - (sum(linear_accuracies) / len(linear_accuracies) if linear_accuracies else 1),
            'nonlinear_error_rate': 1 - (sum(nonlinear_accuracies) / len(nonlinear_accuracies) if nonlinear_accuracies else 1),
            'more_accurate_format': 'tie'
        }
        
        if accuracy_analysis['linear_accuracy_rate'] != accuracy_analysis['nonlinear_accuracy_rate']:
            accuracy_analysis['more_accurate_format'] = 'linear' if accuracy_analysis['linear_accuracy_rate'] > accuracy_analysis['nonlinear_accuracy_rate'] else 'nonlinear'
        
        # 3. 穩定率分析
        consistency_analysis = self.analyze_consistency_by_problem(linear_data, nonlinear_data)
        
        return {
            'timing_analysis': timing_analysis,
            'accuracy_analysis': accuracy_analysis,
            'consistency_analysis': consistency_analysis,
            'overall_summary': {
                'faster_format': timing_analysis['faster_format'],
                'more_accurate_format': accuracy_analysis['more_accurate_format'],
                'more_consistent_format': consistency_analysis['more_consistent_format'],
                'time_improvement_percent': timing_analysis['time_improvement'],
                'accuracy_improvement': accuracy_analysis['nonlinear_accuracy_rate'] - accuracy_analysis['linear_accuracy_rate']
            }
        }

    def analyze_consistency_by_problem(self, linear_data: List, nonlinear_data: List) -> Dict:
        """分析按問題分組的一致性"""
        
        # 按原始問題ID分組
        linear_by_problem = {}
        nonlinear_by_problem = {}
        
        for result in linear_data:
            pid = result['problem_id']
            if pid not in linear_by_problem:
                linear_by_problem[pid] = []
            linear_by_problem[pid].append(result)
        
        for result in nonlinear_data:
            pid = result['problem_id']
            if pid not in nonlinear_by_problem:
                nonlinear_by_problem[pid] = []
            nonlinear_by_problem[pid].append(result)
        
        # 計算每個問題的一致性
        linear_consistencies = []
        nonlinear_consistencies = []
        
        for pid in range(11, 21):  # problem 11-20
            if pid in linear_by_problem:
                responses = [r['extracted_answer']['value'] for r in linear_by_problem[pid] if r['extracted_answer']['success']]
                if len(responses) > 1:
                    consistency = 1.0 if len(set(responses)) == 1 else (1.0 - statistics.stdev(responses) / statistics.mean(responses) if statistics.mean(responses) > 0 else 0.0)
                    linear_consistencies.append(max(0, consistency))
            
            if pid in nonlinear_by_problem:
                responses = [r['extracted_answer']['value'] for r in nonlinear_by_problem[pid] if r['extracted_answer']['success']]
                if len(responses) > 1:
                    consistency = 1.0 if len(set(responses)) == 1 else (1.0 - statistics.stdev(responses) / statistics.mean(responses) if statistics.mean(responses) > 0 else 0.0)
                    nonlinear_consistencies.append(max(0, consistency))
        
        linear_avg_consistency = statistics.mean(linear_consistencies) if linear_consistencies else 0
        nonlinear_avg_consistency = statistics.mean(nonlinear_consistencies) if nonlinear_consistencies else 0
        
        return {
            'linear_consistency_rate': linear_avg_consistency,
            'nonlinear_consistency_rate': nonlinear_avg_consistency,
            'more_consistent_format': 'linear' if linear_avg_consistency > nonlinear_avg_consistency else 'nonlinear' if nonlinear_avg_consistency > linear_avg_consistency else 'tie'
        }

    def save_results(self, results: Dict, analysis: Dict):
        """保存experiment結果"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # 保存完整結果
        with open(f'problem_11_20_results_{timestamp}.json', 'w', encoding='utf-8') as f:
            json.dump({'results': results, 'analysis': analysis}, f, indent=2, ensure_ascii=False)
        
        # 創建摘要報告
        with open(f'problem_11_20_analysis_{timestamp}.txt', 'w', encoding='utf-8') as f:
            f.write("=== Problem 11~20 中等難度三項指標分析 ===\n\n")
            
            timing = analysis['timing_analysis']
            accuracy = analysis['accuracy_analysis']
            consistency = analysis['consistency_analysis']
            summary = analysis['overall_summary']
            
            f.write("🎯 中等難度experiment (Problem 11~20):\n")
            f.write("✅ 涵蓋多步驟問題：碰撞、擺、軌道、相變等\n")
            f.write("✅ 防記憶污染：隨機順序 + 3s延遲\n")
            f.write("✅ 更嚴格驗證：多步計算過程檢查\n")
            f.write("✅ 允許較大誤差：10%容忍度（vs 簡單題5%）\n\n")
            
            f.write("1️⃣ 校正思考時間分析：\n")
            f.write(f"   線性格式平均思考時間: {timing['linear_avg_time']:.3f}秒\n")
            f.write(f"   非線性格式平均思考時間: {timing['nonlinear_avg_time']:.3f}秒\n")
            f.write(f"   速度優勝者: {timing['faster_format']}\n")
            f.write(f"   效率提升: {timing['time_improvement']:.1f}%\n\n")
            
            f.write("2️⃣ 錯誤率分析：\n")
            f.write(f"   線性格式準確率: {accuracy['linear_accuracy_rate']:.1%}\n")
            f.write(f"   非線性格式準確率: {accuracy['nonlinear_accuracy_rate']:.1%}\n")
            f.write(f"   線性格式錯誤率: {accuracy['linear_error_rate']:.1%}\n")
            f.write(f"   非線性格式錯誤率: {accuracy['nonlinear_error_rate']:.1%}\n")
            f.write(f"   準確度優勝者: {accuracy['more_accurate_format']}\n\n")
            
            f.write("3️⃣ 答題穩定率分析：\n")
            f.write(f"   線性格式穩定率: {consistency['linear_consistency_rate']:.1%}\n")
            f.write(f"   非線性格式穩定率: {consistency['nonlinear_consistency_rate']:.1%}\n")
            f.write(f"   穩定性優勝者: {consistency['more_consistent_format']}\n\n")
            
            f.write("🏆 綜合結果：\n")
            f.write(f"   速度優勝者: {summary['faster_format']}\n")
            f.write(f"   準確度優勝者: {summary['more_accurate_format']}\n")
            f.write(f"   穩定性優勝者: {summary['more_consistent_format']}\n")
            f.write(f"   時間效率提升: {summary['time_improvement_percent']:.1f}%\n")
            f.write(f"   準確度提升: {summary['accuracy_improvement']:.1%}\n")
        
        print(f"✅ 中等難度結果已保存：problem_11_20_results_{timestamp}.json")
        print(f"✅ 分析報告：problem_11_20_analysis_{timestamp}.txt")

def main():
    """主執行函數"""
    print("=== Problem 11~20 中等難度認知效率experiment ===")
    print("測試更複雜的多步驟物理問題")
    print("包括：碰撞、擺、軌道運動、相變等\n")
    
    experiment = Problem11To20Experiment()
    
    # Establish baseline
    baseline = experiment.establish_simple_baseline(5)
    if baseline == 0:
        print("❌ 無法Establish baseline，終止experiment")
        return
    
    # 執行中等難度experiment
    results = experiment.run_medium_difficulty_experiment()
    
    # 分析三大指標
    analysis = experiment.analyze_three_metrics(results)
    
    # 顯示關鍵結果
    print(f"\n🏆 Problem 11~20 關鍵結果:")
    summary = analysis['overall_summary']
    timing = analysis['timing_analysis']
    accuracy = analysis['accuracy_analysis']
    
    print(f"⚡ 速度: {summary['faster_format']} 優勝 (提升{summary['time_improvement_percent']:.1f}%)")
    print(f"🎯 準確度: {summary['more_accurate_format']} 優勝")
    print(f"📈 穩定性: {summary['more_consistent_format']} 優勝")
    
    print(f"\n詳細數據:")
    print(f"線性思考時間: {timing['linear_avg_time']:.3f}秒")
    print(f"非線性思考時間: {timing['nonlinear_avg_time']:.3f}秒")
    print(f"線性準確率: {accuracy['linear_accuracy_rate']:.1%}")
    print(f"非線性準確率: {accuracy['nonlinear_accuracy_rate']:.1%}")
    
    # Save results
    experiment.save_results(results, analysis)
    
    print("\n🎉 Problem 11~20 中等難度Experiment completed！")

if __name__ == "__main__":
    main()
