import streamlit as st

# 문화재 정보를 담고 있는 딕셔너리 - API
culture_db = {
    "다보탑": "신라의 예술미가 돋보이는 탑입니다.",
    "불국사": "통일신라 시대의 대표적인 사찰입니다.",
    "석굴암": "정교하게 설계된 화강암 석굴 사원입니다."
}

#문화재 이름 불러오기

# 문화재 설명을 찾아주는 함수
def get_docent_info(name):
    # 입력값으로 백엔드에서 데이터 처리
    info = culture_db.get(user_input)
    return info

#받침의 여부 판별
def has_batchim(word):

    last = word[-1]

    return (ord(last) - ord("가")) % 28 != 0

# 사용자 인터페이스
user_input = st.text_input("궁금한 문화재 이름을 입력하세요: ")

# 함수 실행
result = get_docent_info(user_input)

if user_input != "":
    #설명 찾기
    result = culture_db.get(user_input,"문화재 정보 없음")
    # 출력
    st.write(result)

    recommend = []

    for key in culture_db.keys():
        # 사용자가 입력한 건 제외
        if key != user_input:
            recommend.append(key)
    name = recommend[0]
    if has_batchim(name):
        particle = "은"
    else :
        particle = "는"
    # 추천 출력
    st.write(f"이번엔 {name}{particle} 어떠신가요?")