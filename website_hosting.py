import streamlit as st
import pandas as pd
import numpy as np



option = st.sidebar.header(""" 
	#Edo HAnifauzan Satria
	#200411100058
	#Penambangan Data 
	""")
st.sidebar.selectbox("Tugas :",
	('Dissimilarity','Diskritisasi','K-NN','Naive Bayes','K-Means','K-NN dan Decision tree(UTS)','tugas 8','tugas 9','tugas 10'))

if option =='':
	st.write(""" 
		#web apps - Edo HAnifauzan Satria
		#200411100058
		Welcome 
		""")

elif option=='Dissimilarity':
	st.write(""" 
		#Dissimilarity
		""")
elif option=='K-NN':
	st.write(""" 
		#K-NN
		""")
elif option=='Naive Bayes':
	st.write(""" 
		#Naive Bayes
		""")
elif option=='K-Means':
	st.write(""" 
		#K-Means
		""")
elif option=='K-NN dan Decision tree(UTS)':
	st.write(""" 
		#K-NN dan Decision tree(UTS)
		""")
elif option=='tugas 8':
	st.write(""" 
		#tugas 8
		""")
elif option=='tugas 9':
	st.write(""" 
		#tugas 9
		""")
elif option=='Diskritisasi':
	st.write(""" 
		#Diskritisasi
		""")
elif option=='tugas 10':
	st.write(""" 
		#tugas 10
		""")
