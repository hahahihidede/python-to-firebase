from firebase import firebase


firebase = firebase.FirebaseApplication('https://dede-8abcf-default-rtdb.firebaseio.com/testData', None)
data =  (
    {'Nama': 'Dede Rohmat', 'Alamat': 'Tangerang Selatan', 'Height': 160.2 }, 
    {'Nama': 'Maman', 'Alamat': 'Merkurius', 'Height': 180.1 }, 
    {'Nama': 'Andi Odang', 'Alamat': 'Pluto Selatan', 'Height': 155.7 },
    {'Nama': 'Uvuvwevwe', 'Alamat': 'Zimbabwe Utara', 'Height': 169.9 }
)
result = firebase.post('/',data)
print(result)
