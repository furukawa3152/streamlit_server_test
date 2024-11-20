import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import japanize_matplotlib  # 追加

# データの読み込み
file_path = 'R5年度入院時年齢.xlsx'
data = pd.read_excel(file_path)

# タイトル
st.title("診療科や病棟による年齢の偏差分析")

# データの表示
st.header("データの概要")
st.text("令和5年度の入院患者を入院時の年齢から分析したものです。")
st.dataframe(data)

# 診療科ごとの年齢分布
st.header("診療科ごとの年齢分布")
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(x='診療科', y='入院時年齢', data=data, ax=ax)
ax.set_title("診療科ごとの年齢分布")
ax.set_xlabel("診療科")
ax.set_ylabel("入院時年齢")
st.pyplot(fig)

# 病棟ごとの年齢分布
st.header("病棟ごとの年齢分布")
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(x='部屋番号記録:部屋', y='入院時年齢', data=data, ax=ax)
ax.set_title("病棟ごとの年齢分布")
ax.set_xlabel("病棟")
ax.set_ylabel("入院時年齢")
st.pyplot(fig)

# 診療科別の年齢の平均と標準偏差
st.header("診療科別の年齢の平均と標準偏差")
age_stats_by_department = data.groupby('診療科')['入院時年齢'].agg(['mean', 'std']).reset_index()
st.dataframe(age_stats_by_department)

# 病棟別の年齢の平均と標準偏差
st.header("病棟別の年齢の平均と標準偏差")
age_stats_by_ward = data.groupby('部屋番号記録:部屋')['入院時年齢'].agg(['mean', 'std']).reset_index()
st.dataframe(age_stats_by_ward)


# 年齢の分岐点をスライダーで指定
st.header("年齢の分岐点による年齢分布の比較")
age_threshold = st.slider("年齢の分岐点を指定してください", min_value=int(data['入院時年齢'].min()), max_value=int(data['入院時年齢'].max()), value=int(data['入院時年齢'].median()))

# 指定された年齢の分岐点でデータを分割
younger_group = data[data['入院時年齢'] <= age_threshold]
older_group = data[data['入院時年齢'] > age_threshold]

st.subheader(f"{age_threshold}歳以下の年齢分布")
fig, ax = plt.subplots(figsize=(10, 6))
sns.histplot(younger_group['入院時年齢'], bins=10, kde=True, ax=ax)
ax.set_title(f"{age_threshold}歳以下の年齢分布")
ax.set_xlabel("入院時年齢")
ax.set_ylabel("人数")
st.pyplot(fig)

st.subheader(f"{age_threshold}歳以上の年齢分布")
fig, ax = plt.subplots(figsize=(10, 6))
sns.histplot(older_group['入院時年齢'], bins=10, kde=True, ax=ax)
ax.set_title(f"{age_threshold}歳以上の年齢分布")
ax.set_xlabel("入院時年齢")
ax.set_ylabel("人数")
st.pyplot(fig)