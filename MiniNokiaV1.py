import time
import random
import string
import keyboard
a=1
print("Hello World")  
b = input("What is your name? ")
print("Hello " + b + ",  Welcome to MiniNokiaV1! ") 
while a==1:
 c=1
 print("What would you like to do? ")
 n=input('"1. Calculator" \n "2. Date/Time" \n "3. Games" \n "4. Exit "\n')
 if n=='1':     
      while c==1:
         print("Opening Calculator... \n \n")
         time.sleep(2)
         n1 = int(input("Enter first number: "))
         n2 = int(input("Enter second number: "))
         op = input("Enter operator (+, -, *, /): ")
         if op=='+':
            print(str(n1) + " + " + str(n2) + " = " + str(n1 + n2))
         elif op=='-':
            print(str(n1) + " - " + str(n2) + " = " + str(n1 - n2))
         elif op=='*': 
            print(str(n1) + " * " + str(n2) + " = " + str(n1 * n2))
         elif op=='/':
            if n2 != 0:
               print(str(n1) + " / " + str(n2) + " = " + str(n1 / n2))
            else:
               print("Noob, Division by zero is not allowed.")
         print("Want To Close Calculator? (y/n) \n")
         close = input()
         if close == 'y':
            c = 0   
 if n=='2':
    print("Displaying Date/Time... \n \n")
    print("Press Ctrl+C to stop the clock.")
    print(time.strftime("%d/%m/%y"))
    try:
      while True:
         print(time.strftime("%I:%M:%S %p"), end="\r")
         time.sleep(1)
    except KeyboardInterrupt:
       c=0
       print("\nTime Go Fishing...")
 if n=='3':
    c=1
    print("Opening Games... \n \n")
    time.sleep(2)
    print("    Reaction Time Game !! \n ")
    print(" Press the Key that appears, fast af! \n \n")
    time.sleep(4)
    while c==1:
       print("Readyyy...")
       time.sleep(2)
       print("Set")
       time.sleep(1)
       print("Go!! \n")
       time.sleep(0.5)
       k1 = random.choice(string.ascii_lowercase + string.digits + ".,/;'[]-=\\`")
       print(k1 + "\n")
       start = time.time()
       if keyboard.read_key(suppress=True) == k1:
          end = time.time()
          rt1 = end - start
          print("Reaction Time : " + str(rt1) + "s \n")
          print("    Round 2!! \n")
          time.sleep(1)
       else:
          print("Noob, Wrong Key Idiot. Round 2!! \n")
          rt1 = 0
          time.sleep(1)
       print("Readyyy...")
       time.sleep(2)
       print("Set")
       time.sleep(1)
       print("Go!! \n")
       time.sleep(0.5)
       k2 = random.choice(string.ascii_lowercase + string.digits + ".,/;'[]-=\\`")
       print(k2 + "\n")
       start = time.time()
       if keyboard.read_key(suppress=True) == k2:
          end = time.time()
          rt2 = end - start
          print("Reaction Time : " + str(rt2) + "s \n")
          print("    Round 3!! \n")
          time.sleep(1)
       else:
          print("Noob, Wrong Key Idiot. Round 3!! \n")     
          rt2 = 0
          time.sleep(1)
       print("Readyyy...")
       time.sleep(2)
       print("Set")
       time.sleep(1)
       print("Go!! \n")
       time.sleep(0.5)
       k3 = random.choice(string.ascii_lowercase + string.digits + ".,/;'[]-=\\`")
       print(k3 + "\n")
       start = time.time()
       if keyboard.read_key(suppress=True) == k3:
          end = time.time()
          rt3 = end - start
          print("Reaction Time : " + str(rt3) + "s \n")
          print("    GG!! \n")
          time.sleep(1)
       else:
          print("Noob, Wrong Key Idiot. \n")
          rt3 = 0
          print("    GG!! \n")     
          time.sleep(1)
       rt1 = rt1
       rt2 = rt2
       rt3 = rt3
       if (rt1 == 0 and rt2 == 0) or (rt1 == 0 and rt3 == 0) or (rt2 == 0 and rt3 == 0):
           rt = (rt1 + rt2 + rt3) / 1
       elif (rt1 == 0 and rt2 != 0 and rt3 != 0) or (rt2 == 0 and rt1 != 0 and rt3 != 0) or (rt3 == 0 and rt1 != 0 and rt2 != 0):
           rt = (rt1 + rt2 + rt3) / 2
       elif rt1 != 0 and rt2 != 0 and rt3 != 0:
           rt = (rt1 + rt2 + rt3) / 3
       else:
           rt = 10    
       print("Your Avg Reaction Time : " + str(rt) + "s \n")
       if rt < 0.8:
          print("Your Reaction time is of an F1 driver! \n")
       elif rt < 1.6:
          print("Your Reaction time is of a soldier! \n")
          print("Keep trying and find out below 0.8s whose reaction time do you have..  \n")
       elif rt < 2.4:
          print("Your Reaction time is of a normal human! \n")  
          print("Keep trying and find out below 1.6s whose reaction time do you have..  \n")
       elif rt ==10:
          print("Noob all wrong keys! \n")  
          print("Keep trying and find out below 2.4s whose reaction time do you have..  \n")
       else:
          print("Your Reaction time is worse than a snail! \n")  
          print("Keep trying and find out below 2.4s whose reaction time do you have..  \n")  
       time.sleep(7)
       print("Want To Play Aagain? (y/n) \n")
       if input() == 'y':
            continue
       else:
            c=0
 if n=='4':
    a=0
    print("Goodbye " + b) 
    continue 
 if c==0:
    continue 
 else:
    print("Noob, don't know how to do that. try again idiot.") 
print("Thank you for using MiniNokiaV1, my first program! ")       