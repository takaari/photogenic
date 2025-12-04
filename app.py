import streamlit as st
import time
import random

st.title("you are photogenic")

# == 画像フォルダ ==
BASE = "images/"

# == ランダム画像一覧 ==
images = [
    BASE + "img1.jpg",
    BASE + "img2.jpg",
    BASE + "img3.jpg",
    BASE + "img4.jpg",
    BASE + "img5.jpg",
    BASE + "img6.jpg",
    BASE + "img7.jpg",
    BASE + "img8.jpg",
]

# == 表紙画像を表示（最初だけ） ==
if "started" not in st.session_state:
    st.session_state.started = False

placeholder = st.empty()   # 画像表示用の箱（中身を入れ替える）

# 最初の表紙
if not st.session_state.started:
    placeholder.image(BASE + "top0.jpg")


# ==== ボタンを押したらカウントダウン → ランダム表示 ====
if st.button("photogenic!"):

    st.session_state.started = True

    # カウントダウン画像の順番
    countdown_imgs = [
        BASE + "countdown3.jpg",
        BASE + "countdown2.jpg",
        BASE + "countdown1.jpg",
    ]

    # ===== カウントダウン表示 =====
    for cd_img in countdown_imgs:
        placeholder.image(cd_img)
        time.sleep(1)

    # ===== ランダム画像を表示 =====
    selected = random.choice(images)
    placeholder.image(selected)

