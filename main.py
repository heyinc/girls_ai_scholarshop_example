import matplotlib.pyplot as plt
import numpy as np

# データの作成
x = np.linspace(0, 10, 100)  # 0から10までの100個の点
y = np.sin(x)  # サイン波

# グラフの作成
plt.figure(figsize=(10, 6))  # グラフのサイズを設定
plt.plot(x, y, label='sin(x)')  # 折れ線グラフを描画
plt.title('Sine Wave')  # タイトル
plt.xlabel('x')  # x軸のラベル
plt.ylabel('y')  # y軸のラベル
plt.grid(True)  # グリッドを表示
plt.legend()  # 凡例を表示

# グラフを画像ファイルとして保存
plt.savefig('sine_wave.png')
print("グラフを 'sine_wave.png' として保存しました。")
