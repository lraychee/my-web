import streamlit as st
import streamlit.components.v1 as components

# 設定頁面為寬螢幕模式
st.set_page_config(page_title="數據管理系統", layout="wide")

# --- 第一列：頂部整列功能區 ---
with st.container():
    # 使用 CSS 讓頂部看起來更像導覽列
    st.markdown("""
        <style>
        .top-nav {
            background-color: #f0f2f6;
            padding: 10px;
            border-radius: 5px;
            margin-bottom: 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        </style>
        <div class="top-nav">
            <h2 style="margin:0;">🚀 數據中心管理系統</h2>
        </div>
    """, unsafe_allow_html=True)
    
    # 這裡可以放一些全域按鈕或功能
    col_t1, col_t2, col_t3 = st.columns([1, 1, 6])
    with col_t1:
        st.button("首頁", use_container_width=True)
    with col_t2:
        st.button("監控數據", use_container_width=True)
    with col_t3:
        st.button("其他", use_container_width=True)
    with col_t4:
        st.button("系統設定", use_container_width=True)

st.markdown("---") # 分隔線

# --- 第二列：兩欄佈局 (左 20%, 右 80%) ---
# Streamlit 的比例用數字代表，1:4 即為 20%:80%
col_left, col_right = st.columns([1, 4])

with col_left:
    st.subheader("📁 監控數據")
    # 使用 radio 或 button 製作子選單    
    
    st.info(f"目前檢視：{sub_function}")
    st.button("導出報表", use_container_width=True)

with col_right:
    st.subheader(f"📊 {sub_function} 數據顯示")
    
    # 根據左邊選單選擇，顯示不同的 Looker Studio 報表 (示範用)
    if sub_function == "監控數據":
        looker_url = "https://lookerstudio.google.com/embed/reporting/be525ae8-b922-4993-8909-0d145c8e0291/page/ruyiF"
    elif sub_function == "流量分析":
        looker_url = "你的 Looker Studio 報表網址 2"
    else:
        looker_url = "你的 Looker Studio 報表網址 3"

    # 嵌入報表
    components.iframe(looker_url, height=800, scrolling=True)

