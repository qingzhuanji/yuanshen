import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog
import seaborn as sns

# 设置整体风格
plt.style.use('seaborn-v0_8')  # 使用新版本的seaborn样式名称
# 或者使用其他内置样式
# plt.style.use('bmh')  # 另一个好看的替代样式

# 添加中文字体支持
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
# 设置图形文字大小
plt.rcParams['font.size'] = 12
plt.rcParams['axes.titlesize'] = 16
plt.rcParams['axes.labelsize'] = 14

def plot_constraints(constraints, bounds, objective):
    """
    可视化线性规划问题的约束条件和目标函数
    """
    # 创建坐标点
    x = np.linspace(0, 100, 1000)
    
    # 设置图形大小和样式
    plt.figure(figsize=(12, 8))
    
    # 设置背景网格
    plt.grid(True, linestyle='--', alpha=0.3)
    
    # 绘制约束条件
    colors = sns.color_palette("husl", 3)  # 使用seaborn的调色板
    labels = ['A类资源限制', 'B类资源限制', 'C类资源限制']
    
    for i, (a, b, c) in enumerate(constraints):
        if b != 0:
            y = (c - a * x) / b
            plt.plot(x, y, color=colors[i], label=labels[i], linewidth=2)
    
    # 填充可行域
    y1 = np.minimum(np.minimum((360 - 9*x)/4, (200 - 4*x)/6), (300 - 3*x)/10)
    y1 = np.maximum(y1, 0)
    plt.fill_between(x, 0, y1, alpha=0.2, color='gray', label='可行域')
    
    # 绘制目标函数等值线
    z_values = [1000, 2000, 3000, 4000, 5000]
    cmap = plt.cm.autumn  # 使用渐变色彩
    for i, z in enumerate(z_values):
        y = (z - 70*x) / 120
        color = cmap(i / len(z_values))
        plt.plot(x, y, '--', color=color, alpha=0.5, linewidth=1.5)
        plt.text(2, z/120, f'利润={z}', color=color, alpha=0.8,
                bbox=dict(facecolor='white', edgecolor='none', alpha=0.6))
    
    # 设置图形属性
    plt.xlabel('x₁ (甲产品数量)', fontsize=12)
    plt.ylabel('x₂ (乙产品数量)', fontsize=12)
    plt.title('线性规划问题可视化分析\n最大化利润 = 70x₁ + 120x₂', pad=20)
    
    # 美化坐标轴
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    
    # 设置坐标轴范围
    plt.xlim(0, 50)
    plt.ylim(0, 50)
    
    # 添加图例，并设置样式
    legend = plt.legend(loc='upper right', 
                       bbox_to_anchor=(1.15, 1),
                       frameon=True,
                       fancybox=True,
                       shadow=True,
                       fontsize=10)
    
    return plt

def solve_linear_programming():
    """
    求解线性规划问题
    """
    # 目标函数系数 (最大化70x₁ + 120x₂)
    c = [-70, -120]  # 注意：scipy.linprog默认求最小值，所以需要取负
    
    # 约束条件系数矩阵
    A = [
        [9, 4],    # 9x₁ + 4x₂ ≤ 360
        [4, 6],    # 4x₁ + 6x₂ ≤ 200
        [3, 10]    # 3x₁ + 10x₂ ≤ 300
    ]
    
    # 约束条件右侧常数
    b = [360, 200, 300]
    
    # 变量范围约束
    x_bounds = (0, None)  # x₁, x₂ ≥ 0
    
    # 求解
    result = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, x_bounds], method='simplex')
    
    return result

def main():
    try:
        # 约束条件
        constraints = [
            (9, 4, 360),   # 9x₁ + 4x₂ ≤ 360
            (4, 6, 200),   # 4x₁ + 6x₂ ≤ 200
            (3, 10, 300)   # 3x₁ + 10x₂ ≤ 300
        ]
        
        # 变量范围
        bounds = [(0, None), (0, None)]
        
        # 目标函数
        objective = [70, 120]
        
        # 求解问题
        result = solve_linear_programming()
        
        # 绘制图形
        plt = plot_constraints(constraints, bounds, objective)
        
        # 标注最优解
        if result.success:
            x_opt, y_opt = result.x
            z_opt = -result.fun
            plt.plot(x_opt, y_opt, 'r*', markersize=20, label='最优解')
            
            # 添加最优解说明文本框
            textstr = f'最优解:\nx₁ = {x_opt:.1f}\nx₂ = {y_opt:.1f}\n最大利润 = {z_opt:.1f}'
            props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
            plt.text(x_opt+2, y_opt-5, textstr, fontsize=10,
                    bbox=props, verticalalignment='top')
        
        # 调整布局，防止文字重叠
        plt.tight_layout()
        plt.show()
        
        # 打印结果
        print("\n最优解：")
        print(f"甲产品生产数量 = {result.x[0]:.2f}")
        print(f"乙产品生产数量 = {result.x[1]:.2f}")
        print(f"最大利润 = {-result.fun:.2f}")
        
    except Exception as e:
        print(f"程序运行出错：{str(e)}")

if __name__ == "__main__":
    main() 