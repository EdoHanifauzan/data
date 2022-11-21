import streamlit as st
import pandas as pd 
import numpy as np




st.sidebar.header(""" Edo Hanifauzan Satria
	200411100058
	Penambangan Data 	""")
option=st.sidebar.selectbox('Tugas :',
	('Dissimilarity','Diskritisasi','K-NN','Naive Bayes','K-Means','K-NN dan Decision tree(UTS)','tugas 8','tugas 9','tugas 10')
)



if option=='Dissimilarity':
	st.write(""" Dissimilarity
		""")
	uploaded_file = st.file_uploader("Upload your input CSV file", type=["csv"])
elif option=='K-NN':
	st.write(""" K-NN
		""")
	uploaded_file = st.file_uploader("Upload your input CSV file", type=["csv"])
elif option=='Naive Bayes':
	st.write(""" Naive Bayes
		""")
	uploaded_file = st.file_uploader("Upload your input CSV file", type=["csv"])
elif option=='K-Means':
	st.write(""" K-Means
		""")
	uploaded_file = st.file_uploader("Upload your input CSV file", type=["csv"])
elif option=='K-NN dan Decision tree(UTS)':
	st.write(""" K-NN dan Decision tree(UTS)
		""")
	uploaded_file = st.file_uploader("Upload your input CSV file", type=["csv"])
elif option=='tugas 8':
	st.write(""" tugas 8
		""")
	uploaded_file = st.file_uploader("Upload your input CSV file", type=["csv"])
elif option=='tugas 9':
	st.write(""" tugas 9
		""")
	uploaded_file = st.file_uploader("Upload your input CSV file", type=["csv"])
elif option=='Diskritisasi':
	st.write(""" Diskritisasi
		""")
	uploaded_file = st.file_uploader("Upload your input CSV file", type=["csv"])
elif option=='tugas 10':
	st.write(""" tugas 10
		""")
	uploaded_file = st.file_uploader("Upload your input CSV file", type=["csv"])
