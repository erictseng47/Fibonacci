import matplotlib.pyplot as plt
import os

def plot_fibonacci(high, low):
    # 確保img資料夾存在
    if not os.path.exists('img'):
        os.makedirs('img')
    
    # 計算斐波那契水平
    diff = high - low
    ratios = [0, 0.236, 0.382, 0.5, 0.618, 0.786, 1]
    levels = [low + diff * ratio for ratio in ratios]
    
    # 繪製圖表
    plt.figure(figsize=(10, 6))
    for level, ratio in zip(levels, ratios):
        plt.axhline(level, linestyle='--', alpha=0.5)
        # 在右側標出數值和比例
        plt.text(1.01, level, f'{level:.2f} ({ratio})', transform=plt.gca().get_yaxis_transform(), va='center')
    
    plt.title('Fibonacci Levels')
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.xlim(0, 1.1)  # 擴展x軸以顯示標籤
    
    # 保存圖表到img資料夾
    plt.savefig('img/fibonacci_levels.png', bbox_inches='tight')
    plt.show()

# 使用高點72.5和低點51.8繪製圖表

hight = float(input("Hight Value:"))
low = float(input("Low Value:"))

plot_fibonacci(hight, low)