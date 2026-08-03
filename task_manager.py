import json
class manager:
    def __init__(self) -> None:
        self.tasks=[]
        self.load()
        pass
    def main(self):
        while True:
            try:
                user=int(input("welcome to task manager!\n1.Add a task\n2.See all tasks\n3.Change status of task\n4.Delete a task\n5.find a task\n6.Exit\n=====>>>"))
                if user==1:
                    name=input("enter the name of task you want to add or 0 for main menu:")
                    if name=="0":
                        continue
                    status=input("enter the status of task you want to add or 0 for main menu:")
                    if status=="0":
                        continue
                    self.add_task(name.capitalize(),status.capitalize())
                    self.list_of_tasks()
                elif user==2:
                    self.list_of_tasks()
                elif user==3:
                    self.list_of_tasks()
                    if not self.tasks:
                        continue
                    else:
                        number=int(input("enter the index of task you want to update or 0 for main menu:"))
                    if number==0:
                        continue
                    if number<1 or number>len(self.tasks):
                        print("please enter valid index:")
                    else:
                        status=input("enter the status which will be updated:")
                        self.update(number,status.capitalize())
                        self.list_of_tasks()
                elif user==4:
                    self.list_of_tasks()
                    if not self.tasks:
                        continue
                    else:
                        number=int(input("enter the index of task you want to delete or 0 for main menu:"))
                    if number==0:
                        continue
                    self.delete_task(number)
                elif user==5:
                    if not self.tasks:
                        continue
                    else:
                        name=input("enter the name of task you want to find or 0 for main menu:")
                    if name=="0":
                        continue
                    self.find_task(name.capitalize())
                elif user==6:
                    print("thank you for visitng task manager!")
                    break
            except ValueError:
                print("please enter integer input")
    def add_task(self,name,status):
        self.tasks.append({"Name":name,"Status":status})
        self.save()
        print("task added successfully")
    def list_of_tasks(self):
        if not self.tasks:
            print("no tasks to manager")
        else:
            print("list of tasks in task manager")
            for index,task in enumerate(self.tasks,1):
                print(f"{index}> {task["Name"]} : {task["Status"]}")
    def update(self,number,status):
        if not self.tasks:
            print("no tasks to manager")
        else:
            if number<1 or number>len(self.tasks):
                print("please enter valid number")
            else:
                self.tasks[number-1]["Status"]=status
                print("task updated successfully")
                self.save()
    def delete_task(self,number):
        if number<1 or number>len(self.tasks):
            print("please enter valid number")
        else:
            self.tasks.pop(number-1)
            print("task removed successfully")
            self.save()
    def find_task(self,name):
        found=False
        if not self.tasks:
            print("no tasks to manager")
        else:
            for index,task in enumerate (self.tasks,1):
                if task["Name"]==name:
                    print(f"it's task number {index}")
                    found=True
            if not found:
                print(f"{name} is not in tasks")
    def back(self):
        self.main()
    def load(self):
        try:
            with open("tasks.json","r")as file:
                self.tasks=json.load(file)
        except FileNotFoundError as f:
            self.tasks=[]
            print(f"error occured {f}")
        except json.JSONDecodeError as j:
            self.tasks=[]
            print(f"error occured {j}")
    def save(self):
        with open("tasks.json","w")as file:
            json.dump(self.tasks,file,indent=4)
user=manager()
user.main()