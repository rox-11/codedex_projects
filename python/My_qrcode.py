import qrcode


def qr_maker(choose):
    qr = qrcode.QRCode(version = 1, box_size = 5, border = 5)
    
    msg = "\033[0;32m qrcode is uploded\x1b[0m"

    github = "https://github.com/rox-11"
    tryhackme = "https://tryhackme.com/p/rox11"
    snomshell = "https://snomshell.netlify.app/"
    if choose == 1:
        qr.add_data(github)
        qr.make()
        img = qr.make_image(fill_color = 'black', back_color = 'white')
        img.save('github_qr.png')
        print(msg)
    if choose == 2:
        qr.add_data(tryhackme)
        qr.make()
        img = qr.make_image(fill_color = 'black', back_color = 'white')
        img.save('tryhackme_qr.png')
        print(msg)        
    if choose == 3:
        qr.add_data(snomshell)
        qr.make()
        img = qr.make_image(fill_color = 'black', back_color = 'white')
        img.save('snomshell_qr.png')
        print(msg)

print("my accounts and websit \x1b[31mqrcode\x1b[0m ")
print ('''
GITHUB   [\x1b[31m1\x1b[0m]
TRYHACKME[\x1b[31m2\x1b[0m]
SNOMSHELL[\x1b[31m3\x1b[0m]

 ''')
choose = int(input("please select number from \x1b[31m1\x1b[0m to \x1b[31m3\x1b[0m >>"))



try:
      #    choose == int(choose)
    if choose > 3 :
        choose=input("\x1b[31mEROR\x1b[0m please select number from \x1b[31m1\x1b[0m to \x1b[31m3\x1b[0m >>")
    else :
        pass
except :
    pass
qr_maker(choose)

