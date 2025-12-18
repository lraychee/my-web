from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    # 這會告訴 Flask 去 templates 資料夾找 index.html
    return render_template('index.html')

if __name__ == "__main__":
    # Render 會自動分配 port，這行確保程式能正確執行
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)