from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

# ルーターをインポート
from app.routers import auth, question, interest, spot, user


app = FastAPI(root_path='/api')

# CORSの設定
raw_origins = os.getenv("ALLOWED_ORIGINS", "http://localhost:3000")

origins = [origin.strip() for origin in raw_origins.split(",")]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, # 許可するオリジン
    allow_credentials=True,
    allow_methods=["*"],   # 全てのメソッド(GET, POST...)を許可
    allow_headers=["*"],   # 全てのヘッダーを許可
)

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

# 問題関係のルーターを登録
app.include_router(question.router)

# 興味関係のルーターを登録
app.include_router(interest.router)

# スポット関係のルーターを登録
app.include_router(spot.router)

# ログインAPI
app.include_router(auth.router)

# ユーザー情報取得
app.include_router(user.router)