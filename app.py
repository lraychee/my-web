import streamlit as st
import streamlit.components.v1 as components

# 1. 網頁基本設定 (標題與版面寬度)
st.set_page_config(page_title="我的Report", layout="wide")

# 2. 撰寫你的網頁內容 (原本在 index.html 裡的文字寫在這裡)
st.title("📊 我的自訂報表網站")
st.write("這是我透過 Python 與 Streamlit 建立的網頁，下方嵌入了動態報表。")

# 3. 嵌入 Looker Studio 報表
# 請將下方的 URL 替換成你在 Looker Studio 取得的「嵌入網址」
looker_studio_url = "https://lookerstudio.google.com/embed/reporting/be525ae8-b922-4993-8909-0d145c8e0291/page/ruyiF"

# 建立顯示區域
components.iframe(looker_studio_url, height=800, scrolling=True)

# 4. 如果你還有其他文字想放，直接寫在下面
st.markdown("---")
st.caption("資料來源：我的 Google Sheets / BigQuery")
