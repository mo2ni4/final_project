import streamlit as st
from streamlit_gsheets import GSheetsConnection

#ydata profiling
import pandas as pd
from ydata_profiling import ProfileReport

#report untuk streamlit
from streamlit_pandas_profiling import st_profile_report

st.set_page_config(
    page_title="🏁 Final Project Dashboard 🏆",
    page_icon="👨🏻‍🎓",
    #layout="wide", 
)


#--------------Judul Dashboard (margin tengah)
st.markdown("<h1 style='text-align: center;'> Employee Profiling </h1>",
            unsafe_allow_html=True)
st.markdown("---")


#------read data
conn = st.connection("gsheet", type=GSheetsConnection)
df = conn.read(
    spreadsheet = st.secrets.gsheet_employee["spreadsheet"],
    worksheet = st.secrets.gsheet_employee["worksheet"]
)

#-------------Sidebar selection
with st.sidebar:
    st.subheader("Data Filtering")
    st.markdown("---")
    pilihan_bu = st.selectbox(
        "Pilih Business Unit:",
        options = df['Business Unit'].unique(),
        index=None
)
if pilihan_bu is None:
    st.write("Anda tidak menentukan pilihan Business Unit, maka data dasboard akan mencakup seluruh Business Unit")

else:
    bu = df[df['Business Unit'] == pilihan_bu]
    ##output
    st.write(f"Anda memilih Business Unit {pilihan_bu}. Dashboard selanjutnya hanya akan menampilkan Business Unit yang sudah dipilih.")

#---------------buat button di sidebar
if st.sidebar.button ("Start Profiling Data"):
    # Menampilkan konten dalam tab-tab
    tabs = st.tabs(["Complete Dashboard", "Simple Dashboard"])

    # Konten Tab 1
    with tabs[0]:
        #------generate report
        if pilihan_bu == "Speciality Products":
            dfprod = conn.read(
                spreadsheet = st.secrets.gsheet_product["spreadsheet"],
                worksheet = st.secrets.gsheet_product["worksheet"]
            )
            prprod = ProfileReport (dfprod)
            st_profile_report(prprod)
        elif pilihan_bu == "Corporate":
            dfcorp = conn.read(
                spreadsheet = st.secrets.gsheet_corporate["spreadsheet"],
                worksheet = st.secrets.gsheet_corporate["worksheet"]
            )
            prcorp = ProfileReport (dfcorp)
            st_profile_report(prcorp)
        elif pilihan_bu == "Manufacturing":
            dfmanu = conn.read(
                spreadsheet = st.secrets.gsheet_manufacturing["spreadsheet"],
                worksheet = st.secrets.gsheet_manufacturing["worksheet"]
            )
            prmanu = ProfileReport (dfmanu)
            st_profile_report(prmanu)
        elif pilihan_bu == "Research & Development":
            dfrnd = conn.read(
                spreadsheet = st.secrets.gsheet_rnd["spreadsheet"],
                worksheet = st.secrets.gsheet_rnd["worksheet"]
            )
            prrnd = ProfileReport (dfrnd)
            st_profile_report(prrnd)
        else:
            pr = ProfileReport (df)
            st_profile_report(pr)
            
        

    # Konten Tab 2
    with tabs[1]:
        #------generate report
        if pilihan_bu == "Speciality Products":
            prprod2 = ProfileReport (
            dfprod,
            minimal=True,
            orange_mode=True,
            title="Simple Employee Profiling",
            explorative=True,
            sensitive=True,
            dark_mode=True
            )
            st_profile_report(prprod2)
        elif pilihan_bu == "Corporate":
            prcorp2 = ProfileReport (
            dfcorp,
            minimal=True,
            orange_mode=True,
            title="Simple Employee Profiling",
            explorative=True,
            sensitive=True,
            dark_mode=True
            )
            st_profile_report(prcorp2)
        elif pilihan_bu == "Manufacturing":
            prmanu2 = ProfileReport (
            dfmanu,
            minimal=True,
            orange_mode=True,
            title="Simple Employee Profiling",
            explorative=True,
            sensitive=True,
            dark_mode=True
            )
            st_profile_report(prmanu2)
        elif pilihan_bu == "Research & Development":
            prrnd2 = ProfileReport (
            dfrnd,
            minimal=True,
            orange_mode=True,
            title="Simple Employee Profiling",
            explorative=True,
            sensitive=True,
            dark_mode=True
            )
            st_profile_report(prrnd2)
        else:
            pr2 = ProfileReport (
            df,
            minimal=True,
            orange_mode=True,
            title="Simple Employee Profiling",
            explorative=True,
            sensitive=True,
            dark_mode=True
            )
            st_profile_report(pr2)
    
else:
    st.info("Click button in the left sidebar to generate data report")   
