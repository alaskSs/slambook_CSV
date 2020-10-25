import csv

fo = open('slambook.csv')

objReader = csv.reader(fo)

lsData = list(objReader)

fo.close()

choice = 0

while 1:
    print('*MENU*')
    print('Press 1: To ADD New Record')
    print('Press 2: To EDIT Record')
    print('Press 3: To DISPLAY Specific Record')
    print('Press 4: To DISPLAY Specific Column')
    print('Press 5: To DISPLAY Complete Record')
    print('Press 6: To DELETE Record')
    print('Press 7: To EXIT Application')

    choice = int(input('Please enter your choice : '))

    if choice == 1:

        row = []
        fo = open('slambook.csv', 'a')
        objWriter = csv.writer(fo)

        name = input('Enter your name : ')
        row.append(name)
        address = input('Enter your address : ')
        row.append(address)
        contact = input('Enter your contact no. : ')
        row.append(contact)
        email = input('Enter your email_id : ')
        row.append(email)
        dob = input('Enter your DOB(dd/mm/yy) : ')
        row.append(dob)

        objWriter.writerow(row)
        fo.close()

    elif choice == 2:

        recdata = []
        with open('slambook.csv', 'r') as fo:
            lsData = list(csv.reader(fo))
        b = 1
        for i in lsData:
            print(str(b) + '. ' + i[0])
            b = b + 1
        rec = int(input('Whose record you want to edit : '))
        print("1. Name\n2. Address\n3. Phone no.\n4. E-mail\n5. DOB")
        col = int(input('Which info. you want to edit : '))
        correction = input('Enter Correction : ')
        lsData[rec - 1][col - 1] = correction
        recdata = lsData

        fo = open('slambook.csv', 'w',newline="")
        writer = csv.writer(fo)
        for lines in recdata:
            writer.writerow(lines)
        fo.close()

    elif choice == 3:

        fo = open('slambook.csv', 'r')
        objReader = csv.reader(fo)
        lsData = list(objReader)
        c = 1
        for i in lsData:
            print(str(c) + '. ' + i[0])
            c = c + 1
        rec = int(input('Whose record you want to display :'))
        print("Name\t: " + lsData[rec - 1][0])
        print("Address\t: " + lsData[rec - 1][1])
        print("Phone no.\t: " + lsData[rec - 1][2])
        print("E-mail\t: " + lsData[rec - 1][3])
        print("DOB\t: " + lsData[rec - 1][4])
        fo.close()

    elif choice == 4:

        fo = open('slambook.csv', 'r')
        objReader = csv.reader(fo)
        lsData = list(objReader)
        print("1. Name\n2. Address\n3. Phone no.\n4. E-mail\n5. DOB")
        col = int(input('Which column you want to display :'))
        for i in lsData:
            print(i[col - 1])

    elif choice == 5:

        fo = open('slambook.csv', 'r')
        objReader = csv.reader(fo)
        lsData = list(objReader)
        for i in lsData:
            for j in i:
                print(j + '\t\t'),
            print('\n'),
        fo.close()

    elif choice == 6:

        recdata = []

        fo = open('slambook.csv', 'r')
        objReader = csv.reader(fo)
        lsData = list(objReader)
        d = 1
        for i in lsData:
            print(str(d) + '. ' + i[0])
            d = d + 1
        rec = int(input('Whose record you want to delete :'))
        member = lsData[rec - 1][0]

        for i in lsData:
            if i[0] == member:
                lsData.remove(i)
            recdata = lsData
        fo.close()

        fo = open('slambook.csv', 'w',newline="")
        writer = csv.writer(fo)
        for lines in recdata:
            writer.writerow(lines)
        fo.close()
        print("Record Deleted Successfully")

    else:
        exit()
