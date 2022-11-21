import streamlit as st
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KneighborsClassifier
from sklearn.decomposition import PCA


st.title("Aplikasi Web Data Mining")
st.write("""
	#menggunakan algoritma dan dataset mana yang memiliki akurasi terbaik?
	""")

st.sidebar.header(""" Edo Hanifauzan Satria
	200411100058
	Penambangan Data 	""")

st.sidebar.subheader('User Input Features')

st.sidebar.markdown("""
[student_data file source :](https://raw.githubusercontent.com/EdoHanifauzan/data/Dataset/student_data.csv)
""")

nama_dataset= st.sidebar.selectbox(
    'pilih Dataset',
    ('BUnga Iris','Kanker Payudara','Digit Angka','student_data')
)

st.write(f"## Dataset {nama_dataset}")

algoritma= st.sidebar.selectbox(
	'pilih algoritma',
	('KNN',"SVM","Random Forest")
)

def pilih_dataset(nama):
	data=None
	if nama =='BUnga Iris':
		data=dataset.load_iris()
	elif nama =='Kanker Payudara':
		data=dataset.load_breast_cancer()
	elif nama =='Digit Angka':
		data=dataset.load_digits()
	elif nama =='Dataset user':
		data= pd.read_csv('https://raw.githubusercontent.com/EdoHanifauzan/data/Dataset/student_data.csv')
	X =data.data
	y =data.target
	return X ,y

if data is not None:
	st.write("dataset :")
	st.write(data)

X, y = pilih_dataset(nama_dataset)
st.write('Jumlah Baris dan Kolom :',X.shape)
st.write('Jumlah kelas :',len(np.unique(y)))

def tambah_parameter(nama_algoritma):
	params=dict()
	if nama_algoritma =='KNN':
		K=st.sidebar.slider('K',1,20)
		params['K']=K
	elif nama_algoritma =='SVM':
		C=st.sidebar.slider('C',0.01,20.0)
		params['C']=C
	elif nama_algoritma =='Random Forest':
		max_depth=st.sidebar.slider('max_depth',1,20)
		params['max_depth']=max_depth
		n_estimators=st.sidebar.slider('n_estimators',1,100)
		params['n_estimators']=n_estimator
	return params
params=tambah_parameter(algoritma)

def pilih_klasifikasi(nama_algoritma, params):
	algo=None
	if nama_algoritma=='KNN':
		algo=KneighborsClassifier(n_neighbors=params['K'])
	elif nama_algoritma=='SVM':
		algo=SVCr(Cs=params['C'])
	elif nama_algoritma=='KNN':
		algo=RandomForestClassifier(n_estimators=params['n_estimators'],max_depth=params['max_depth'], random_state=4321)
	return algo

algo=pilih_klasifikasi(algoritma, parsams)

### proses skalifikasi###
X_train, X_test, y_train, y_test=train_test_split(X, y, test_size= 0.25, random_state=4321)

algo.fit(X_train,y_train)
y_pred=algo.predict(X_test)

acc=accuracy_score(y_test, y_pred)

st.write(f'algoritma = {algoritma}')
st.write(f'Akurasi  =', a)

# proyeksi data PCA #
#pca= PCA(2)
#X_projected = pca.fit_transform(X)
#X1= X_projected[:,0]
#x2= X_projected[:,1]

#fig= plt.figure()
#plt.scatter(x1, x2, c=y, alpha=0.75, cmap='viridis')

#plt.xlabel('principal Component 1')
#plt.ylabel('principal Component 2')
#plt.colorbar

#st.pyplot(fig)	
