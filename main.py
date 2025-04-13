import streamlit as st
st.set_page_config(page_title='Trac nghiem kiem tra tinh cach',page_icon='♫',layout='wide')
st.title('Trac nghiem kiem tra tinh cach by duong')
dict={
'':'ban chua chon con gi',
'meo':'lua chon nay cho thay ban chua san sang de bat dau cong viec, khao khat duoc di nghi',
'cho':'ban cam nhan duoc su ho tro nhiet tinh cua ban be va vi the nen san sang giai quyet moi van de xay ra',
'sutu':'Co the thay ban la nguoi co ve ngoai noi bat, thu hut mn bang ve hao nhoang',
'ngua':'Co dieu gi do dang han che su tu do cua ban',
'thiennga':'hien tai ban co khoang thoi gian ngot ngao, co gang tan huong va keo dai no.'}
choice=''
c1,c2,c3,c4,c5=st.columns(5)
with c1:
  if st.button('Meo'):
    choice='meo'
with c2:
  if st.button('Cho'):
    choice='cho'
with c3:
  if st.button('Su tu'):
    choice='sutu'
with c4:
  if st.button('Ngua'):
    choice='ngua'
with c5:
  if st.button('Thien nga'):
    choice='thiennga'
st.write(dict[choice])
with st.sidebar:
  st.write('Trac nghiem kiem tra tinh cach')
  if choice=='':
    st.write('ban chua chon con gi')
  else:
    st.write('Ban da chon con',choice)
