# 간단한 홈페이지 제공
# 1. 모듈 가져오기
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

# 2. Fastapi객체 생성, 전역 변수 생성
app = FastAPI()
templates = Jinja2Templates(directory="templates")

# 3. 라우팅 구성/정의
@app.get("/")
def home(req:Request):
    # 홈페이지( "/")get 방식으로 요청> 매칭되는 함수 home()호출됨
    # index를 읽어서 req 데이터를 전달하여 동적 html구성
    # 응답(return)> 클라이언트 브라우저에게 전달 -> 렌더링, Dom tree
    # 브라우저 해석 화면에 그리기 -> 클라이언트는 응답결과를 화면서 볼수있다
    return templates.TemplateResponse(req,"index.html")