from fastapi import FastAPI
from app.api.v1.routers import api_router
from pydantic import BaseModel

# [과제용 주석] CORS 문제 해결용으로 Starlette/FastAPI 미들웨어 임포트
from fastapi.middleware.cors import CORSMiddleware

# Pydantic 모델은 데이터의 구조와 타입을 정의합니다.
class User(BaseModel):
    id: str
    password: str
    email: str

class LoginRequest(BaseModel):
    id: str
    password: str
   
member = {'admin': {'password': 'admin123', 'email': 'admin@example.com'}}

app = FastAPI()

origins = [
    "http://localhost:3000",  # FE 서버
]

# app에 미들웨어를 추가하여 모든 요청 검사 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,       # 허용할 출처 목록
    allow_credentials=True,      # 쿠키 및 인증 정보 포함 허용
    allow_methods=["*"],         # 모든 HTTP 메서드(GET, POST, PUT, DELETE 등) 허용
    allow_headers=["*"],         # 모든 HTTP 헤더 허용
)

app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"Hello": "World"}


# 회원가입
@app.post("/register")
def register_user(user: User):
    id = user.id
    password = user.password
    email = user.email 

    if id in member:
        return {"error": "이미 존재하는 아이디입니다."}
    
    member[id] = {"password": password, "email": email}
    print(member)
    return {"message": "회원가입이 완료되었습니다."}

# 로그인
@app.post("/login")
def login_user(login: LoginRequest):
    id = login.id
    password = login.password

    if id not in member:
        return {"error": "존재하지 않는 아이디입니다."}
    
    if member[id]['password'] != password:
        return {"error": "비밀번호가 틀렸습니다."}
    
    return {"message": "로그인 성공"}

# 디버깅용
@app.get("/debug")
def debug():
    return member