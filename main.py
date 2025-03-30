import streamlit as st
st.write(Xin chào mọi người)
st.title('Tạo tài khoản')
ten=st.text_input('Tên đăng nhập')
mk=st.text_input('Mật khẩu')
bar=st.progress(0)
if ten=='' and mk=='' :
  bar.progress(0)
elif ten=='' or mk=='':
  bar.progress(50)
else:
  bar.progress(100)
