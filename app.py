import streamlit as st
import random

st.title("you are photogenic")

# ==== 画像ファイル名一覧（8種類） ====
images = [
    "images/img1.jpg",
    "images/img2.jpg",
    "images/img3.jpg",
    "images/img4.jpg",
    "images/img5.jpg",
    "images/img6.jpg",
    "images/img7.jpg",
    "images/img8.jpg"
]

# ==== ボタンを押したらランダム表示 ====
if st.button("photogenic!"):
    selected = random.choice(images)
    st.image(selected, caption=f"Let's pose!：{selected}")
