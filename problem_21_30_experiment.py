#!/usr/bin/env python3
"""
Problem 21~30 高難度experiment
Challenging Difficulty Problems: Advanced Physics Concepts
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

class Problem21To30Experiment:
    """Problem 21~30 高難度experiment類"""
    
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

    def load_challenging_problems(self) -> List[Dict]:
        """載入problem 21~30的高難度問題"""
        base_problems = [
            {
                'id': 21,
                'linear_text': 'An advanced robotics project involves a rotating system where a uniform metal rod of length L and mass M rotates about one end. An additional component (point mass m) is attached at distance d from the rotation axis. When the entire system rotates with angular velocity ω, determine the total rotational kinetic energy of this composite system.',
                'given': 'L = rod length, M = rod mass, m = point mass, d = distance from axis, ω = angular velocity',
                'formula': 'KE_total = ½I_rod ω² + ½I_point ω², I_rod = ⅓ML², I_point = md²',
                'target': 'total rotational kinetic energy',
                'expected_value': 'symbolic',  # Will need special handling
                'expected_unit': 'symbolic'
            },
            {
                'id': 22,
                'linear_text': 'A solid cylindrical wheel rolls without slipping down a frictionless inclined ramp of angle θ. Using energy conservation principles, derive a general expression for the cylinder\'s linear acceleration down the incline in terms of the angle θ and gravitational acceleration g.',
                'given': 'θ = incline angle, g = 9.8 m/s², rolling without slipping',
                'formula': 'Energy: mgh = ½mv² + ½Iω², I = ½mr², v = ωr',
                'target': 'linear acceleration down incline',
                'expected_value': 'symbolic',
                'expected_unit': 'symbolic'
            },
            {
                'id': 23,
                'linear_text': 'A graduate student analyzes an ideal Carnot cycle where the working gas undergoes isothermal expansion at 400 K from 1.0 L to 4.0 L, followed by adiabatic expansion to 300 K. In the subsequent isothermal compression step at 300 K, determine the volume compression ratio (V_initial/V_final for this step).',
                'given': 'T_hot = 400 K, V₁ = 1.0 L, V₂ = 4.0 L, T_cold = 300 K',
                'formula': 'Carnot cycle: TV^(γ-1) = const, γ = 1.4',
                'target': 'volume compression ratio',
                'expected_value': 3.0,
                'expected_unit': 'ratio'
            },
            {
                'id': 24,
                'linear_text': 'An amusement park designs a loop-the-loop track where a solid sphere of radius R rolls down from rest and enters a circular vertical loop of radius 5R. Calculate the minimum height h from which the sphere must be released to just complete the loop (maintain contact at the top).',
                'given': 'sphere radius = R, loop radius = 5R, solid sphere I = (2/5)mr²',
                'formula': 'Energy: mgh = mg(10R) + ½mv² + ½Iω², v = ωr',
                'target': 'minimum release height',
                'expected_value': 2.7,  # in units of R
                'expected_unit': 'R'
            },
            {
                'id': 25,
                'linear_text': 'In an advanced physics laboratory, two identical pendulums of length L and mass m are weakly coupled by a horizontal spring of spring constant k attached at distance d below their pivot points. For small oscillations, find the two normal mode frequencies of this coupled oscillator system.',
                'given': 'L = pendulum length, m = mass, k = spring constant, d = spring position',
                'formula': 'Normal modes: ω₁ = √(g/L), ω₂ = √(g/L + 2kd²/mL²)',
                'target': 'normal mode frequencies',
                'expected_value': 'symbolic',
                'expected_unit': 'symbolic'
            },
            {
                'id': 26,
                'linear_text': 'A thermodynamics researcher studies a gas that undergoes a polytropic process described by PV^n = constant, where n = 1.3. The gas expands from an initial state of 2.0 L at 5.0 atm to a final volume of 6.0 L. Calculate the work done by the gas during this expansion process.',
                'given': 'n = 1.3, P₁ = 5.0 atm, V₁ = 2.0 L, V₂ = 6.0 L',
                'formula': 'W = (P₁V₁ - P₂V₂)/(n-1), P₁V₁ⁿ = P₂V₂ⁿ',
                'target': 'work done by gas',
                'expected_value': 1215,
                'expected_unit': 'J'
            },
            {
                'id': 27,
                'linear_text': 'A space agency designs a rocket that burns fuel at a constant rate dm/dt = -α (where α is positive) and ejects the burned fuel at speed v_e relative to the rocket. Derive an expression for the rocket\'s acceleration when its instantaneous mass is M, considering both thrust and gravitational effects.',
                'given': 'dm/dt = -α, v_e = exhaust velocity, M = instantaneous mass, g = 9.8 m/s²',
                'formula': 'F_thrust = αv_e, F_gravity = Mg, F_net = Ma',
                'target': 'rocket acceleration',
                'expected_value': 'symbolic',
                'expected_unit': 'symbolic'
            },
            {
                'id': 28,
                'linear_text': 'A theoretical physics problem involves a small bead constrained to slide without friction on a wire bent into the parabolic shape y = x²/(4a), where a is a positive constant. Under the influence of gravity, derive the equation of motion for small oscillations of the bead about the lowest point of the wire.',
                'given': 'y = x²/(4a), a = positive constant, gravity g',
                'formula': 'V(x) = mgy = mgx²/(4a), F = -dV/dx',
                'target': 'equation of motion',
                'expected_value': 'symbolic',
                'expected_unit': 'symbolic'
            },
            {
                'id': 29,
                'linear_text': 'An advanced thermodynamics course examines a three-step cycle for an ideal monatomic gas: (1→2) isothermal expansion at 300 K from 1.0 L to 3.0 L, (2→3) isobaric cooling to 200 K, (3→1) isochoric heating back to initial state. Calculate the thermal efficiency of this heat engine cycle.',
                'given': 'T₁ = T₂ = 300 K, T₃ = 200 K, V₁ = 1.0 L, V₂ = 3.0 L, monatomic gas',
                'formula': 'Q = nCₚΔT (isobaric), Q = nCᵥΔT (isochoric), Q = nRT ln(V₂/V₁) (isothermal)',
                'target': 'thermal efficiency',
                'expected_value': 47.9,
                'expected_unit': '%'
            },
            {
                'id': 30,
                'linear_text': 'A mechanical engineering project involves a uniform thin rod of length L and mass M that can rotate freely about a horizontal axis passing through one end. The rod is initially held in a horizontal position and then released. Using energy conservation, find the angular velocity of the rod when it reaches the vertical position.',
                'given': 'L = rod length, M = rod mass, I = ⅓ML²',
                'formula': 'Energy conservation: PE_initial = KE_final, Mg(L/2) = ½Iω²',
                'target': 'angular velocity at vertical position',
                'expected_value': 'symbolic',
                'expected_unit': 'symbolic'
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
FORMULAS: {problem['formula']}
TARGET: {problem['target']}

Provide only the numerical answer with units.
Format: "XX.X unit"
"""

    def extract_answer_advanced(self, response_text: str, problem_id: int) -> Dict:
        """提取高級問題的答案（包含符號解）"""
        
        # 對於需要數值答案的問題
        numerical_problems = {23: 3.0, 24: 2.7, 26: 1215, 29: 47.9}
        
        if problem_id in numerical_problems:
            # 尋找數值答案
            answer_pattern = r'Answer:\s*([+-]?[0-9,]+\.?[0-9]*)\s*([a-zA-Z/%²³°]*)'
            match = re.search(answer_pattern, response_text)
            
            if match:
                value_str = match.group(1).replace(',', '')
                unit = match.group(2) if match.group(2) else ''
                
                try:
                    value = float(value_str)
                    return {
                        'success': True,
                        'value': value,
                        'unit': unit,
                        'raw_text': response_text,
                        'type': 'numerical'
                    }
                except ValueError:
                    pass
        
        # 對於符號解答案，檢查是否包含關鍵符號
        symbolic_keywords = {
            21: ['ML²', 'md²', 'ω²'],
            22: ['g', 'sin', 'θ', '2/3'],
            25: ['√(g/L)', 'kd²', 'mL²'],
            27: ['αv_e/M', 'g'],
            28: ['g/2a', 'x'],
            30: ['√(3g/L)', 'ω']
        }
        
        if problem_id in symbolic_keywords:
            keywords = symbolic_keywords[problem_id]
            found_keywords = sum(1 for keyword in keywords if keyword in response_text)
            
            if found_keywords >= len(keywords) // 2:  # 至少找到一半關鍵詞
                return {
                    'success': True,
                    'value': f'symbolic_{found_keywords}/{len(keywords)}',
                    'unit': 'symbolic',
                    'raw_text': response_text,
                    'type': 'symbolic',
                    'keywords_found': found_keywords,
                    'keywords_total': len(keywords)
                }
        
        # 備用：檢查是否包含任何物理公式
        formula_indicators = ['=', '√', 'sin', 'cos', 'ln', '²', '³', 'π', 'α', 'ω', 'θ']
        formula_score = sum(1 for indicator in formula_indicators if indicator in response_text)
        
        if formula_score >= 3:
            return {
                'success': True,
                'value': f'formula_attempt_{formula_score}',
                'unit': 'attempt',
                'raw_text': response_text,
                'type': 'attempt',
                'formula_score': formula_score
            }
        
        return {
            'success': False,
            'value': None,
            'unit': None,
            'raw_text': response_text,
            'type': 'failed',
            'error': 'Could not extract meaningful answer'
        }

    def calculate_accuracy_advanced(self, extracted: Dict, expected_value, expected_unit: str, problem_id: int) -> Dict:
        """計算高級問題的準確性"""
        if not extracted['success']:
            return {
                'accurate': False,
                'relative_error': float('inf'),
                'unit_match': False,
                'reason': 'Failed to extract answer'
            }
        
        # 數值問題的準確性檢查
        if extracted['type'] == 'numerical' and isinstance(expected_value, (int, float)):
            relative_error = abs(extracted['value'] - expected_value) / expected_value if expected_value != 0 else abs(extracted['value'])
            value_accurate = relative_error <= 0.15  # 高難度問題允許15%誤差
            
            # 單位匹配
            unit_variants = {
                'ratio': ['ratio', '', '1', 'dimensionless'],
                'R': ['R', 'r', 'radius'],
                'J': ['J', 'joules', 'joule'],
                '%': ['%', 'percent']
            }
            
            expected_variants = unit_variants.get(expected_unit, [expected_unit])
            unit_match = extracted['unit'].lower() in [v.lower() for v in expected_variants]
            
            return {
                'accurate': value_accurate and unit_match,
                'value_accurate': value_accurate,
                'unit_match': unit_match,
                'relative_error': relative_error,
                'extracted_value': extracted['value'],
                'expected_value': expected_value
            }
        
        # 符號問題的準確性檢查
        elif extracted['type'] == 'symbolic':
            keywords_ratio = extracted.get('keywords_found', 0) / extracted.get('keywords_total', 1)
            symbolic_accurate = keywords_ratio >= 0.5  # 至少找到50%的關鍵詞
            
            return {
                'accurate': symbolic_accurate,
                'value_accurate': symbolic_accurate,
                'unit_match': True,  # 符號解不檢查單位
                'relative_error': 1.0 - keywords_ratio,
                'keywords_ratio': keywords_ratio
            }
        
        # 嘗試性回答的檢查
        elif extracted['type'] == 'attempt':
            attempt_score = extracted.get('formula_score', 0)
            attempt_accurate = attempt_score >= 5  # 至少包含5個公式指標
            
            return {
                'accurate': attempt_accurate,
                'value_accurate': attempt_accurate,
                'unit_match': True,
                'relative_error': max(0, 1.0 - attempt_score / 10),
                'attempt_score': attempt_score
            }
        
        return {
            'accurate': False,
            'value_accurate': False,
            'unit_match': False,
            'relative_error': 1.0,
            'reason': 'Unknown answer type'
        }

    def run_verified_test(self, prompt: str, problem: Dict, format_type: str) -> Dict:
        """執行包含驗證的測試"""
        start_time = time.time()
        
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are an expert theoretical physicist. Solve advanced problems with rigorous mathematical derivations."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=500,  # 高難度問題需要更多token
                temperature=0.1
            )
            
            end_time = time.time()
            raw_time = end_time - start_time
            thinking_time = max(0, raw_time - self.baseline_time)
            
            response_text = response.choices[0].message.content.strip()
            
            # 提取答案
            extracted = self.extract_answer_advanced(response_text, problem['id'])
            
            # Calculate accuracy
            accuracy = self.calculate_accuracy_advanced(
                extracted, 
                problem['expected_value'], 
                problem['expected_unit'],
                problem['id']
            )
            
            # 檢查是否顯示了推導過程
            derivation_keywords = ['derive', 'conservation', 'energy', 'momentum', 'equation', 'substitute', 'therefore', 'hence']
            derivation_shown = sum(1 for keyword in derivation_keywords if keyword.lower() in response_text.lower()) >= 2
            
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
                'derivation_shown': derivation_shown,
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
                'derivation_shown': False,
                'success': False,
                'timestamp': datetime.now().isoformat()
            }

    def run_challenging_experiment(self) -> Dict:
        """執行高難度experiment"""
        print("🚀 Starting Problem 21~30 高難度experiment")
        print("策略：隨機順序、長延遲、深度驗證")
        print("包含：刚体力學、熱力學循環、耦合振動、火箭推進等")
        
        problems = self.load_challenging_problems()
        random.shuffle(problems)
        
        results = {
            'linear': [],
            'nonlinear': [],
            'experiment_info': {
                'baseline_time': self.baseline_time,
                'difficulty_level': 'challenging',
                'problem_range': '21-30',
                'concepts': [
                    'rigid_body_mechanics',
                    'thermodynamic_cycles', 
                    'coupled_oscillations',
                    'variable_mass_systems',
                    'constrained_motion',
                    'advanced_energy_conservation'
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
            time.sleep(4.0)  # 高難度問題需要更長延遲
            
            # 第二格式測試
            current_test += 1
            print(f"   🔸 {second_format} 格式 ({current_test}/{total_tests})")
            result2 = self.run_verified_test(second_prompt, problem, second_format)
            results[second_format].append(result2)
            
            # 題目間延遲
            time.sleep(3.0)
        
        results['experiment_info']['end_time'] = datetime.now().isoformat()
        return results

    def analyze_three_metrics(self, results: Dict) -> Dict:
        """分析三大核心指標"""
        print("\n📊 分析 Problem 21~30 三大核心指標...")
        
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
        
        # 對於高難度問題，一致性基於答案類型的一致性
        linear_consistencies = []
        nonlinear_consistencies = []
        
        for pid in range(21, 31):  # problem 21-30
            if pid in linear_by_problem:
                answer_types = [r['extracted_answer'].get('type', 'failed') for r in linear_by_problem[pid]]
                consistency = len(set(answer_types)) == 1  # 所有答案類型相同
                linear_consistencies.append(1.0 if consistency else 0.5)
            
            if pid in nonlinear_by_problem:
                answer_types = [r['extracted_answer'].get('type', 'failed') for r in nonlinear_by_problem[pid]]
                consistency = len(set(answer_types)) == 1
                nonlinear_consistencies.append(1.0 if consistency else 0.5)
        
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
        with open(f'problem_21_30_results_{timestamp}.json', 'w', encoding='utf-8') as f:
            json.dump({'results': results, 'analysis': analysis}, f, indent=2, ensure_ascii=False)
        
        # 創建摘要報告
        with open(f'problem_21_30_analysis_{timestamp}.txt', 'w', encoding='utf-8') as f:
            f.write("=== Problem 21~30 高難度三項指標分析 ===\n\n")
            
            timing = analysis['timing_analysis']
            accuracy = analysis['accuracy_analysis']
            consistency = analysis['consistency_analysis']
            summary = analysis['overall_summary']
            
            f.write("🎯 高難度experiment (Problem 21~30):\n")
            f.write("✅ 涵蓋高級概念：刚体力學、熱力學循環、耦合振動、火箭推進\n")
            f.write("✅ 混合數值與符號解答\n")
            f.write("✅ 防記憶污染：隨機順序 + 4s延遲\n")
            f.write("✅ 允許更大誤差：15%容忍度（vs 中等題10%）\n\n")
            
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
        
        print(f"✅ 高難度結果已保存：problem_21_30_results_{timestamp}.json")
        print(f"✅ 分析報告：problem_21_30_analysis_{timestamp}.txt")

def main():
    """主執行函數"""
    print("=== Problem 21~30 高難度認知效率experiment ===")
    print("測試最具挑戰性的物理問題")
    print("包括：刚体力學、熱力學循環、耦合振動、火箭推進、約束運動等\n")
    
    experiment = Problem21To30Experiment()
    
    # Establish baseline
    baseline = experiment.establish_simple_baseline(5)
    if baseline == 0:
        print("❌ 無法Establish baseline，終止experiment")
        return
    
    # 執行高難度experiment
    results = experiment.run_challenging_experiment()
    
    # 分析三大指標
    analysis = experiment.analyze_three_metrics(results)
    
    # 顯示關鍵結果
    print(f"\n🏆 Problem 21~30 關鍵結果:")
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
    
    print("\n🎉 Problem 21~30 高難度Experiment completed！")
    print("🔬 現在擁有簡單、中等、高難度三個級別的完整數據！")

if __name__ == "__main__":
    main()
