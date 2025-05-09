import streamlit as st

st.set_page_config(page_title='Thực đơn', page_icon='', layout='wide')
st.title('Chọn món ăn')

gia_khai_vi = {'rau': 10000, 'ruốc': 15000, 'dưa': 8000}
gia_mon_chinh = {'cá': 30000, 'thịt': 35000, 'tôm': 40000}
gia_trang_mieng = {'táo': 10000, 'dưa hấu': 12000, 'cam': 9000}

status = False
hoadon_text = ""

with st.form('form', clear_on_submit=False):
    a = st.multiselect('Món khai vị', list(gia_khai_vi.keys()))
    b = st.multiselect('Món chính', list(gia_mon_chinh.keys()))
    c = st.multiselect('Món tráng miệng', list(gia_trang_mieng.keys()))
    allow_download = st.checkbox("Tạo hóa đơn sau khi xác nhận")
    d = st.form_submit_button('Xác nhận')

    if d:
        if not a:
            st.warning('Bạn chưa chọn món khai vị')
        elif not b:
            st.warning('Bạn chưa chọn món chính')
        elif not c:
            st.warning('Bạn chưa chọn món tráng miệng')
        else:
            tong_tien = 0
            hoadon_text += "=== HÓA ĐƠN THANH TOÁN ===\n\n"

            st.subheader('Món khai vị bạn đã chọn:')
            hoadon_text += "Món khai vị:\n"
            for i in a:
                dong = f"{i} - {gia_khai_vi[i]:,} VND"
                st.write(dong)
                hoadon_text += f"- {dong}\n"
                tong_tien += gia_khai_vi[i]

            st.subheader('Món chính bạn đã chọn:')
            hoadon_text += "\nMón chính:\n"
            for i in b:
                dong = f"{i} - {gia_mon_chinh[i]:,} VND"
                st.write(dong)
                hoadon_text += f"- {dong}\n"
                tong_tien += gia_mon_chinh[i]

            st.subheader('Món tráng miệng bạn đã chọn:')
            hoadon_text += "\nMón tráng miệng:\n"
            for i in c:
                dong = f"{i} - {gia_trang_mieng[i]:,} VND"
                st.write(dong)
                hoadon_text += f"- {dong}\n"
                tong_tien += gia_trang_mieng[i]

            tong_str = f"\nTổng tiền: {tong_tien:,} VND"
            st.success(tong_str)
            hoadon_text += f"\nTổng tiền: {tong_tien:,} VND"

            status = allow_download

if status and hoadon_text:
    with open("hoadon.txt", "w", encoding="utf-8") as f:
        f.write(hoadon_text)

    with open("hoadon.txt", "r", encoding="utf-8") as f:
        st.download_button(
            label="Tải hóa đơn (TXT)",
            data=f,
            file_name="hoa_don.txt",
            mime="text/plain"
        )
