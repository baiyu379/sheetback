import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter
import streamlit as st

# 18×20の座標を作成する
x = np.arange(1, 100)
y = np.arange(1, 120)

# 中心点を指定
center_x1 = 35
center_y1 = 80
center_x2 = 65
center_y2 = 80
center_x3 = 35
center_y3 = 50  # 新しい中心点
center_x4 = 65
center_y4 = 50
center_x5 = 35
center_y5 = 20  # 新しい中心点
center_x6 = 65
center_y6 = 20

# ガウシアン関数によるデータ生成（各中心点から）
X, Y = np.meshgrid(x, y)

# ガウシアン関数の標準偏差を、距離に依存させる
distance1 = np.sqrt((X - center_x1)**2 + (Y - center_y1)**2)
distance2 = np.sqrt((X - center_x2)**2 + (Y - center_y2)**2)
distance3 = np.sqrt((X - center_x3)**2 + (Y - center_y3)**2)
distance4 = np.sqrt((X - center_x4)**2 + (Y - center_y4)**2)
distance5 = np.sqrt((X - center_x5)**2 + (Y - center_y5)**2)
distance6 = np.sqrt((X - center_x6)**2 + (Y - center_y6)**2)

sigma1 = np.where(distance1 == 0, 1, distance1) * 60 / 100
sigma2 = np.where(distance2 == 0, 1, distance2) * 60 / 100
sigma3 = np.where(distance3 == 0, 1, distance3) * 60 / 100
sigma4 = np.where(distance4 == 0, 1, distance4) * 60 / 100
sigma5 = np.where(distance5 == 0, 1, distance5) * 60 / 100
sigma6 = np.where(distance6 == 0, 1, distance6) * 60 / 100

data1 = np.exp(-((X - center_x1)**2 + (Y - center_y1)**2) / (2 * sigma1**2))
data2 = np.exp(-((X - center_x2)**2 + (Y - center_y2)**2) / (2 * sigma2**2))
data3 = np.exp(-((X - center_x3)**2 + (Y - center_y3)**2) / (2 * sigma3**2))
data4 = np.exp(-((X - center_x4)**2 + (Y - center_y4)**2) / (2 * sigma4**2))
data5 = np.exp(-((X - center_x5)**2 + (Y - center_y5)**2) / (2 * sigma5**2))
data6 = np.exp(-((X - center_x6)**2 + (Y - center_y6)**2) / (2 * sigma6**2))

# データ合算の係数をサイドバーに追加
coeff_data1 = st.sidebar.slider('Coefficient for Data 1', min_value=0.0, max_value=10.0, value=1.0)

# 各データを合算
data = data1 + data2 + data3 + data4 + coeff_data1 *data5 + coeff_data1 * data6

# データを平滑化
data_smoothed = gaussian_filter(data, sigma=14)

fig, ax = plt.subplots(figsize=(10, 8))
ax.imshow(data_smoothed, cmap='hot_r', interpolation='nearest')  # 'hot_r'はhotカラーマップの逆

# 等高線を追加
contours = ax.contour(X, Y, data_smoothed, colors='black', linewidths=0.5)

# x軸とy軸の設定
ax.set_xticks(np.arange(0, len(x), 10))
ax.set_xticklabels(np.arange(1, len(x) + 1, 10))
ax.set_yticks(np.arange(0, len(y), 10))
ax.set_yticklabels(np.arange(1, len(y) + 1, 10))

# 軸ラベルを削除
ax.set_xlabel('')
ax.set_ylabel('')
ax.set_xticks([])
ax.set_yticks([])
#ax.set_xlabel('X')
#ax.set_ylabel('Y')
#ax.set_title('Heat Map with Contours')

#plt.colorbar(ax=ax)
st.pyplot(fig)
