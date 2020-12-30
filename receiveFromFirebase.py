#import firebase library
from firebase import firebase
 
#declare your database url and make sure to enable write and read setting in your firebase database setting
firebase = firebase.FirebaseApplication('YOUR DATABASE URL', None)

#spesific table of your database (e.g '/-MPmcn2rs3o2xxxqlAY/')
data = firebase.get('SPECIFIED TABLE OF YOUR DATABASE', '')

#column you want to fetch
for d in data:
    print (d['Nama'])
    print (d['Alamat'])
    print (d['Height'])

