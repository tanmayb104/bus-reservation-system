""""
        author: Tanmay Bansal
"""


import math
import sys
import re


class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    def printSolution(self, dist, des):
        print("The minimum distance between the souce and and destination entered is ", dist[des], " kilometers")

    def minDistance(self, dist, sptSet):
        min = 999999
        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v
        return min_index

    def dijkstra(self, src, des):
        dist = [99999] * self.V
        dist[src] = 0
        sptSet = [False] * self.V
        for cout in range(self.V):
            u = self.minDistance(dist, sptSet)
            sptSet[u] = True
            for v in range(self.V):
                if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]
        self.printSolution(dist, des)


class Bus():

    def __init__(self, bus_no, source, destination, pickup_time, dropoff_time, driv_nam, seats_left, tic_price, seats):
        self.bus_no = bus_no
        self.source = source
        self.destination = destination
        self.pickup_time = pickup_time
        self.dropoff_time = dropoff_time
        self.driv_name = driv_nam
        self.seats_left = seats_left
        self.tic_price = tic_price
        self.seats = seats


def login():
    
    flag = 0
    while(flag == 0):

        print("\n1.To login")
        print("2.To signup")
        print("\nEnter your choice: ", end=" ")
        choice = int(input())
        
        if(choice == 1):

            with open('data1.txt','r') as f:

                print("Enter the username: ",end = " ")
                username=input()
                print("Enter the password: ",end = " ")
                password = input()
                
                for line in f:
                    
                    l = line.split()
                    
                    if( username == l[0] ):

                        decrypt_pass=""
                        
                        for i in l[1]:
                            decrypt_pass += chr(ord(i)+1)

                        if(decrypt_pass == password):    
                            print( "Successfully loged in" )
                            flag = 1

                        else:
                            print( "Wrong Password" )
                            flag = 0  
                                                
                    else:                    
                        print( "Wrong username" )
                        flag = 0               
                
        elif(choice == 2):
            
            flag = 1
            print("Enter the username: ",end = " ")
            username=input()
            print("Enter the password: ",end = " ")
            password=input()

            while(len(password) <= 8 or len(password) >= 32 ):
                print("Enter password of length between 8-32 characters")
                print("Enter the password again: ",end=" ")
                password=input()

            print("Enter the password again: ",end=" ")
            re_pass = input()
            
            while(re_pass != password):

                print("Password doesn't match.")
                print("Enter the password again: ",end=" ")
                re_pass = input()

            encripted_pass = ""
            
            for i in password:
                encripted_pass+=chr(ord(i)-1)
                            
            with open('data1.txt','a') as f:
                f.write( username + " " + encripted_pass )
                
        else:
            print("Enter a valid input")


def line1():
    print("*" * 80)


def info():

    print("1.Mumbai")
    print("2.Jaipur")
    print("3.Bangalore")
    print("4.New Delhi")
    print("5.Kolkata")
    print("6.Chennai")
    print("7.Bhopal")
    print("8.Ranchi")
    print("9.Patna")
    print("10.Chandigarh")
    g = Graph(10)

    # All the data below has been taken from the site https://www.distancecalculator.net/country/india and the units of the data are in kilometres

    # This is the original data

    # g.graph = [
    # [0,922,987,1153,1654,1033,660,1375,1452,1355],
    # [922,0,1562,239,1358,1607,439,1040,942,435],
    # [987,1562,0,1744,1560,291,1144,1414,1610,1977],
    # [1153,239,1744,0,1305,1759,601,1002,851,235],
    # [1654,1358,1560,1305,0,1356,1125,322,472,1464],
    # [1033,1607,291,1759,1356,0,1170,1259,1481,1995],
    # [660,439,1144,601,1125,1170,0,810,823,834],
    # [1375,1040,1414,1002,322,1259,810,0,252,1179],
    # [1452,942,1610,851,472,1481,823,252,0,996],
    # [1355,435,1977,235,1464,1995,834,1179,996,0]
    # ]

    # Many values are changed to zero below to show the implementation of dijsktra's algorithm

    g.graph = [
        [0, 922, 987, 0, 1654, 1033, 0, 1375, 1452, 0],
        [922, 0, 1562, 0, 1358, 0, 439, 1040, 0, 435],
        [987, 1562, 0, 1744, 0, 291, 1144, 0, 1610, 0],
        [0, 0, 1744, 0, 1305, 0, 0, 1002, 851, 235],
        [1654, 1358, 0, 1305, 0, 0, 1125, 322, 472, 0],
        [1033, 0, 291, 0, 0, 0, 1170, 0, 0, 1995],
        [0, 439, 1144, 601, 0, 1170, 0, 810, 823, 834],
        [1375, 1040, 0, 1002, 322, 0, 810, 0, 0, 0],
        [1452, 0, 1610, 851, 472, 0, 823, 0, 0, 996],
        [0, 435, 0, 235, 0, 1995, 834, 0, 996, 0]
    ]

    print("Enter the source number from which minimum distance is to be found")
    src = int(input())
    print("Enter the destination number to which the minimum distance is to be found")
    des = int(input())
    g.dijkstra(src - 1, des - 1)


def update():

    print("Enter bus number: ")
    bus_no = input()
    print("Enter source: ")
    source = input()
    print("Enter destination: ")
    destination = input()
    print("Enter pickup_time: ")
    pickup_time = input()
    print("Enter dropoff_time: ")
    dropoff_time = input()
    print("Enter driv_nam: ")
    driv_nam = input()
    seats_left = "32"
    print("Enter ticket price: ")
    tic_price = input()
    seats = [str(x) for x in range(1, 33)]
    bus = Bus(bus_no, source, destination, pickup_time, dropoff_time, driv_nam, tic_price, seats_left, seats)
    l = [bus_no, source, destination, pickup_time, dropoff_time, driv_nam, tic_price, seats_left]
    l += seats
    with open("data.txt", "a") as f:
        f.write(" ".join(l) + "\n")


def delete():

    print("Enter bus number to be deleted: ")
    bus_no = input()
    with open("updates.txt", "w") as f:
        f.write(f"The bus with bus number {bus_no} has been cancelled. We are sorry for the inconvenience caused.\n")
    with open("data.txt", "r+") as f:
        new_f = f.readlines()
        f.seek(0)
        for line in new_f:
            if bus_no not in line:
                f.write(line)
        f.truncate()


def updates():

    print("\n\n")
    with open("updates.txt", "r+") as f:
        new_f = f.readlines()
        f.seek(0)
        for l in new_f:
            print(l)
    print("\n\n")


def bus_avail():

    print("\n\n")
    line1()
    with open("data.txt", "r") as f:
        data = f.readlines()
        for line in data:
            words = line.split()
            print("\n\nbus number: {}   \n\nsource: {}   destination: {} \n\npickup time:{}   dropoff time: {}   \n\ndriver name: {} \n\nPrice of one ticket: {}".format(
                    words.pop(0), words.pop(0), words.pop(0), words.pop(0), words.pop(0), words.pop(0), words.pop(0)))
            words.pop(0)
            print("\nSeats:\n")
            for i in range(len(words)):
                print(words[i]+"\t", end="   ")
                if ((i + 1) % 4 == 0):
                    print()
            print()
            print("\n")
            line1()


def reservation():

    print("\n\nEnter the Bus Number: ")
    bus_number = input()
    with open("data.txt", "r") as f:
        data = f.readlines()
        for line in data:
            words = line.split()
            if (words[0] == bus_number):
                break
    temp = words
    print("\nDiscount Detail:\n\nFor every 5 tickets 5'%' extra discount will be provided")
    print("\nNumber of tickets to Book: ")
    tickets = int(input())
    if (tickets > int(words[7])):
        print(f"\nOnly {words[7]} tickets left")
    else:
        words[7] = str(int(words[7]) - tickets)
        for i in range(8, len(words)):
            print(words[i]+"\t", end="   ")
            if ((i + 1) % 4 == 0):
                print()
        print("\n\nEnter the seat numbers :")
        i = 0
        seats_booked = []
        while (i < tickets):
            seat_no = int(input())
            if (words[7 + seat_no] == "Booked"):
                print("\nThe seat is occupied")
                print("Please choose a different seat\n")
            else:
                words[7 + seat_no] = "Booked"
                i += 1
                seats_booked.append(str(seat_no))
        line1()
        print("\n\t\t\t\tTICKET VIEW")
        print("\n\nbus number: {}   \n\nsource: {}   destination: {}\n\npickup time:{}   dropoff time: {}   \n\ndriver name: {}".format(
                words[0], words[1], words[2], words[3], words[4], words[5]))
        print("\n\nSeat Numbers: ", end=" ")
        print(" ".join(seats_booked))
        print("\n\n")
        print("Price to be paid on arrival point: ", math.ceil(int(words[6]) * tickets * (1 - (tickets // 5) / 20)))
        print("\n\nTake a screenshot of the ticket")
        line1()
        with open("data.txt", "r+") as f:
            new_f = f.readlines()
            f.seek(0)
            for line in new_f:
                if bus_number not in line:
                    f.write(line)
            f.write(" ".join(words) + "\n")
            f.truncate()


def welcome():

    print("\n\nWelcome to DSA's tours and travels")
    print("We serve at many cities inside India")
    print("Few cities we serve in are Mumbai, Chennai, Bangalore, Kolkata, Ranchi, Hyderabad, Jaipur and New Delhi")


def main():

    password = 1234
    while (True):
        print("\n\n1.Add Bus ")
        print("2.Delete Bus ")
        print("3.Updates")
        print("4.Buses Available")
        print("5.Reservation")
        print("6.Information")
        print("7.Exit\n\n")
        print()
        print("Enter your choice: ")
        choice = int(input())
        if (choice == 1):
            print("Input the Password: ")
            if (input() == str(password)):
                update()
            else:
                print("Wrong Password Entered\n\n")
        elif (choice == 2):
            print("Input the Password: ")
            if (input() == str(password)):
                delete()
            else:
                print("Wrong Password Entered\n\n")
        elif (choice == 3):
            updates()
        elif (choice == 4):
            bus_avail()
        elif (choice == 5):
            reservation()
        elif (choice == 6):
            info()
        elif (choice == 7):
            break
        else:
            print("Please enter a valid choice\n\n")


if __name__ == "__main__":
    welcome()
    login()
    main()