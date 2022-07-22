# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
class Restaurant_Reservation_System:

    def __init__(self, name, date, time, no_adults, no_child):
        self.name = name
        self.date = date
        self.time = time
        self.no_adults = no_adults
        self.no_child = no_child

    def add(self, name, date, time, no_adults, no_child):
        ob = Restaurant_Reservation_System(name, date, time, no_adults, no_child)
        reserve.append(ob)

    def view(self, reserve):
        if (len(reserve) == 0):
            return print("No data found!")
        elif (len(reserve) > 0):
            ctr = 0
            title_num = "No"
            title_date = "Date"
            title_time = "Time"
            title_name = "Name"
            title_adults = "Adults"
            title_children = "Children"
            title_subtotal = "Sub-Total"
            print("%-15s %-15s %-15s %-15s %-15s %-15s %s" % (
            title_num, title_date, title_time, title_name, title_adults, title_children, title_subtotal))
            for ctr in range(len(reserve)):
                no = ctr
                date = reserve[ctr].date
                time = reserve[ctr].time
                name = reserve[ctr].name
                adults = reserve[ctr].no_adults
                children = reserve[ctr].no_child
                subtotal = reserve[ctr].no_adults * 1200 + reserve[ctr].no_child * 800
                print("%-15s %-15s %-15s %-15s %-15s %-15s %s" % (no, date, time, name, adults, children, subtotal))

            print("\n-------------------------------Nothing follows")

    def delete(self, reserve):
        if (len(reserve)==0):
            return print("No data found!")
        elif (len(reserve)>0):
            ctr = 0
            res_num = int(input("Please enter reservaton number: "))

            if (res_num < 0):
                print ("Invalid reservation number!")
                return

            del reserve[res_num]
            print("Record deleted successfully.")

    def gen_rep(self, reserve, no_adults, no_child ):

        obj.view(reserve)

        if (len(reserve) == 0):
            return print ("No Data found!")
        elif(len(reserve) > 0):
            ctr = 0
            total_adults = 0
            total_child = 0
            total_adultsprice = 0
            total_childprice = 0

            for ctr in range (len(reserve)):

                total_adults += reserve[ctr].no_adults
                total_child += reserve[ctr].no_child
                total_adultsprice += reserve[ctr].no_adults * 1200
                total_childprice += reserve[ctr].no_child * 800

            print("Total no of Adults: ",  total_adults)
            print("total no of Children: ", total_child)
            print("Grand total: ", total_adultsprice + total_childprice)



reserve = []
obj = Restaurant_Reservation_System(' ', ' ', ' ', '  ', ' ')
if __name__ == '__main__':

    print("================== RESTAURANT RESERVATION SYSTEM")
    print("==================")

    print ("\n")

    while(True):
        print("a. View all Reservations"
              "\nb. Add Reservations"
              "\nc. Delete Reservations"
              "\nd. Generate Report"
              "\ne. Exit")

        print("Enter your choice: ")
        ch = input()

        if ch == 'a' or ch == 'A':
            obj.view(reserve)
        elif ch == 'b' or ch == 'B':
            print("Name: ")
            name = input()
            print("Date of reservation (mm/dd/yyyy): ")
            date = input()
            print("Time of reservation (hh:mm AM/PM): ")
            time =  input()
            print("No of adults: ")
            no_adults = int(input())
            print("No of Kids: ")
            no_child = int(input())
            obj.add(name, date, time, no_adults, no_child)
            print("Record Added Successfully.")
        elif ch == "c" or ch == "C":
            obj.delete(reserve)
        elif ch == "d" or ch == "D":
            obj.gen_rep(reserve, no_adults, no_child)
        elif ch == "e" or ch == "E":
            exit()

        os.system("pause")
        os.system('cls')




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
