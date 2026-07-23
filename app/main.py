# 1. 모듈 가져오기
from fastapi import FastAPI

# 2. 객체 생성
app = FastAPI()

# 3. 라우팅 구성: 특정 요청을 받을 URL을 설정하고 이 요청을 처리할 함수를 매핑
@app.get("/") # 홈페이지
def read_root(): # 요청 처리 함수 > 반환값은 응답
    return {"message": "Hello World2"}

# 4. 서버가동 > uvicorn이 담당
