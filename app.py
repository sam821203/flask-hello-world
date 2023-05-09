from flask import Flask

# 建立應用程式的物件
# __name__ 代表目前執行的模組
app = Flask(__name__)

# 函式的裝飾(Decorator): 以函式為基礎，提供附加的功能
# "/" 代表網站的根目錄
# 127.0.0.1:5000 代表網站的主機名稱和 port 號
@app.route("/")
def home():
  return "Hello Flask 2"

# 新增要處理的路徑
@app.route("/test")
def test():
  return "This is Test"

# 如果以 app.py 主程式執行
if __name__ == "__main__":
  app.run() # 立刻啟動伺服器