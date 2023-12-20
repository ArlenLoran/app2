import streamlit as st
import pandas as pd
import datetime
import sqlite3
import oracledb

conn = sqlite3.connect('usuarios.db')
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, email TEXT, usuario TEXT, senha TEXT, status TEXT)")

st.set_page_config(page_title="Teste Arlen")

st.write("testeee")

entrada = st.date_input("input data", datetime.date(2019, 7, 6))

entrada2 = st.text_input("testeeee")

conn = sqlite3.connect('usuarios.db')
c = conn.cursor()
c.execute("SELECT * FROM users")
tr = c.fetchall()

connection = oracledb.connect(user="RBC01PRD_RO", password="rbc012023roDlx09prd",
                                  dsn="USMEGAP004-SCAN.PHX-DC.DHL.COM:1521/RBC01PRD")

cursor = connection.cursor()
cursor.execute(f"""select TRNDTE DATA,
     LODNUM LPN,
     PRTNUM SKU,
     TRNQTY QTD,
     PRT_CLIENT_ID CLIENTE,
     FR_VALUE DE,
     TO_VALUE PARA,
     ins_user_id USUARIO
 from DLYTRN where actcod = 'INVATTCHG' AND prtnum = '21010' and lotnum IN nvl(('202312010000'), lotnum)""",
                   )

result = cursor.fetchall()

def printing():
    conn = sqlite3.connect('usuarios.db')
    c = conn.cursor()
    c.execute("INSERT INTO users ('email', 'usuario', 'senha', 'status') VALUES (?,?,?,?)",
              (entrada, entrada, entrada, entrada))
    conn.commit()

def printing2():
    conn = sqlite3.connect('usuarios.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    st.text_input("aaaa", entrada2)


st.button("ok", on_click=printing)

st.button("pegar", on_click=printing2)

st.table(tr)


st.table(result)
