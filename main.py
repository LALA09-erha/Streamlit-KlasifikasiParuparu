# import libary 
import streamlit as st
import metode
import time


# pige title
st.set_page_config(
    page_title="Klasifikasi Penyakit Paru-paru",
    page_icon="https://png.pngtree.com/png-clipart/20190520/original/pngtree-red-lung-pink-lung-tube-cartoon-illustration-hand-drawn-organ-illustration-png-image_3874739.jpg",
)

    # 0 = tidak ada penyakit jantung
    # 1 = ada penyakit jantung

# hide menu
hide_streamlit_style = """



<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>

"""
st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.4.0/css/font-awesome.min.css">', unsafe_allow_html=True)
# st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
# st.markdown(' <div style="position: fixed; top: 0; left: 0; z-index: 9999; width: 100%; background: rgb(14, 17, 23); ; text-align: center;"><a href="https://github.com/LALA09-erha/Streamlit---WebPrediksiKNN" target="_blank"><button style="border-radius: 12px;position: relative; top:50%; margin:10px;"><i class="fa fa-github"></i> Source Code</button></a><a href="https://lala09-erha.github.io/datamining/intro.html" target="_blank"><button  style="border-radius: 12px;position: relative; top:50%;"><i style="color: orange" class="fa fa-book"></i> Jupyter Book</button></a></div>', unsafe_allow_html=True)



# insialisasi web
st.markdown("<p style='text-align: center; color: white; margin:0 ; padding:0;'>MENU</p>", unsafe_allow_html=True)
kolom = st.columns((2.2, 0.48, 2.7))
home = kolom[1].button('🏠')
about = kolom[2].button('About')

# home page
if home==False and about==False or home==True and about==False:
    st.markdown("<h1 style='text-align: center; color: white; margin:0 ; padding:0;'>Klasifikasi Penyakit Paru-paru</h1>", unsafe_allow_html=True)
    # setting kolom
    # with st.expander("Setting"):

    #     preprosesing = st.radio('Preprocessing Data', options=['Normalization (Min-Max)', 'Normal'], index=0, horizontal=True)
    #     st.markdown("""---""")
    #     st.write("""Metode Klasfikasi""")

    #     model_1 = st.checkbox('K-Nearest Neighbors (K=11) ', value=True)
    #     model_2 = st.checkbox('Bagging Clasifier (Gaussian) ')
    #     model_3 = st.checkbox('Random Forest')

    col1, col2 = st.columns(2)
    with col1:
        nama = st.text_input("Masukkan Nama",placeholder='Nama')
    with col2:
        umur = st.number_input("Masukkan Umur",max_value=100)
    col9,col10 = st.columns(2)
    with col9:
        jk = st.selectbox("Jenis Kelamin",('Laki-laki','Perempuan'))
    with col10:
        batuk = st.selectbox("Batuk",('Ya','Tidak'))

    col3,col4 = st.columns(2)
    with col3:
        spek = st.number_input("Kualitas Oksigen Anda",min_value=0,max_value=1000)
    with col4:
        nafas = st.number_input("Jumlah Nafas Dalam 1 Menit",min_value=0,max_value=1000)
    col5,col6 = st.columns(2)
    with col5:
         nadi = st.number_input("Denyut Nadi Dalam 1 Menit",min_value=0,max_value=100)
    with col6:
         berat = st.number_input("Berat Badan (kg)",min_value=0,max_value=100)
    
    col11,col12 = st.columns(2)
    with col11:
        sesak = st.selectbox("Sesak",('Ya','Tidak'))
    with col12:
        parukesan = st.selectbox("Suara Nafas Paru",('Mengi/Bising Gesek','Normal'))
    col7,col8= st.columns(2)
    with col7:
         sistol = st.number_input("Tekanan Sistolik (mmHG)",min_value=0,max_value=1000)
    with col8:
         diastol = st.number_input("Tekanan Diastolik (mmHG)",min_value=0,max_value=1000)
    #    Centering Butoon 
    columns = st.columns((2, 0.6, 2))
    sumbit = columns[1].button("Submit")
    if sumbit == True:

        if  nama != '' and jk != '' and spek != 0 and nafas != 0 and umur != 0:
                    # cek jenis kelamin
                    #0 = laki-laki
                    #1 = perempuan
                    if jk == 'Laki-laki':
                        jk = 0
                    else:
                        jk = 1
                    # tensi 
                    tensi = metode.def_tensi(umur,sistol,diastol)
                    if(tensi == 'Rendah'):
                        tensi = 2
                    elif(tensi == 'Normal'):
                        tensi = 0
                    else:
                        tensi = 1
                    # batuk
                    if batuk == 'Ya':
                        batuk = 1
                    else:
                        batuk = 0
                    # sesak
                    if sesak == 'Ya':
                        sesak = 1
                    else:
                        sesak = 0
                    # paru kesan
                    if parukesan == 'Mengi/Bising Gesek':
                        parukesan = 1
                    else:
                        parukesan = 0
                    # normalisasi 
                    # ,UMUR,JENKEL,BATUK,SESAK,SPESIFIKASI,PARU-KESAN,NAFAS,NADI,BB,TENSI
                    normalisasi = metode.normalisasi([ umur, jk, batuk, sesak, spek, parukesan, nafas, nadi, berat, tensi])
                    # klasifikasi
                    klasifikasi = metode.svm(normalisasi)
                    # cek klasifikasi
                    with st.spinner("Tunggu Sebentar Masih Proses..."):
                        if klasifikasi[-1] == 0:
                            time.sleep(1)
                            st.success("Hasil klasifikasi : **"+nama+"** Tidak Ada Penyakit Paru-paru")
                            st.balloons()
                        else:
                            time.sleep(1)
                            st.warning("Hasil klasifikasi : **"+nama+"** Ada Penyakit Paru-paru")        
                            st.write("Silahkan Untuk Periksa Lebih Lanjut Ke Dokter" )
        else:
            st.error("Harap Diisi Semua Kolom")

# about page
if about==True and home==False:
    st.markdown("<h2 style='text-align: center; color: white; margin:0 ; padding:0;'>Tentang Sistem ini</h2>", unsafe_allow_html=True)
    st.write('Sistem ini dibuat untuk mempermudah dalam proses diagnosa **dini** Penyakit paru-paru, menggunakan metode **SVM**')
    st.markdown("<h4 style='text-align: center; color: white; margin:0 ; padding:0;'>Tentang Paramater Pemeriksaaan dan Cara Mengetahui</h4>", unsafe_allow_html=True)
    st.write('**Tekanan Kualitas Oksigen** adalah Kualitas Oksigen yang berada pada tubuh anda. Cara mengetahuinya menggunakan Alat Pantau Oksigen dalam Tubuh / **Oximeter**')
    st.write('**Denyut Nadi** adalah Denyut Nadi yang berada pada tubuh anda. Cara mengetahuinya cukup dengan memegang bagian leher anda dan hitung berapa kali anda merasa dalam 1 menit')
    st.write('**Suara Nafas Paru** adalah Suara Nafas yang berada pada tubuh anda. Cara mengetahuinya dengan menarik nafas dalam-dalam dan hembuskan nafas')
    st.write('**Tekanan Sistolik** adalah tekanan darah pada saat jantung memompa darah atau saat berkontraksi, sedangkan **Diastolik** adalah tekanan darah pada saat jantung relaksasi. Cara mengetahuinya dengan menggunakan alat **tensi menter**')