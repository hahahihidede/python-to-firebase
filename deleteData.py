from firebase import firebase

#declare your database url and make sure to enable write and read setting in your firebase database sett
firebase = firebase.FirebaseApplication('YOUR DATABASE URL', None)


#spesific table of your database (e.g '/-MPmcn2rs3o2xxxqlAY/') and variable you want to delete (e.g 4)
result = firebase.put('SPECIFIED TABLE OF YOUR DATABASE',4)
print('Deleted')
print(result)
