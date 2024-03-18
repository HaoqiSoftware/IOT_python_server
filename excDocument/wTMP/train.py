
import numpy as np
from matplotlib import pyplot as plt

# 读取TMP.npy数据
wtmp_data = np.load('../../data/wTMP.npy')

# 将数据区分为训练数据和测试数据
test_data_size = 60
train_data = wtmp_data[: -test_data_size]
test_data = wtmp_data[-test_data_size:]

# 数据归一化
