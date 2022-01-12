"""
1/12/2022
"""

from os import system
print('1. Ping Google')
print('2. Ping Facebook')
print('3. Ping Instagram')
print('4. Ping Popsci')
print('5. Ping Discovery')
print('6. Ping Cnn')
print('7. Ping Abc')
print('8. Ping custom URL')
key = int(input('Input your choice: '))
if key == 1:
        system("ping www.google.com")
elif key == 2:
        system("ping www.facebook.com")
elif key == 3:
        system("ping www.instagram.com")
elif key == 4:
        system("ping www.popsci.com")
elif key == 5:
        system("ping www.discovery.com")
elif key == 6:
        system("ping www.cnn.com")
elif key == 7:
        system("ping www.abc.com")
elif key == 8:
        url = input('Enter URL: ')
        system("ping " + url)
else:
        print("Invalid Option!")