import streamlit as st
import time

# 网页标题
st.title("For 7zz❤️")

# 创建一个按钮，点击后显示弹窗
if st.button("给我一个惊喜！"):
    with st.spinner("正在准备惊喜..."):
        time.sleep(2)  # 模拟加载时间
    st.balloons()  # 展示气球效果
    st.success("🎉 你是我生命中最美好的惊喜！🎉")
    
# 添加一些互动
st.write("我想知道，你的爱好是什么？")
hobby = st.text_input("请输入你的爱好：", "")
if hobby:
    st.write(f"哇！我也喜欢 {hobby}！我们可以一起去做！😊")

# 结尾的温馨话语
st.write("感谢你让我的生活变得如此美好！💖")
