#!/usr/bin/env python3
"""
難度比較圖表生成器
Difficulty Comparison Charts Generator

生成線性 vs 非線性語言系統在不同難度級別的表現比較圖
"""

import matplotlib.pyplot as plt
import numpy as np

# 設置字體為Times New Roman
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 12

def generate_comparison_charts():
    """生成三個比較圖表：時間、準確率、穩定性"""
    
    # X 軸分類
    labels = ["Easy", "Medium", "Hard"]
    x = np.arange(len(labels))  # X 軸位置
    width = 0.35  # 柱子寬度

    # Data - Updated to match experimental results from COMPLETE_EXPERIMENTAL_RESULTS_ANALYSIS_WITH_STABILITY.md
    time_linear = [0.227, 2.125, 3.718]
    time_nonlin = [0.172, 1.229, 2.307]

    correct_linear = [60.0, 36.7, 36.7]
    correct_nonlin = [70.0, 66.7, 60.0]

    stability_linear = [97.9, 76.8, 58.6]
    stability_nonlin = [67.8, 91.4, 67.9]

    datasets = [
        ("Time (sec)", time_linear, time_nonlin),
        ("Correctness (%)", correct_linear, correct_nonlin),
        ("Stability (%)", stability_linear, stability_nonlin),
    ]

    # 畫三張圖
    for title, linear, nonlin in datasets:
        fig, ax = plt.subplots(figsize=(10, 4.5))  # 降低高度讓柱子扁一點
        
        # 使用對比明顯的顏色：深藍和橘色
        ax.bar(x - width/2, linear, width, label="Linear", color='#2E5BBA', alpha=0.85)
        ax.bar(x + width/2, nonlin, width, label="Non-linear", color='#FF8C42', alpha=0.85)

        ax.set_ylabel(title, fontsize=14, fontweight='bold')
        ax.set_xlabel("Difficulty Level", fontsize=14, fontweight='bold')
        ax.set_xticks(x)
        ax.set_xticklabels(labels, fontsize=12)
        ax.legend(fontsize=12)
        ax.set_title(f"Comparison of {title} by Difficulty Level", fontsize=16, fontweight='bold', pad=20)
        
        # 根據數據類型設定精度格式
        if "Time" in title:
            format_str = '{:.3f}'  # 時間顯示三位小數
        else:
            format_str = '{:.1f}'  # 百分比顯示一位小數
        
        # 添加數值標籤 - 統一黑色，放在柱子上方
        max_val = max(linear + nonlin)
        for i, v in enumerate(linear):
            y_pos = v + max_val * 0.015  # 稍微往上一點
            ax.text(i - width/2, y_pos, format_str.format(v), 
                   ha='center', va='bottom', fontsize=10, fontweight='bold', color='black')
        
        for i, v in enumerate(nonlin):
            y_pos = v + max_val * 0.015  # 稍微往上一點
            ax.text(i + width/2, y_pos, format_str.format(v), 
                   ha='center', va='bottom', fontsize=10, fontweight='bold', color='black')

        # 調整Y軸範圍，為標籤留出空間
        max_val = max(linear + nonlin)
        ax.set_ylim(0, max_val * 1.1)
        
        # 調整刻度標籤字體大小
        ax.tick_params(axis='both', which='major', labelsize=12)
        
        # 添加網格線增加可讀性
        ax.grid(True, alpha=0.3, linestyle='--')
        ax.set_axisbelow(True)
        
        plt.tight_layout()
        filename = f"{title.replace(' ', '_').replace('(', '').replace(')', '')}.pdf"
        plt.savefig(filename, dpi=300, bbox_inches='tight')  # 高質量輸出
        print(f"✅ 已生成圖表: {filename}")
        plt.close()

    print("\n🎯 所有比較圖表已生成完成！")

if __name__ == "__main__":
    print("🚀 Starting生成難度比較圖表...")
    generate_comparison_charts()
