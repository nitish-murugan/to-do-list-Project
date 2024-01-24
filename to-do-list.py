import csv
while(1):
    print("\n\t\t MENU ")
    print("-------------------------------------------")
    print("Press 1 for adding new tasks\nPress 2 for removing a task\nPress 3 for viewing the remaining task\nPress 4 to exit")
    choice = int(input("Enter your choice => "))
    if choice == 1:
        with open("to-do-list.csv","a") as fileObject:
            writer = csv.writer(fileObject)
            loop = 'y'
            while(loop == 'y'):
                desp = input("Enter the task => ")
                writer.writerow([desp])
                loop = input("Do you want to add any other task(y/n) ?! ").lower()
        fileObject.close()
    elif choice == 2:
        with open("to-do-list.csv","r") as fileObject:
            reader = csv.reader(fileObject)
            lst = list(reader)
            z = int(0)
            while(z<(len(lst))):
                if(lst[z] == [] or lst[z] == [' ']):
                    del lst[z]
                    z = z - 1
                z = z + 1
            for i in range(len(lst)):
                print(i+1," => ",lst[i][0])
            rem = int(input("Which task is to be removed?: "))-1
            flag = int(0)
            try:
                del lst[rem]
                flag = int(1)
            except:
                print("Please enter the right option")
        fileObject.close()
        if(flag):
            with open("to-do-list.csv","w") as fileObject:
                writer = csv.writer(fileObject)
                for i in lst:
                    writer.writerow(i)
            print("Task deleted successfully")
            fileObject.close()
    elif choice == 3:
        print("The remaining tasks are")
        with open("to-do-list.csv","r") as fileObject:
            reader = csv.reader(fileObject)
            lst = list(reader)
            z = int(0)
            while(z<(len(lst))):
                if(lst[z] == [] or lst[z] == [' ']):
                    del lst[z]
                    z = z - 1
                z = z + 1
            for i in range(len(lst)):
                print(i+1," => ",lst[i][0])
    elif choice == 4:
        break
    else:
        print("Enter the right choice")
