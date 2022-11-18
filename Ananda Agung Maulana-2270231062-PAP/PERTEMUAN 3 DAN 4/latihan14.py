data="ini adalah string"
print(data)
print(type(data))

#1.cara membuat string

'''
1.dengan menggunakan single quote'...'
2.dengan menggunakan double quote'...'
'''
data ='menggunakan single quote'
print(data)
data="menggunakan double quote"
print(data)

print("halo,apa kabar?")
print("hallo,apa kabar gaes?")
print("ini adalah hari jum'at")

#2.menggunakan tanda \
#membuat tanda' menjadi string
print('mari sholat jum\at')
print("g\day,isn\t it?")

#backlash
print("C:\\user\\UCUP")
#tab
print("ucup\tpotong,semakin jauhan")
#backspace
print("ucup\botong,jadi deketan")
#newline
print("baris pertama.\nbaris kedua.")#LF->UNIX,MACOS,LINUX
print("baris pertama.\rbaris kedua.")#CR->carriage return->commodore,acorn,lisp
print("baris pertama.\r\nbaris kedua.")#CRLF->line feed carriage return->dipakai oleh windows
#3.String literal atau raw
#hati-hati
print("C:\new folder")#akan salah path nya

#menggunakan raw string 
print('r\C:\new folder')

#multiline literal string
print("""
Nama : Ucup
kelas : 3 SD

""")

#MULTILINE literal string dan RAW
print(r"""
Nama : Ucup
kelas : 3 SD\new normal
website : www.ucup.com/newID
""")