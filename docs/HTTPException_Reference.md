# HTTPException 참고 자료

## 개요

FastAPI에서 HTTP 예외를 발생시키기 위해 사용하는 `HTTPException` 클래스에 대한 참고 자료입니다. 이는 C#의 `throw new Exception()`과 유사하게, 서버에서 에러를 발생시키고 클라이언트에 적절한 HTTP 응답을 반환합니다.

## 임포트

```python
from fastapi import HTTPException
```

## 기본 사용법

```python
raise HTTPException(status_code=400, detail="에러 메시지")
```

### 파라미터 설명

- `status_code`: HTTP 상태 코드 (예: 400, 404, 500 등)
- `detail`: 에러 메시지 (문자열)
- `headers`: 선택적 헤더 (딕셔너리)

## 예제 코드

### 1. 회원가입 에러 처리

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id: str
    password: str
    email: str

member = {}

@app.post("/register")
def register_user(user: User):
    if user.id in member:
        raise HTTPException(status_code=400, detail="이미 존재하는 아이디입니다.")

    member[user.id] = {"password": user.password, "email": user.email}
    return {"message": "회원가입이 완료되었습니다."}
```

### 2. 로그인 에러 처리

```python
class LoginRequest(BaseModel):
    id: str
    password: str

@app.post("/login")
def login_user(login: LoginRequest):
    if login.id not in member:
        raise HTTPException(status_code=400, detail="존재하지 않는 아이디입니다.")

    if member[login.id]['password'] != login.password:
        raise HTTPException(status_code=400, detail="비밀번호가 틀렸습니다.")

    return {"message": "로그인 성공"}
```

## 클라이언트 측 처리 (axios)

### JavaScript (axios) 예제

```javascript
// 회원가입 요청
axios
  .post("/register", {
    id: "testuser",
    password: "password123",
    email: "test@example.com",
  })
  .then((response) => {
    console.log("성공:", response.data);
  })
  .catch((error) => {
    if (error.response) {
      console.log("에러 상태 코드:", error.response.status); // 400
      console.log("에러 메시지:", error.response.data.detail); // "이미 존재하는 아이디입니다."
    } else {
      console.log("네트워크 에러:", error.message);
    }
  });
```

## 주요 HTTP 상태 코드

- `400`: Bad Request (잘못된 요청)
- `401`: Unauthorized (인증 실패)
- `403`: Forbidden (권한 없음)
- `404`: Not Found (리소스 없음)
- `500`: Internal Server Error (서버 내부 에러)

## 추가 옵션

```python
# 헤더 추가
raise HTTPException(
    status_code=401,
    detail="인증이 필요합니다.",
    headers={"WWW-Authenticate": "Bearer"}
)

# 커스텀 예외 클래스 생성 (선택적)
from fastapi import HTTPException

class CustomException(HTTPException):
    def __init__(self, detail: str):
        super().__init__(status_code=400, detail=detail)
```

## 참고 사항

- `HTTPException`을 `raise`하면 FastAPI가 자동으로 JSON 응답을 생성합니다.
- 클라이언트에서는 `error.response.data.detail`로 메시지를 접근할 수 있습니다.
- 일반적인 성공 응답은 `return {"message": "..."}`로 처리하고, 에러는 `HTTPException`으로 처리하세요.
