import streamlit as st
st.set_page_config(page_title="Giới thiệu Calliope Mori", layout="centered")
st.sidebar.title("🎤 Calliope Mori")
st.sidebar.image("https://hololive.hololivepro.com/wp-content/uploads/2020/07/Mori-Calliope_pr-img_01.png", use_container_width=True)
st.sidebar.markdown("""
**Nghệ danh**: Calliope Mori  
**Thuộc nhóm**: Hololive English - Myth  
**Debut**: 12/09/2020  
**Phong cách**: Rap, J-Rap, Hip-hop  
**Bài hát nổi bật**:  
- *Go-Getters*  
- *Red*  
- *End of a Life*
""")
st.title("🎶 Giới thiệu Calliope Mori")
st.subheader("🎧 Nghe thử bài hát End of a life")
audio_url = "https://rr3---sn-i3b7knse.googlevideo.com/videoplayback?expire=1745668661&ei=1XUMaIPcCs6y2roP7-aZoAI&ip=103.16.227.98&id=o-ACMCRjqi-8_bYTHMuZlnEagzatFyg9iq6DWMD6v3uj8D&itag=140&source=youtube&requiressl=yes&xpc=EgVo2aDSNQ%3D%3D&bui=AecWEAbkXQW2n_nr-OsukrGAVlxCCEM0bEuCh3y-HbW3xUdxQf0EN_ZORzlRcV-a-mdFSNY00KtU6yao&vprv=1&svpuc=1&mime=audio%2Fmp4&ns=5Bl6NlmGU15QA-fn-_kf0FoQ&rqh=1&gir=yes&clen=4671448&dur=288.600&lmt=1726230257877416&keepalive=yes&lmw=1&fexp=24350590,24350737,24350827,24350961,24351173,24351429,24351431,24351495,24351528,24351543,24351545,24351638,24351658,24351661,24351662,24351672,24351704,24351790,24351859,51466698&c=TVHTML5&sefc=1&txp=4532434&n=s_teOMzkBjmPyA&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cxpc%2Cbui%2Cvprv%2Csvpuc%2Cmime%2Cns%2Crqh%2Cgir%2Cclen%2Cdur%2Clmt&sig=AJfQdSswRgIhAMMYX85Dv2IoARgctSPy_Gyh19Icl0f6PUiDry4YXOagAiEA9VQ-f-6c4nhponMawwNQkWkLPvHzEFyKGPgYhkuEnCI%3D&rm=sn-x5guiuxaxjvh-jb2z7l,sn-x5guiuxaxjvh-q5jk7d,sn-h55ey7z&rrc=79,79,104&req_id=5531327f7a3da3ee&cmsv=e&rms=nxu,au&redirect_counter=3&cms_redirect=yes&ipbypass=yes&met=1745647136,&mh=XK&mip=1.55.166.242&mm=30&mn=sn-i3b7knse&ms=nxu&mt=1745646745&mv=m&mvi=3&pl=24&lsparams=ipbypass,met,mh,mip,mm,mn,ms,mv,mvi,pl,rms&lsig=ACuhMU0wRAIgPJSM34kDNN_A5ZnD1eXLfiZOCeOgTxMNHkK_u9fQ8UQCIGYxoxSHn-eLOzmgTtnxapw0Bkd3JF4pUsrKUTnSaUpj"
st.audio(audio_url)
st.subheader("📺 Xem MV Go-Getters")
video_url = "https://www.youtube.com/watch?v=j7RbmhKeaZs"
st.video(video_url)
