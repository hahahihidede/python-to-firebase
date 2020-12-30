from firebase import firebase
import json

firebase = firebase.FirebaseApplication('https://dede-8abcf-default-rtdb.firebaseio.com/testData/', None)
data = firebase.get('/-MPmcn2rs3o2AXTfqlAY/', '')
for d in data:
    print (d['Nama'])
    print (d['Alamat'])
    print (d['Height'])

