todos = ["task1","task2","task3"]

while True:
    user_choice = input("Enter your choice: ")

    match user_choice:
        case "add":
            todo = input("Enter the task please : ")
            todos.append(todo)
        case "show":
            print(todos)
        
        case "remove":            
            print("1 .Remove by index")
            print("2 .Remove by name")
            remove_type = input("How would you like to remove the task : ")
            if remove_type == "1":
                index = int(input("Enter the position"))
                if index <= 0 :
                    print("invalid index")
                else:
                    del todos[index-1]
            elif remove_type == "2":
                pat = input("Enter the pattern of the task which you want to delete : ")
                shortlen = []

                for task in todos:
                    if pat in task:
                        shortlen.append(task)
                
                if len(shortlen) == 1:
                    todos.remove(shortlen[0])

                else:
                    while True:
                        another_list = shortlen
                        shortlen = []
                        print(another_list)
                        pat = input("We have more than 1 result be specific :")
                        for task in another_list:
                            if pat in task:
                                shortlen.append(task)
                        
                        if len(shortlen) > 1:
                            continue
                        else:
                            todos.remove(shortlen[0])
                            break
                        
        case default:
            exit()
    
