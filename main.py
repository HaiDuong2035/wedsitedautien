import streamlit as st
st.title('Tạo tài khoản')
x=0
a=st.text_input('Tài khoản')
if a!='':
  x+=20
b=st.text_input('Mật khẩu')
if b!='':
  x+=20
c=st.text_input('Nhập lại mật khẩu')
if c!='':
  x+=20
d=st.text_input('Tên người dùng')
if d!='':
  x+=20
e=st.text_input('Email')
if e!='':
  x+=20
st.progress(x)
