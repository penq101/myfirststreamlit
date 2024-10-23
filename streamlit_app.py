import streamlit as st

st.title("👋🏻 연수 실습 페이지")
st.subheader("오늘은 24년10월23일 수요일입니다")
st.write("환영합니다.")
st.write("https://weather.naver.com/")

st.link_button("날씨 바로가기!", "https://weather.naver.com/")

#창의 색깔을 바꾸기
st.success("success=초록색 창")
# st.error("error=빨간색 창")
# st.info("info=파란색 창")
# st.warning("warning=노란색 창") # ctrl+/ : 주석처리

#이미지주소
st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbnRud210dzd3MGM2N21xbXV1ODN6N292MXR4aTNicHZ5dzFrb2xpayZlcD12MV9naWZzX3NlYXJjaCZjdD1n/VJCK9OYBxtdGo/giphy.gif", caption="핑구성공") 
st.video("https://www.youtube.com/watch?v=l2Uhi9bTJOM")
#내가 갖고있던 이미지