def main():
    user_name = input("Enter your name: ")
    user_id = int(input("Enter your ID number: "))
    user_score1 = float(input("Enter your First test Score: "))
    user_score2 = float(input("Enter your second test score: "))
    user_score3 = float(input("Enter your third test score: "))
    user_score4 = float(input("Enter your fourth test score: "))
    user_score5 = float(input("Enter your fifth test score: "))

    with open("studentdetails.txt", "w") as file:
        file.write(f" You are {user_name}.\n Your user ID is {user_id}.\n Your first test score is {user_score1}.\n Your second test score is {user_score2}.\n Your third test score is {user_score3}.\n Your fourth test score is {user_score4}.\n Your fifth test score is {user_score5}.")

    with open("studentdetails.txt") as file:
        print(file.readlines())

        dict_value = {
            "name" : user_name,
            "id" : user_id,
            "scores" : [user_score1, user_score2, user_score3, user_score4, user_score5]
        }
    options = int(input("1. Add a student's details into the text file\n2. Search for a student's grade\n3. Read all content in the dictionary\n4. Update a student's grade"))
    if options == 1:
        user_name2 = input("Enter your name: ")
        user_id2 = int(input("Enter your ID number: "))
        user2_score1 = float(input("Enter your First test Score: "))
        user2_score2 = float(input("Enter your second test score: "))
        user2_score3 = float(input("Enter your third test score: "))
        user2_score4 = float(input("Enter your fourth test score: "))
        user2_score5 = float(input("Enter your fifth test score: "))

#To append the file
        with open("studentdetails.txt", "a") as file:
            file.write(f" \n You are {user_name2}.\n Your user ID is {user_id2}.\n Your first test score is {user2_score1}.\n Your second test score is {user2_score2}.\n Your third test score is {user2_score3}.\n Your fourth test score is {user2_score4}.\n Your fifth test score is {user2_score5}.")
            
        with open("studentdetails.txt") as file:
             print(file.readlines())
#A nested dictionary to keep another student's details in the dictionary if option 1 is selcted by the user.
        dict_value = {
        "dict_value1" : {
         "name1" : user_name,
         "id1" : user_id,
        "scores1" : [user_score1, user_score2, user_score3, user_score4, user_score5]
        },
        "dict_value2" : {
        "name2" : user_name2,
        "id2" : user_id2,
        "scores2" : [user2_score1, user2_score2, user2_score3, user2_score4, user2_score5]
        } 
    }
        
    elif options == 3:
        print(dict_value)

    elif options == 2:
      student_name = input("Enter the name to see the student's grade:")
      if student_name == user_name:
            print(user_score1, user_score2, user_score3, user_score4, user_score5)
   
    elif options == 4:
        user_score1 = float(input("Enter your First test Score: "))
        user_score2 = float(input("Enter your second test score: "))
        user_score3 = float(input("Enter your third test score: "))
        user_score4 = float(input("Enter your fourth test score: "))
        user_score5 = float(input("Enter your fifth test score: "))

        with open("studentdetails.txt", "w") as file:
            file.write(f" You are {user_name}.\n Your user ID is {user_id}.\n Your first test score is {user_score1}.\n Your second test score is {user_score2}.\n Your third test score is {user_score3}.\n Your fourth test score is {user_score4}.\n Your fifth test score is {user_score5}.")

        with open("studentdetails.txt") as file:
            print(file.readlines())

main()

