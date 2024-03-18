import pandas as pd
import json
import numpy as np

# 读取 CSV 文件
df = pd.read_csv("../data/environment_data.csv")

# 创建一个字典来存储每个字段的数据
field_data = {}

# 遍历每一行数据
for index, row in df.iterrows():
    # 解析 JSON 数据
    json_data = json.loads(row['data'])

    # 遍历每个字段
    for field, value in json_data.items():
        # 将数据添加到字典中相应字段的列表中
        if field not in field_data:
            field_data[field] = []
        field_data[field].extend(value)

# 保存为 .npy 文件
for field, data in field_data.items():
    np.save(f'../data/{field}.npy', np.array(data))