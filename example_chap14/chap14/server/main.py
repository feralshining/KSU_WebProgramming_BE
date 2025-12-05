
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

# User 타입 생성
class User(BaseModel):
    id: str
    email: str
    password: str
# 딕셔너리 {'키', '밸류'}  키: id, 밸류 {'email': 'test01@google.com', 'password': '1234'}
members = {}
origin = [
    "http://localhost:3000"
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origin,
    allow_credentials=True,      # 쿠키 및 인증 정보 포함 허용
    allow_methods=["*"],         # 모든 HTTP 메서드(GET, POST, PUT, DELETE 등) 허용
    allow_headers=["*"],         # 모든 HTTP 헤더 허용
)

@app.get('/')
def read_root():
    return {'message': '안녕 FastAPI!'}

# 회원 가입(json)
@app.post('/register')
def register(user: User):
    id, email, password = user.id, user.email, user.password 
    if id in members:
        return {'error': '이미 존재하는 아이디입니다'}
    # 리스트에만 append 가능
    # members.append()
    members[id] = {'email': email, 'password': password}
    print(members)
    return members

# 로그인
@app.post('/login')
def login(user: User):
    id, password = user.id, user.password

    # 존재하지 않는 아이디일때..
    if id not in members or members[id]["password"] != password:
        return {'error': "존재하지 않는 아이디이거나 또는 암호가 틀립니다"}
    # 존재할때...
    else:
        return {'success': '로그인 성공'}
