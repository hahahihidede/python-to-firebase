from firebase import firebase

#declare your database url and make sure to enable write and read setting in your firebase database sett
firebase = firebase.FirebaseApplication('YOUR DATABASE URL', None)
#variable that you want to send
data =  (
    {'Nama': 'Dede Rohmat', 'Alamat': 'Tangerang Selatan', 'Height': 160.2 }, 
    {'Nama': 'Maman', 'Alamat': 'Merkurius', 'Height': 180.1 }, 
    {'Nama': 'Andi Odang', 'Alamat': 'Pluto Selatan', 'Height': 155.7 },
    {'Nama': 'Uvuvwevwe', 'Alamat': 'Zimbabwe Utara', 'Height': 169.9 }
)

#spesific table of your database (e.g '/-MPmcn2rs3o2xxxqlAY/') and variable you want to send to database(e.g data)
result = firebase.get('SPECIFIED TABLE OF YOUR DATABASE', data)
print(result)
