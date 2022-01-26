#usr/bin/python
xush_kelibsiz = 'Kalkulyatorga Xush Kelibsiz!\n'
print(xush_kelibsiz)
chiqish = str(input('Agar Dasturni To\'xtatishni Hohlasangiz <exit> So\'zini Kiriting:\nDavom Ettirish Uchun <go> So\'zini Kiriting:  '))
if chiqish== 'exit':
    exit()

calculator = input('Amallardan Birini Tanlang!\n1: Qo\'shish\n2: Ayirish\n3: Ko\'paytirish\n4: Bo\'lish>>')
if calculator== '1':
    savol = int(input('1-Sonni Kiriting: '))
    savol2 = int(input('2-Sonni Kiriting:'))
    print('Javobi>', int(savol) + int(savol2))
    
elif calculator== 'Qo\'shish':
    savol = int(input('1-Sonni Kiriting: '))
    savol2 = int(input('2-Sonni Kiriting:'))
    print('Javobi>', int(savol) + int(savol2))

elif calculator== 'qo\'shish':
    savol = int(input('1-Sonni Kiriting: '))
    savol2 = int(input('2-Sonni Kiriting:'))
    print('Javobi>', int(savol) + int(savol2))

elif calculator== 'qoshish':
    savol = int(input('1-Sonni Kiriting: '))
    savol2 = int(input('2-Sonni Kiriting:'))
    print('Javobi>', int(savol) + int(savol2))
    
elif calculator== 'Qoshish':
    savol = int(input('1-Sonni Kiriting: '))
    savol2 = int(input('2-Sonni Kiriting:'))
    print('Javobi>', int(savol) + int(savol2))

elif calculator== '2':
    savol = int(input('1-Sonni Kiriting: '))
    savol2 = int(input('2-Sonni Kiriting: '))
    print('Javobi>', int(savol) - int(savol2))

elif calculator== 'Ayirish':
    savol = int(input('1-Sonni Kiriting: '))
    savol2 = int(input('2-Sonni Kiriting: '))
    print('Javobi>', int(savol) - int(savol2))

elif calculator== 'ayirish':
    savol = int(input('1-Sonni Kiriting: '))
    savol2 = int(input('2-Sonni Kiriting: '))
    print('Javobi>', int(savol) - int(savol2))

elif calculator== '3':
    savol = int(input('1-Sonni Kiriting: '))
    savol2 = int(input('2-Sonni Kiriting: '))
    print('Javobi>', int(savol) * int(savol2))

elif calculator== 'Ko\'paytirish':
    savol = int(input('1-Sonni Kiriting: '))
    savol2 = int(input('2-Sonni Kiriting: '))
    print('Javobi>', int(savol) * int(savol2))

elif calculator== 'ko\'paytirish':
    savol = int(input('1-Sonni Kiriting: '))
    savol2 = int(input('2-Sonni Kiriting: '))
    print('Javobi>', int(savol) * int(savol2))

elif calculator== 'kopaytirish':
    savol = int(input('1-Sonni Kiriting: '))
    savol2 = int(input('2-Sonni Kiriting: '))
    print('Javobi>', int(savol) * int(savol2))

elif calculator== 'Kopaytirish':
    savol = int(input('1-Sonni Kiriting: '))
    savol2 = int(input('2-Sonni Kiriting: '))
    print('Javobi>', int(savol) * int(savol2))

elif calculator== '4':
    savol = int(input('1-Sonni Kiriting: '))
    savol2 = int(input('2-Sonni Kiriting: '))
    print('Javobi>', int(savol) / int(savol2))

elif calculator== 'Bo\'lish':
    savol = int(input('1-Sonni Kiriting: '))
    savol2 = int(input('2-Sonni Kiriting: '))
    print('Javobi>', int(savol) / int(savol2))

elif calculator== 'bo\'lish':
    savol = int(input('1-Sonni Kiriting: '))
    savol2 = int(input('2-Sonni Kiriting: '))
    print('Javobi>', int(savol) / int(savol2))

elif calculator== 'Bolish':
    savol = int(input('1-Sonni Kiriting: '))
    savol2 = int(input('2-Sonni Kiriting: '))
    print('Javobi>', int(savol) / int(savol2))

elif calculator== 'bolish':
    savol = int(input('1-Sonni Kiriting: '))
    savol2 = int(input('2-Sonni Kiriting: '))
    print('Javobi>', int(savol) / int(savol2))

else:
    print('Iltimos Qaysi Amalni Bajarish Kerak Ekanligini Aniqroq Kiriting!')

tugatish = input('Dasturni To\'xtatish Uchun Hohlagan So\'zingizni Kiriting>')
exit()