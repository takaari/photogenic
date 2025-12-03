import streamlit as st
import random

st.title("you are photogenic")

# ==== 画像ファイル名一覧（8種類） ====
images = [
    "img1.jpg",
    "img2.jpg",
    "img3.jpg",
    "img4.jpg",
    "img5.jpg",
    "img6.jpg",
    "img7.jpg",
    "img8.jpg"
]

# ==== ボタンを押したらランダム表示 ====
if st.button("photogenic!"):
    selected = random.choice(images)
    st.image(selected, caption=f"Let's pose!：{selected}")
