todos = ["apple","orange","banana","Your most important task is to become the most successful person in the world"]
p = len(todos)+1
todos_dict = dict()
i = 1
for task in todos:
    todos_dict["Task no. {0} : ".format(i)] = task
    i+=1

print("============ Welcome to my Todo Application in Python ============")

def show():
        print()
        print("Tasks        ||     Description")
        print("-----        ||     -----------")
        for key,values in todos_dict.items():
            print(key+"||  "+     values)
        print()

while True:
    print("So what would you like to choose ?")
    print("1. Add \n2. Show \n3. Edit \n4. Remove \n5. Exit")
    user_choice = input("Enter your choice: ")


    match user_choice:
        case "add" | "1":
            while True:
                todo = input("Enter the task please : ")
  
                todos_dict.update({"Task no. {0} : ".format(p) : todo})
                p+=1
                ans = input("Do you want to continue adding tasks ? [ Y / n] ?")
                if ans == "Y" or ans == "y":
                    continue
                else:
                    break
        case "show" | "2":
            # print(todos_dict)
            show()

        case "edit" | "3":
            while True:
                try:
                    edit_task = int(input("Tell us which task you want to edit :"))
                except:
                    print()
                    print("It is requested by the user to put an integer value !")
                    continue

                if edit_task > len(todos_dict) or edit_task < 0:
                    print("invalid task number")
                else:
                    ans = input("Enter the task content : ")
                    # print("Task no. {0} : ".format(edit_task))
                    todos_dict.update({"Task no. {0} : ".format(edit_task) : ans})
                
                que = input("Do you want to continue ? [ Y / n] : ")
                if que == "Y" or que == "y":
                    continue
                else:
                    break

        case "remove" | "4":            
            while True:
                    print("Please choose which task you want to remove !")
                    show()
                    index = int(input("Enter the position : "))
                    if index <= 0 :
                        print("invalid index")
                        x = input("Do you still want to continue [Y/n] ? : ")
                        if x == "Y" or x == "y":
                            continue
                        else:
                            break
                    else:
                        try:
                            del todos_dict["Task no. {0} : ".format(index)]
                        except:
                            print("Actually the key does not exist ! I think you should try other index !")
                            print()
                        x = input("Do you still want to continue [Y/n] ? : ")
                        if x == "Y" or x == "y":
                            continue
                        else:
                            break
                
        case "exit" | "5":
            exit()
        
        
    
