#!/usr/bin/env python3
"""
Circular Non-linear Language Design Visualization
Circular Non-linear Language Design Visualization
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

def create_circular_language_visualization():
    """Create circular language design visualization"""
    
    # Set up chart
    fig, ax = plt.subplots(1, 1, figsize=(14, 14))
    ax.set_xlim(-1.3, 1.3)
    ax.set_ylim(-1.3, 1.3)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Define ring radius
    inner_radius = 0.2
    middle_radius = 0.5
    outer_radius = 1.0
    
    # Inner ring: Target physics quantity
    inner_circle = patches.Circle((0, 0), inner_radius, 
                                 facecolor='#FF6B6B', alpha=0.8, 
                                 edgecolor='black', linewidth=2)
    ax.add_patch(inner_circle)
    
    # Middle ring: Solving conditions
    middle_ring = patches.Circle((0, 0), middle_radius, 
                                facecolor='#4ECDC4', alpha=0.6, 
                                edgecolor='black', linewidth=2)
    ax.add_patch(middle_ring)
    
    # Inner ring cover (create middle ring effect)
    inner_cover = patches.Circle((0, 0), inner_radius, 
                                facecolor='#FF6B6B', alpha=0.8,
                                edgecolor='black', linewidth=2)
    ax.add_patch(inner_cover)
    
    # Middle ring text
    ax.text(0, 0.35, 'SOLVING', fontsize=18, weight='bold', 
            ha='center', va='center', color='black')
    ax.text(0, -0.35, 'CONDITIONS', fontsize=16, weight='bold',
            ha='center', va='center', color='black')
    
    # Outer ring: Divided into three regions, each with different color
    # Region A: Time-independent (top, green)
    theta1 = np.linspace(np.pi/6, 5*np.pi/6, 100)
    r_outer = np.full_like(theta1, outer_radius)
    r_middle = np.full_like(theta1, middle_radius)
    x_outer_a = r_outer * np.cos(theta1)
    y_outer_a = r_outer * np.sin(theta1)
    x_middle_a = r_middle * np.cos(theta1)
    y_middle_a = r_middle * np.sin(theta1)
    
    # Create wedge for region A
    wedge_a = patches.Wedge((0, 0), outer_radius, 30, 150, width=outer_radius-middle_radius,
                           facecolor='#E8F6F3', alpha=0.8, edgecolor='black', linewidth=2)
    ax.add_patch(wedge_a)
    
    # Region B: Time-dependent (bottom left, red)
    wedge_b = patches.Wedge((0, 0), outer_radius, 150, 270, width=outer_radius-middle_radius,
                           facecolor='#FFE5E5', alpha=0.8, edgecolor='black', linewidth=2)
    ax.add_patch(wedge_b)
    
    # Region C: Boundaries (bottom right, yellow)
    wedge_c = patches.Wedge((0, 0), outer_radius, 270, 390, width=outer_radius-middle_radius,
                           facecolor='#FFF9E5', alpha=0.8, edgecolor='black', linewidth=2)
    ax.add_patch(wedge_c)
    
    # Re-add middle ring
    middle_ring2 = patches.Circle((0, 0), middle_radius, 
                                 facecolor='#4ECDC4', alpha=0.6,
                                 edgecolor='black', linewidth=2)
    ax.add_patch(middle_ring2)
    
    # Re-add inner ring
    inner_circle2 = patches.Circle((0, 0), inner_radius, 
                                  facecolor='#FF6B6B', alpha=0.8, 
                                  edgecolor='black', linewidth=2)
    ax.add_patch(inner_circle2)
    
    # Region A: Time-independent conditions (top)
    ax.text(0, 0.75, 'Time-independent\nConditions', fontsize=16, weight='bold',
            ha='center', va='center', color='#2E4057',
            bbox=dict(boxstyle="round,pad=0.3", facecolor='white', alpha=0.9))
    
    # Example - top region
    ax.text(-0.2, 0.65, '• Mass m', fontsize=14, ha='left', va='center')
    ax.text(-0.2, 0.6, '• Gravity g', fontsize=14, ha='left', va='center')
    ax.text(-0.2, 0.55, '• Friction μ', fontsize=14, ha='left', va='center')
    
    # Region B: Time-dependent conditions (bottom left)
    ax.text(-0.6, -0.3, 'Time-dependent\nVariables', fontsize=16, weight='bold',
            ha='center', va='center', color='#2E4057',
            bbox=dict(boxstyle="round,pad=0.3", facecolor='white', alpha=0.9))
    
    # Example - bottom left region
    ax.text(-0.8, -0.5, '• F(x) Force', fontsize=14, ha='left', va='center')
    ax.text(-0.8, -0.55, '• v(t) Velocity', fontsize=14, ha='left', va='center')
    ax.text(-0.8, -0.6, '• x²+6x Position', fontsize=14, ha='left', va='center')
    
    # Region C: Boundary conditions (bottom right)
    ax.text(0.6, -0.3, 'Boundary\nConditions', fontsize=16, weight='bold',
            ha='center', va='center', color='#2E4057',
            bbox=dict(boxstyle="round,pad=0.3", facecolor='white', alpha=0.9))
    
    # Example - bottom right region
    ax.text(0.4, -0.5, '• t=0 Initial', fontsize=14, ha='left', va='center')
    ax.text(0.4, -0.55, '• x=5 Position', fontsize=14, ha='left', va='center')
    ax.text(0.4, -0.6, '• v₀=0 Velocity', fontsize=14, ha='left', va='center')
    
    # Re-add中心文字 - 分開顯示避免重疊，調整間距
    ax.text(0, 0.1, 'TARGET', fontsize=15, weight='bold', 
            ha='center', va='center', color='white')
    ax.text(0, 0, 'PHYSICS', fontsize=15, weight='bold', 
            ha='center', va='center', color='white')
    ax.text(0, -0.1, 'QUANTITY', fontsize=15, weight='bold', 
            ha='center', va='center', color='white')
    
    # 添加箭頭指示處理順序
    # 從內到外的箭頭 - 修正位置
    arrow1 = patches.FancyArrowPatch((0.15, 0.15), (0.4, 0.4),
                                    arrowstyle='->', mutation_scale=25,
                                    color='red', linewidth=3)
    ax.add_patch(arrow1)
    
    arrow2 = patches.FancyArrowPatch((0.4, 0.4), (0.7, 0.7),
                                    arrowstyle='->', mutation_scale=25,
                                    color='red', linewidth=3)
    ax.add_patch(arrow2)
    
    # 處理順序標示 - 修正位置和大小
    ax.text(0.3, 0.3, '1', fontsize=16, weight='bold', 
            ha='center', va='center', color='red',
            bbox=dict(boxstyle="circle,pad=0.15", facecolor='white', edgecolor='red', linewidth=2))
    
    ax.text(0.55, 0.55, '2', fontsize=16, weight='bold', 
            ha='center', va='center', color='red',
            bbox=dict(boxstyle="circle,pad=0.15", facecolor='white', edgecolor='red', linewidth=2))
    
    ax.text(0.8, 0.8, '3', fontsize=16, weight='bold', 
            ha='center', va='center', color='red',
            bbox=dict(boxstyle="circle,pad=0.15", facecolor='white', edgecolor='red', linewidth=2))
    
    # 標題
    plt.title('Circular Non-linear Language Structure\nfor AI Physics Problem Solving', 
             fontsize=22, weight='bold', pad=25)
    
    # 圖例 - 放大字體
    legend_elements = [
        patches.Patch(color='#FF6B6B', alpha=0.8, label='Inner Ring: Target Physics Quantity'),
        patches.Patch(color='#4ECDC4', alpha=0.6, label='Middle Ring: Solving Conditions'),
        patches.Patch(color='#E8F6F3', alpha=0.8, label='Outer Ring A: Time-independent'),
        patches.Patch(color='#FFE5E5', alpha=0.8, label='Outer Ring B: Time-dependent'),
        patches.Patch(color='#FFF9E5', alpha=0.8, label='Outer Ring C: Boundary Conditions')
    ]
    ax.legend(handles=legend_elements, loc='upper right', bbox_to_anchor=(1.25, 1), 
              fontsize=14, frameon=True, fancybox=True, shadow=True)
    
    # 移除Processing Flow說明
    
    plt.tight_layout()
    return fig

def create_comparison_diagram():
    """創建線性vs非線性語言比較圖"""
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 8))
    plt.subplots_adjust(wspace=0.1)  # 減少子圖間距
    
    # 左側：線性語言
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 10)
    ax1.set_title('Linear Language Structure\n(Traditional Sequential Processing)', fontsize=16, weight='bold')
    ax1.axis('off')
    
    # 線性語言流程
    linear_boxes = [
        (5, 9, 'Read Complete Text'),
        (5, 8, 'Understand Semantics'),
        (5, 7, 'Identify Keywords'),
        (5, 6, 'Extract Numerical Values'),
        (5, 5, 'Determine Formulas'),
        (5, 4, 'Establish Relationships'),
        (5, 3, 'Calculate Solution')
    ]
    
    for i, (x, y, text) in enumerate(linear_boxes):
        color = plt.cm.Blues(0.3 + i * 0.1)
        box = patches.FancyBboxPatch((x-1.5, y-0.3), 3, 0.6,
                                    boxstyle="round,pad=0.1",
                                    facecolor=color, edgecolor='black')
        ax1.add_patch(box)
        ax1.text(x, y, text, ha='center', va='center', fontsize=12, weight='bold')
        
        if i < len(linear_boxes) - 1:
            arrow = patches.FancyArrowPatch((x, y-0.4), (x, y-0.6),
                                          arrowstyle='->', mutation_scale=15,
                                          color='black', linewidth=1.5)
            ax1.add_patch(arrow)
    
    # 右側：圓環狀非線性語言
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 10)
    ax2.set_title('Circular Non-linear Language Structure\n(Hierarchical Parallel Processing)', fontsize=16, weight='bold')
    ax2.axis('off')
    
    # 簡化的圓環示意圖
    center_x, center_y = 5, 5
    
    # 內環
    inner = patches.Circle((center_x, center_y), 0.8, 
                          facecolor='#FF6B6B', alpha=0.8, 
                          edgecolor='black', linewidth=2)
    ax2.add_patch(inner)
    ax2.text(center_x, center_y, 'TARGET', ha='center', va='center', 
            fontsize=10, weight='bold', color='white')
    
    # 中環
    middle = patches.Circle((center_x, center_y), 1.5, 
                           facecolor='#4ECDC4', alpha=0.6, 
                           edgecolor='black', linewidth=2)
    ax2.add_patch(middle)
    
    # 遮蓋內環
    inner_cover = patches.Circle((center_x, center_y), 0.8, 
                                facecolor='#FF6B6B', alpha=0.8, 
                                edgecolor='black', linewidth=2)
    ax2.add_patch(inner_cover)
    
    ax2.text(center_x, center_y+1.1, 'CONDITIONS', ha='center', va='center', 
            fontsize=13, weight='bold')
    
    # 外環三個區域
    # Region A: Time-independent (頂部，綠色)
    wedge_a2 = patches.Wedge((center_x, center_y), 2.2, 30, 150, width=2.2-1.5,
                           facecolor='#E8F6F3', alpha=0.8, edgecolor='black', linewidth=1)
    ax2.add_patch(wedge_a2)
    
    # Region B: Time-dependent (bottom left, red)
    wedge_b2 = patches.Wedge((center_x, center_y), 2.2, 150, 270, width=2.2-1.5,
                           facecolor='#FFE5E5', alpha=0.8, edgecolor='black', linewidth=1)
    ax2.add_patch(wedge_b2)
    
    # Region C: Boundaries (bottom right, yellow)
    wedge_c2 = patches.Wedge((center_x, center_y), 2.2, 270, 390, width=2.2-1.5,
                           facecolor='#FFF9E5', alpha=0.8, edgecolor='black', linewidth=1)
    ax2.add_patch(wedge_c2)
    
    # 遮蓋中環
    middle_cover = patches.Circle((center_x, center_y), 1.5, 
                                 facecolor='#4ECDC4', alpha=0.6, 
                                 edgecolor='black', linewidth=2)
    ax2.add_patch(middle_cover)
    
    # Re-add inner ring
    inner_final = patches.Circle((center_x, center_y), 0.8, 
                                facecolor='#FF6B6B', alpha=0.8, 
                                edgecolor='black', linewidth=2)
    ax2.add_patch(inner_final)
    ax2.text(center_x, center_y, 'TARGET', ha='center', va='center', 
            fontsize=16, weight='bold', color='white')
    
    # 外環標籤 - 水平文字，放在圓圈外面
    ax2.text(center_x, center_y+2.8, 'A: Time-independent', ha='center', va='center', fontsize=13, weight='bold')
    ax2.text(center_x-2.2, center_y-1.5, 'B: Time-dependent', ha='center', va='center', fontsize=13, weight='bold')
    ax2.text(center_x+2.2, center_y-1.5, 'C: Boundary Conditions', ha='center', va='center', fontsize=13, weight='bold')
    
    # 處理流程箭頭（並行）
    ax2.text(center_x, 1.5, 'Hierarchical Parallel\nProcessing', ha='center', va='center', 
            fontsize=14, weight='bold', color='green')
    
    plt.tight_layout()
    return fig

if __name__ == "__main__":
    # 生成圓環狀語言設計圖
    fig1 = create_circular_language_visualization()
    fig1.savefig('/Users/hungyuwang/Desktop/experiment_language/circular_language_design.pdf', 
                dpi=300, bbox_inches='tight', facecolor='white')
    fig1.savefig('/Users/hungyuwang/Desktop/experiment_language/circular_language_design.png', 
                dpi=300, bbox_inches='tight', facecolor='white')
    
    # 生成比較圖
    fig2 = create_comparison_diagram()
    fig2.savefig('/Users/hungyuwang/Desktop/experiment_language/language_comparison.pdf', 
                dpi=300, bbox_inches='tight', facecolor='white')
    fig2.savefig('/Users/hungyuwang/Desktop/experiment_language/language_comparison.png', 
                dpi=300, bbox_inches='tight', facecolor='white')
    
    plt.show()
    
    print("✅ Circular Language Design Diagrams Generated:")
    print("   - circular_language_design.pdf: Detailed circular structure diagram (PDF)")
    print("   - circular_language_design.png: Detailed circular structure diagram (PNG)")
    print("   - language_comparison.pdf: Linear vs Circular language comparison (PDF)")
    print("   - language_comparison.png: Linear vs Circular language comparison (PNG)")
