import streamlit as st
import pandas as pd 
import numpy as np
#import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.ensemble import StackingClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
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
    ('Kanker Payudara','Bunga Iris','student_data','Digit Angka')
)
df=pd.read_csv('https://raw.githubusercontent.com/EdoHanifauzan/data/Dataset/student_data.csv')

st.write(f"## Dataset {nama_dataset}")
algoritma= st.sidebar.selectbox(
	'pilih algoritma',
	("SVM","KNN","Random Forest","Decision Tree")
)
def pilih_dataset(nama):
	data=None
	if nama =='Bunga Iris':
		data=datasets.load_iris()
	elif nama =='Kanker Payudara':
		data=datasets.load_breast_cancer()
	elif nama =='Digit Angka':
		data=datasets.load_digits()
	else:
		data= df.to_numpy()
	X =data.data
	y =data.target
	return X ,y


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
	elif nama_algoritma =='Decision Tree':
		max_depth=st.sidebar.slider('max_depth',1,20)
		params['max_depth']=max_depth
	elif nama_algoritma =='Random Forest':
		max_depth=st.sidebar.slider('max_depth',1,20)
		params['max_depth']=max_depth
		n_estimators=st.sidebar.slider('n_estimators',1,100)
		params['n_estimators']=n_estimators
	return params
params=tambah_parameter(algoritma)

def pilih_klasifikasi(nama_algoritma, params):
	algo=None
	if nama_algoritma=='KNN':
		algo=KNeighborsClassifier(n_neighbors=params['K'])
	elif nama_algoritma=='SVM':
		algo=SVC(C=params['C'])
	elif nama_algoritma =='Decision Tree':
		algo= DecisionTreeClassifier(max_depth=params['max_depth'],)
	elif nama_algoritma =='Random Forest':
		algo=RandomForestClassifier(n_estimators=params['n_estimators'],max_depth=params['max_depth'], random_state=4321)
	return algo

algo=pilih_klasifikasi(algoritma, params)

### proses skalifikasi###
X_train, X_test, y_train, y_test=train_test_split(X, y, test_size= 0.25, random_state=4321)

algo.fit(X_train,y_train)
y_pred=algo.predict(X_test)

acc=accuracy_score(y_test, y_pred)
st.write(f'algoritma = {algoritma}')
st.write(f'Akurasi  =', acc)

# proyeksi data PCA #
#pca= PCA(2)
#X_projected = pca.fit_transform(X)
#X1= X_projected[:,0]
#X2= X_projected[:,1]

#fig= plt.figure()
#plt.scatter(X1, X2, c=y, alpha=0.75, cmap='viridis')

#st.pyplot(fig)	
