import joblib
import pandas as pd

# preprocessing
def normalisasi(x):
    # import data test
    data_test = pd.read_csv('data/testingdata.csv')
    data_test = data_test.drop(data_test.columns[0], axis=1)
    # memasukkan data kedalam data test
    cols = data_test.columns
    df = pd.DataFrame([x], columns=cols)
    data_test = data_test.append(other=df, ignore_index=True)
    
    for col in cols:
        data_test[col] = data_test[col] / data_test[col].max()
    return data_test

def svm(x):
    return joblib.load('model/modelSVMRISET.pkl').predict(x)

def def_tensi(umur,sistol,dias):
  if umur >= 14 and umur <= 18 :
    if(sistol < 90 and dias <50):
      return "Rendah"
    elif (90 <= sistol <= 120) and (50 <= dias <=80):
      return "Normal"
    else:
      return "Tinggi"
  elif umur >= 19 and umur <= 40:
    if(sistol < 95 and dias <60):
      return "Rendah"
    elif (95 <= sistol <= 135) and (60 <= dias <=80):
      return "Normal"
    else:
      return "Tinggi"
  elif umur >= 41 and umur <=60 :
    if(sistol < 110 and dias < 70):
      return "Rendah"
    elif (110 <= sistol <= 145) and (70 <= dias <=90):
      return "Normal"
    else:
      return "Tinggi"
  elif umur > 60 :
    if(sistol < 95 and dias < 70):
      return "Rendah"
    elif (95 <= sistol <= 145) and (70 <= dias <=90):
      return "Normal"
    else:
      return "Tinggi"
  else:
    if(sistol < 80 and dias < 45):
      return "Rendah"
    elif (80 <= sistol <= 120) and (45 <= dias <=80):
      return "Normal"
    else:
      return "Tinggi"
