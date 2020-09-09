
import datetime

def getdate():
    return datetime.datetime.now()

def log_func(client):
    if client=="1":
        exer_diet=input("Enter no. 1 for Exercise,2 for diet:\n")
        add_items=input("what do you want to add? :\n")
        if exer_diet=="1":
            with open("Saurabh_exer.txt","a") as f:
                add=["[",getdate(),"]",add_items,"\n"]
                for item in add:
                    f.write("%s"%item)
            print("item successfully added")

        elif exer_diet=="2":
            with open("Saurabh_diet.txt", "a") as f:
                add = ["[", getdate(), "]", add_items, "\n"]
                for item in add:
                    f.write("%s" % item)
            print("item successfully added")
    elif client=="2":
        exer_diet = input("Enter no. 1 for Exercise,2 for diet:\n")
        add_items = input("what do you want to add? :\n")
        if exer_diet == "1":
            with open("Tamanna_exer.txt", "a") as f:
                add = ["[", getdate(), "]", add_items, "\n"]
                for item in add:
                    f.write("%s" % item)
            print("item successfully added")

        elif exer_diet == "2":
            with open("Tamanna_diet.txt", "a") as f:
                add = ["[", getdate(), "]", add_items, "\n"]
                for item in add:
                    f.write("%s" % item)
            print("item successfully added")

    else:
        exer_diet = input("Enter no. 1 for Exercise,2 for diet:\n")
        add_items = input("what do you want to add? :\n")
        if exer_diet == "1":
            with open("Babeena_exer.txt", "a") as f:
                add = ["[", getdate(), "]", add_items, "\n"]
                for item in add:
                    f.write("%s" % item)
            print("item successfully added")

        elif exer_diet == "2":
            with open("Babeena_diet.txt", "a") as f:
                add = ["[", getdate(), "]", add_items, "\n"]
                for item in add:
                    f.write("%s" % item)
            print("item successfully added")
def retrieve_func(client):
    if client=="1":
        exer_diet=input("Enter number 1 for exercise 2 for diet:\n ")
        if exer_diet=="1":
            try:
                with open("Saurabh_exer.txt") as f:
                    for i in (f.readlines()):
                        print(i)
            except:
                print("items can't retrive,plzz add items in file")

        elif exer_diet=="2":
            try:
                with open("Saurabh_diet.txt") as f:
                    for i in (f.readlines()):
                        print(i)
            except:
                print("items can't retrive,plzz add items in file")
    elif client=="2":
        exer_diet = input("Enter number 1 for exercise 2 for diet:\n ")
        if exer_diet == "1":
            try:
                with open("Tamanna_exer.txt") as f:
                    for i in (f.readlines()):
                        print(i)
            except:
                print("items can't retrive,plzz add items in file")

        elif exer_diet=="2":
            try:
                with open("Tamanna_diet.txt") as f:
                    for i in (f.readlines()):
                        print(i)
            except:
                print("items can't retrive,plzz add items in file")

    else:
        exer_diet = input("Enter number 1 for exercise 2 for diet:\n ")
        if exer_diet == "1":
            try:
                with open("Babeena_exer.txt") as f:
                    for i in (f.readlines()):
                        print(i)
            except:
                print("items can't retrive,plzz add items in file")

        elif exer_diet=="2":
            try:
                with open("Babeena_diet.txt") as f:
                    for i in (f.readlines()):
                        print(i)
            except:
                print("items can't retrive,plzz add items in file")

client=input("Enter number 1 for Saurabh ,2 for Tamanna,3 for Babeena:\n")

log_retrive=input("Enter 1 for log ang 2 for retrive\n")

if log_retrive=="1":
    log_func(client)
elif log_retrive=="2":
    retrieve_func(client)
