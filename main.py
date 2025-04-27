import streamlit as st
st.set_page_config(page_title='Thong tin dong vat',page_icon='',layout='wide')
st.title('Thông tin động vật')
dict={
'':'Bạn chưa chọn con gì',
'meo':'Mèo là động vật có vú, nhỏ nhắn và chuyên ăn thịt, sống chung với loài người, được nuôi để săn vật gây hại hoặc làm thú nuôi cùng với chó.',
'cho':'Chó, là một loài động vật thuộc chi Chó (Canis), tạo nên một phần tiến hóa của sói, đồng thời là loài động vật ăn thịt trên cạn có số lượng lớn nhất. Chó và sói xám thuộc nhóm chị em, giống như những loài sói hiện đại đều không có họ hàng gần đến những loài sói được thuần hóa đầu tiên, đồng nghĩa với tổ tiên gốc của chó đã bị tuyệt chủng.',
'sutu':'Sư tử (Panthera leo) là một trong những loài đại miêu của họ Mèo, chi Báo, được mệnh danh là "chúa tể rừng xanh" (king of the jungle) hay "vua của muôn thú" (king of beasts).',
'ngua':'Ngựa hay mã, ngọ (Equus ferus caballus) là một loài động vật có vú trong họ Equidae, bộ Perissodactyla. Loài này được Linnaeus mô tả năm 1758., và là một trong số 8 phân loài còn sinh tồn cho tới ngày nay của họ Equidae.',
'thiennga':'Thiên nga là một nhóm chim nước cỡ lớn thuộc họ Vịt, cùng với ngỗng và vịt. Thiên nga và ngỗng có quan hệ gần gũi, cùng được xếp vào phân họ Ngỗng trong đó thiên nga làm thành tông Cygnini. Đôi khi, chúng được phân loại thành một phân họ riêng có tên là Cygninae.'}
choice=''
c1,c2,c3,c4,c5=st.columns(5)
with c1:
  if st.button('Mèo'):
    choice='meo'
with c2:
  if st.button('Chó'):
    choice='cho'
with c3:
  if st.button('Sư tử'):
    choice='sutu'
with c4:
  if st.button('Ngựa'):
    choice='ngua'
with c5:
  if st.button('Thiên nga'):
    choice='thiennga'
with st.sidebar:
  st.write('Thông tin động vật')
  if choice=='':
    st.write('bạn chưa chọn con gì')
  else:
    st.write(dict[choice])
if choice=='':
  st.write('bạn chưa chọn con gì')
elif choice=='meo':
  st.image('https://fagopet.vn/storage/in/r5/inr5f4qalj068szn2bs34qmv28r2_phoi-giong-meo-munchkin.webp')
  st.audio('https://pic.pikbest.com/00/28/50/28s888piCXKr.mp3')
  st.video('https://youtu.be/WeOTW8mCSHQ?si=vIQxBZ6Iu1KgwSkF')
elif choice=='cho':
  st.image('https://kimipet.vn/wp-content/uploads/2022/10/cho-pug-de-thuong.jpg')
  st.audio('https://pic.pikbest.com/00/42/86/714888piCvzr.mp3')
  st.video('https://youtu.be/qxQPPOYoqU0?si=60FDMT4Vb3fGw1-x')
elif choice=='sutu':
  st.image('https://thanksofa.com/wp-content/uploads/Su-tu-Lion-Panthera-leo-ThankSofa-Anh-1.webp')
  st.audio('https://pic.pikbest.com/00/21/58/204888piCCSP.mp3')
  st.video('https://youtu.be/oWc3_C4EtbQ?si=jnlyKKKyrmFbbLEM')
elif choice=='ngua':
  st.image('https://img.cand.com.vn/resize/800x800/NewFiles/Images/2022/11/02/1416hinh_anh_chu_ngua_o_dung_man-1667380309457.jpg')
  st.audio('https://pic.pikbest.com/00/24/25/465888piCQ9H.mp3')
  st.video('https://youtu.be/9m5VxpXKGSk?si=zpB8QIC22Q5Rno_3')
elif choice=='thiennga':
  st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/CygneVaires.jpg/500px-CygneVaires.jpg')
  st.audio('https://pic.pikbest.com/00/86/53/62w888piCGVC.mp3')
  st.video('https://youtu.be/oMfXIJS-1sI?si=g8ZK68ZOHOZ3zja7')
