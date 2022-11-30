while 1:
    #IMPORT_SECTION
    import errno
    import os
    import itertools

    try:
        with open("PSWD_LIST.txt") as f:
            print("FILE ALREADY EXISTS....\n")
            a=int(input("DO YOU WANT TO DELETE THE EXISTING FILE?..\n ENTER  1 TO DELETE THE FILE.....\n 2 TO MAKE A NEW FILE .....\n 3 TO SKIP....\n"))
            if a==1:
                #INPUT_SECTION
                start=int(input("Enter lower limit: "))
                end=int(input("Enter higher limit: "))

                os.remove("PSWD_LIST.txt")
                print("FILE DELETE SUCCESSFUL....\n")
                print("")
                with open("PSWD_LIST.txt","a") as j:
                    #PASSWORD_GENERATION
                    list=["A","a","B","b","C","c","D","d","E","e","F","f","G","g","H","h","I","i","J","j","K","k","L","l","M","m","N","n","O","o","P","p","Q","q","R","r","S","s","T","t","U","u","V","v","W","w","X","x","Y","y","Z","z","!","@","#","$","^","&","*","(",")","_","-","=","+","[","]","{","}","\\","|",";",":","\'","\"",".","<",">",",","/","?","0","1","2","3","4","5","6","7","8","9"]

                    if start<=end and start<=26 and end<=26:
                        for i in range(start,end+1):
                            pswd=itertools.product(list,repeat=i)
                            for i in pswd:
                                j.write(''.join(i)+"\n")
                        print("YOUR PASSWORD FILE IS READY TO USE....")
                    #INVALID_INPUT_HANDELING
                    if start>26 or end>26:
                        print("OUT OF RANGE...WRITE VALUES LESS THAN OR EQUAL TO 26!!!")
                    if start>end:
                        print("GIVEN RANGE IS NOT ITERABLE....")
                    if start==end==0:
                        print("NO PASSWORD GENERATED......")
                j.close()

            elif a==2:
                b=input("ENTER A NAME FOR THE NEW FILE....(WITHOUT .TXT)")
                #INPUT_SECTION
                start=int(input("Enter lower limit: "))
                end=int(input("Enter higher limit: "))

                with open(b+".txt","a") as g:
                    #PASSWORD_GENERATION
                    list=["A","a","B","b","C","c","D","d","E","e","F","f","G","g","H","h","I","i","J","j","K","k","L","l","M","m","N","n","O","o","P","p","Q","q","R","r","S","s","T","t","U","u","V","v","W","w","X","x","Y","y","Z","z","!","@","#","$","^","&","*","(",")","_","-","=","+","[","]","{","}","\\","|",";",":","\'","\"",".","<",">",",","/","?","0","1","2","3","4","5","6","7","8","9"]

                    if start<=end and start<=26 and end<=26:
                        for i in range(start,end+1):
                            pswd=itertools.product(list,repeat=i)
                            for i in pswd:
                                g.write(''.join(i)+"\n")

                    #INVALID_INPUT_HANDELING
                    if start>26 or end>26:
                        print("OUT OF RANGE...WRITE VALUES LESS THAN OR EQUAL TO 26!!!")
                    if start>end:
                        print("GIVEN RANGE IS NOT ITERABLE....")
                    if start==end==0:
                        print("NO PASSWORD GENERATED......")
                g.close()
            elif a==3:
                f.close()
                print("BYE...")
                break
            else:
                print("CHOOSE FROM THE GIVEN NUMBERS......")
        f.close()
    except IOError as e:
        #INPUT_SECTION
        start=int(input("Enter lower limit: "))
        end=int(input("Enter higher limit: "))

        with open("PSWD_LIST.txt","a") as h:
            #PASSWORD_GENERATION
            list=["A","a","B","b","C","c","D","d","E","e","F","f","G","g","H","h","I","i","J","j","K","k","L","l","M","m","N","n","O","o","P","p","Q","q","R","r","S","s","T","t","U","u","V","v","W","w","X","x","Y","y","Z","z","!","@","#","$","^","&","*","(",")","_","-","=","+","[","]","{","}","\\","|",";",":","\'","\"",".","<",">",",","/","?","0","1","2","3","4","5","6","7","8","9"]

            if start<=end and start<=26 and end<=26:
                for i in range(start,end+1):
                    pswd=itertools.product(list,repeat=i)
                    for i in pswd:
                        h.write(''.join(i)+"\n")
    
            #INVALID_  INPUT_HANDELING
            if start>26 or end>26:
                print("OUT OF RANGE...WRITE VALUES LESS THAN OR EQUAL TO 26!!!")
            if start>end:
                print("GIVEN RANGE IS NOT ITERABLE....")
            if start==end==0:
                print("NO PASSWORD GENERATED......")
        h.close()
        print("YOUR PASSWORD LIST IS READY TO USE...")
        if e.errno != errno.ENOENT:
            print("OOPS...SEEMS LIKE SOMETHING WENT DOWN....")
