from firebase import firebase

#declare your database url and make sure to enable write and read setting in your firebase database sett
firebase = firebase.FirebaseApplication('YOUR DATABASE URL', None)


#spesific table of your database (e.g '/-MPmcn2rs3o2xxxqlAY/') and variable you want to add/update to firebase
result = firebase.put('SPECIFIED TABLE OF YOUR DATABASE',
                      4, {'Nama' : 'Susilo Bambang Pamungkas', 'Alamat' :  'Wakanda', 'Height': 178.1}) #data you want to add/update to firebase
print('updated')
print(result)
