from fastapi import FastAPI
from app.api.v1.routers import api_router
from pydantic import BaseModel

#Pydantic 모델은 데이터의 구조와 타입을 정의합니다.

class User(BaseModel):
    id: str
    password: str
    email: str

class LoginRequest(BaseModel):
    id: str
    password: str
   
member = {'admin': {'password': 'admin123', 'email': 'admin@example.com'}}

app = FastAPI()

app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"Hello": "World"}


#회원가입
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

#로그인
@app.post("/login")
def login_user(login: LoginRequest):
    id = login.id
    password = login.password

    if id not in member:
        return {"error": "존재하지 않는 아이디입니다."}
    
    if member[id]['password'] != password:
        return {"error": "비밀번호가 틀렸습니다."}
    
    return {"message": "로그인 성공"}

#디버깅용
@app.get("/debug")
def debug():
    return member