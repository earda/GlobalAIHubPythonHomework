if __name__ == '__main__':
    a = 2
    warn1 = "You can't go out because it's too dangerous."
    wanr2 = "You can go out the street."
    liste = []
    izin = []
    while a > 0:
        fname = input("Enter your First Name : ")
        lname = input("Enter your Last Name: ")
        age = input("Enter your Age: ")
        byear = input("Enter your BirthDay Year Just date : ")

        liste.append(fname + " " + lname + " " + age + " " + byear)
        if int(age) <= 18:
            izin.append(1)
        if int(age) > 18:
            izin.append(0)
        a = a - 1
    print(f"{liste}")
    for i in izin:
        if i == 1:
            izin.append(warn1)

        elif i == 0:
            izin.append(wanr2)

    print(f"{izin}")
