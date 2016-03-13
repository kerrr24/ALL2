import tkinter as tk
from tkinter import *
import ctypes
import random
import time



currentNode = 't'

graph = {'s': {'a': 3, 'c': 7, 'd': 7},
            'a': {'s': 3, 'b': 2, 'c':3, 't': 3},
            'b': {'c': 5, 'a': 2, 'd': 3},
            'c': {'a': 3, 'b': 5, 's': 7},
            'd': {'b': 3, 't': 5, 's': 7},
            't': {'d': 5,'a': 3}}


#imgCred =  (PhotoImage(file='Credits.png'))
#imgSelctLev = (PhotoImage(file='SelectLevel.png'))

#Shop Contents and prices
itemsAv = ["Tryes" , "Suspension", "Windows", "Spoiler", "Engine", "Exhaughst", "Brakes", "Pink Fluffy Dice", "MOT", "Paint Job", "Gear Stick", "Seats"]
shopDict = {
    'ShopA' : {'Tryes': '450', 'Suspension': '1000' , 'MOT' : '150'},
    'ShopB' : {'Tryes': '475', 'Windows': '675', 'Spoiler': '350'},
    'ShopC' : {'Windows': '750' , 'Suspension': '875' , 'Gear Stick' : '135'},
    'ShopD' : {'Suspension': '1050' , 'Spoiler': '350'},
    'ShopS' : {'Engine' : '1000' , 'Exhaughst' : '450' , 'Pink Fluffy Dice' : '60'},
    'ShopT' : {'Brakes' : '650' , 'Paint Job' : '650' , 'Seats' : '345'}}
gotItems = {}
gotItemArray = []
totalMoney = 0
neededItems = []
moneySpent = 0
randomInt = 0
currentFuel = 0
lastFuelUsage = 0
testList = []
gameMade = False
currentPage = "StartPage"
loopAdd =0
loopGot = 0
totalGot = 0
ballLoop = 0
tempList = []
CostOfItem = []
distanceTraveledtoShop = "0"
findNode = ' '
searc = False
nodeTo = ""
done = False
Started = False
temp = []
user = "COM"
COMnextNODE = ''
COMCurrentNode = ''
shopBasket = []
diff = ""
COMRoute = []
neededItemSearch = False
COMScore = 0
COMFuel = 0
COMMoney = 0
COMused = False
            
            

class gameActions():

    def __init__(self):
            pass

    def searchDict(searchItem):
        
        global tempList
        global CostOfItem
        if searchItem in shopDict['ShopA']:
              tempList.append("ShopA" + shopDict['ShopA'][str(searchItem)])
              print(tempList)
              CostOfItem.append(int(shopDict['ShopA'][str(searchItem)]))
              print(CostOfItem)
              
        if searchItem in shopDict['ShopB']:
              tempList.append("ShopB" + shopDict['ShopB'][str(searchItem)])
              print(tempList)
              CostOfItem.append(int(shopDict['ShopB'][str(searchItem)]))
              print(CostOfItem)
              
        if searchItem in shopDict['ShopC']:
              tempList.append("ShopC" + shopDict['ShopC'][str(searchItem)])
              print(tempList)
              CostOfItem.append(int(shopDict['ShopC'][str(searchItem)]))
              print(CostOfItem)

        if searchItem in shopDict['ShopD']:
              tempList.append("ShopD" + shopDict['ShopD'][str(searchItem)])
              print(tempList)
              CostOfItem.append(int(shopDict['ShopD'][str(searchItem)]))
              print(CostOfItem)

        if searchItem in shopDict['ShopT']:
              tempList.append("ShopT" + shopDict['ShopT'][str(searchItem)])
              print(tempList)
              CostOfItem.append(int(shopDict['ShopT'][str(searchItem)]))
              print(CostOfItem)

        if searchItem in shopDict['ShopS']:
              tempList.append("ShopS" + shopDict['ShopS'][str(searchItem)])
              print(tempList)
              CostOfItem.append(int(shopDict['ShopS'][str(searchItem)]))
              print(CostOfItem)

        #Insertion sort

        for i in range(1, len(CostOfItem)):
            val = CostOfItem[i]
            j = i - 1
            while (j >= 0) and (CostOfItem[j] > val):
                CostOfItem[j+1] = CostOfItem[j]
                j = j - 1
                CostOfItem[j+1] = val

        print(CostOfItem)


        poppedItem = str(CostOfItem.pop(0))
        print(poppedItem)

        #Linear Search
        n = 0
        while n in range(0, len(tempList) +1):
            if poppedItem  not in str(tempList[n]):
                    n = n + 1
                    print("Here")
            else:
                    shopName = tempList[n][:5]
                    global COMnextNODE
                    if shopName == "ShopA":
                        COMnextNODE = 'a'
                    if shopName == "ShopB":
                        COMnextNODE = 'b'
                    if shopName == "ShopC":
                        COMnextNODE = 'c'
                    if shopName == "ShopD":
                        COMnextNODE = 'd'
                    if shopName == "ShopT":
                        COMnextNODE = 't'
                    if shopName == "ShopS":
                        COMnextNODE = 's'
                    print(shopName + (" sells the cheapest ") + str(searchItem) + (" at a cost of £") + str(poppedItem))
                    n = len(tempList) + 1
                    cheapShop =  messagebox.showinfo('',shopName + (" sells the cheapest ") + str(searchItem) + (" at a cost of £") + str(poppedItem)) 
                
            

        n = 0  
        tempList = []
        CostOfItet = []

    def nearestShop(searchItem):
            global searc
            searc = True
            theSum = 1
            global done
            done = False
            aDone = False
            bDone = False
            cDone = False
            dDone = False
            tDone = False
            sDone = False
            global COMnextNODE 
        
            
            if searchItem in shopDict['ShopA'] and aDone == False:
                if currentNode == 'a':
                      closestshop = messagebox.showinfo('',"You are currently at the closest shop that sells " + str(searchItem))
                      done = True
                      COMnextNODE = 'a'
                else:
                          nodeToA = 'a'
                          dijkstraA(graph , 'a' , currentNode)
                          tempList.append(str(distanceTraveledtoShop) +"a")
                          
                          aDone = True

             
            if searchItem in shopDict['ShopB'] and bDone == False:
                if currentNode == 'b':
                      closestshop = messagebox.showinfo('',"You are currently at the closest shop that sells " + str(searchItem))
                      done = True
                      COMnextNODE = 'b'
                else:
                          nodeToB = 'b'
                          dijkstraB(graph , 'b' , currentNode)
                          tempList.append(str(distanceTraveledtoShop) +"b")
                          
                          bDone = True
            
            if searchItem in shopDict['ShopC'] and cDone == False:
                if currentNode == 'c':
                      closestshop = messagebox.showinfo('',"You are currently at the closest shop that sells " + str(searchItem))
                      done = True
                      COMnextNODE = 'c'
                else:
                          nodeToC = 'c'
                          dijkstraC(graph , 'c' , currentNode)
                          tempList.append(str(distanceTraveledtoShop) +"c")
                          
                          cDone = True
            
            if searchItem in shopDict['ShopD'] and dDone == False:
                if currentNode == 'd':
                      closestshop = messagebox.showinfo('',"You are currently at the closest shop that sells " + str(searchItem))
                      done = True
                      COMnextNODE = 'd'
                else:
                          nodeToD = 'd'
                          dijkstraD(graph , 'd' , currentNode)
                          tempList.append(str(distanceTraveledtoShop) +"d")
                          
                          dDone = True
            
            if searchItem in shopDict['ShopT'] and tDone == False:
                if currentNode == 't':
                      closestshop = messagebox.showinfo('',"You are currently at the closest shop that sells " + str(searchItem))
                      done = True
                      COMnextNODE = 't'
                else:
                  nodeToT = 't'
                  dijkstraT(graph , 't' , currentNode)
                  tempList.append(str(distanceTraveledtoShop) +"t")
                  
                  tDone = True
            
            if searchItem in shopDict['ShopS'] and sDone == False:
                  if currentNode == 's':
                      closestshop = messagebox.showinfo('',"You are currently at the closest shop that sells " + str(searchItem))
                      done = True
                      COMnextNODE = 's'
                  else:
                          nodeToS = 's'
                          dijkstraS(graph , 's' , currentNode)
                          tempList.append(str(distanceTraveledtoShop) +"s")
                        
                          
                          sDone = True
            searc = False
            if done != True:
                print(tempList)
                gameActions.cocktailshakersort(searchItem)
                
    def cocktailshakersort(searchItem):
        if done == False:
                passed = 0
                swapped = True
                while swapped == True:
                    swapped = False
                    if passed % 2 == 0:
                        for i in range(len(tempList) - 1):
                            if tempList[i] > tempList[i+1]:
                                tempList[i], tempList[i+1] = tempList[i+1], tempList[i]
                                swapped = True
                                print(tempList)
                    else:
                        for i in range(len(tempList) - 1, 0,-1):
                            if tempList[i] < tempList[i - 1]:
                                tempList[i - 1], tempList[i] = tempList[i], tempList[i-1]
                                swapped = True
                                print(tempList)
                    passed = passed + 1

                print(tempList)
                closestNodeshop = str(tempList.pop(0))
                length = len(closestNodeshop)-1
                closestNodeshopName = closestNodeshop[length : length + 1]
                closestNodeshopValue = closestNodeshop[0 : length]
                print(closestNodeshopName)
                print(closestNodeshopValue)

                if closestNodeshopName == 'a':
                    shop = "ShopA"
                    global COMnextNODE
                    COMnextNODE = 'a'
                    closestshop = messagebox.showinfo('',"The closest shop that sells " + str(searchItem) + " is " + shop + " which is " + closestNodeshopValue + " fuel away")
                if closestNodeshopName == 'b':
                    shop = "ShopB"
                    global COMnextNODE
                    COMnextNODE = 'b'
                    closestshop = messagebox.showinfo('',"The closest shop that sells " + str(searchItem) + " is " + shop + " which is " + closestNodeshopValue + " fuel away")
                if closestNodeshopName == 'c':
                    shop = "ShopC"
                    global COMnextNODE
                    COMnextNODE = 'c'
                    closestshop = messagebox.showinfo('',"The closest shop that sells " + str(searchItem) + " is " + shop + " which is " + closestNodeshopValue + " fuel away")
                if closestNodeshopName == 'd':
                    shop = "ShopD"
                    global COMnextNODE
                    COMnextNODE = 'd'
                    closestshop = messagebox.showinfo('',"The closest shop that sells " + str(searchItem) + " is " + shop + " which is " + closestNodeshopValue + " fuel away")
                if closestNodeshopName == 't':
                    shop = "ShopT"
                    global COMnextNODE
                    COMnextNODE = 't'
                    closestshop = messagebox.showinfo('',"The closest shop that sells " + str(searchItem) + " is " + shop + " which is " + closestNodeshopValue + " fuel away")
                if closestNodeshopName == 's':
                    shop = "ShopS"
                    global COMnextNODE
                    COMnextNODE = 's'
                    closestshop = messagebox.showinfo('',"The closest shop that sells " + str(searchItem) + " is " + shop + " which is " + closestNodeshopValue + " fuel away")
                global tempList    
                tempList = []


                
               # global tempList
                tempList = []
               # done = False
                searc = False

                
    
      
    def addtoList(self):
            lbNeed.insert(itemRan)

    def MakeUser():
        global user
        user = "player"
        gameActions.loopDictCheck()

    def loopDictCheck():
            global currentPage
            currentPage = ""
            global currentFuel
            currentFuel = 0
            global totalMoney
            totalMoney = 6000
            print(totalMoney)
            global currentNode
            ranNode = random.choice(list(graph.keys()))
            currentNode = ranNode
            print(ranNode)
            global randomInt
            if diff == "Easy" or diff == "Med":
                randomInt = random.randint(1,4)
            else:
                randomInt = random.randint(2,8)
            n = 0
            num = 0
            while num < randomInt:
                itemRan = random.choice(itemsAv)

                if itemRan not in neededItems:
                    neededItems.append(itemRan)
                    print(str(neededItems))
                    #gameActions.bubble(neededItems)
                    num = num + 1
                    if randomInt <= 4 or user == "COM":
                        global neededItems
                        gameActions.bubble(neededItems)
            if user == "player":
                if randomInt > 4:
                            global neededItems
                            gameActions.quickSort(neededItems)
                            neededItems = temp
                            print(neededItems)
                update.updater(False)


            
            

    def quickSort(theList):
        print("Started")
        
        thisDone = False
        less = []
        equal = []
        greater = []
        k = 0
        i = 0
        if len(theList) > 1:
            pivot = theList[k]
            while thisDone == False:
                if i < len(theList):
                    if theList[i] < theList[k]:
                        less.append(theList[i])
                        i = i + 1
                        
                if i < len(theList):
                        
                    if theList[i] == theList[k]:
                        equal.append(theList[i])
                        i = i + 1
                        
                if i < len(theList):   
                         
                    if theList[i] > theList[k]:
                         greater.append(theList[i])
                         i = i + 1

                    print( str(less) + "!" + str(equal) + "!" + str(greater))
                if i >= len(theList):
                    theList = less + equal + greater
                    less = []
                    equal = []
                    greater = []
                    i = 0
                    k = k + 1
                    if k == len(theList):
                        print(theList)
                        thisDone = True

            print(theList)
            global temp
            temp = theList
            print(temp)
                

              


    def bubble(listToSort):
            print("Ran bubbleSort")
            print(" ")
            print(" ")
            
            length = len(listToSort) - 1
            sorted = False
            print("Before: " + str(listToSort))
            while not sorted:
                    sorted = True
                    for i in range(length):
                        
                        if listToSort[i] > listToSort[i+1]:
                            sorted = False
                            listToSort[i], listToSort[i+1] = listToSort[i+1], listToSort[i]
                    print(listToSort)
                    
                            
            print("After: " + str(listToSort))
            if gotItemArray == neededItems:
                    print("Game Won")
                


    def FuelLeft(lastFuelUsage):
            global currentFuel
            if currentFuel < 0 :
                    print("Game Over: No fuel left!")
                    if gameMade == True:
                        SampltotalGoteApp.restartGame()
            else:
                if searc == False:
                    print(currentFuel)
                    currentFuel = currentFuel + lastFuelUsage
                    print("Fuel Used: " + str(currentFuel))
                else:
                    global distanceTraveledtoShop
                    distanceTraveledtoShop = lastFuelUsage
            


    def neededReset():
            del neededItems[:]
            del gotItemArray[:]
            del testList[:]
            global gotItems
            gotItems = {}
            update.updater(True)
            

    def close_window(): 
            shop.withdraw()

    def close_handler():
            shop.iconify()
            #after(1000, me.shop.deiconify)

    def pressC1():
            cost = shopDict['ShopC']['Windows']
               
            if totalMoney >= int(cost) and 'Windows' not in gotItems:
                        gotItems['Windows'] = cost
                        print (gotItems)
                        global totalMoney
                        global moneySpent
                        totalMoney = totalMoney - int(cost)
                        moneySpent = moneySpent + int(cost)
                        print(moneySpent)
                        print(totalMoney)
                        if 'Windows' in neededItems:
                            neededItems.remove('Windows')
                        gotItemArray.append("Windows")
                        print("1: " + str(gotItemArray))
                        print("2: " + str(neededItems))
                        gameActions.bubble(gotItemArray)
                        global totalGot
                        totalGot = totalGot + 1
                        update.addToGot()
                        global testList 
                        if 'Windows' in gotItemArray:
                            if 'Windows' in neededItems:
                                testList.append('Windows')
                        if neededItems == []:
                            print("Game Won")
                            SampleApp.GameWon()
                        else:
                            pass
            elif 'Windows' in gotItems:
                print("Can't buy more than one of the aame upgrade")
                sameUpgrade = messagebox.showinfo('', "Can't buy more than one of the aame upgrade")


    def pressD2():

            cost = shopDict['ShopD']['Spoiler']
                
            if  totalMoney >= int(cost) and 'Spoiler' not in gotItems:
                        gotItems['Spoiler'] = cost
                        print (gotItems)
                        global totalMoney
                        global moneySpent
                        totalMoney = totalMoney - int(cost)
                        moneySpent = moneySpent + int(cost)
                        print(totalMoney)
                        print(moneySpent)
                        if 'Spoiler' in neededItems:
                            neededItems.remove('Spoiler')
                        gotItemArray.append("Spoiler")
                        
                        print("1: " + str(gotItemArray))
                        print("2: " + str(neededItems))
                        gameActions.bubble(gotItemArray)
                        global totalGot
                        totalGot = totalGot + 1
                        update.addToGot()
                        global testList 
                        if 'Spoiler' in gotItemArray:
                            if 'Spoiler' in neededItems:
                                testList.append('Spoiler')
                        if neededItems == []:
                            print("Game Won")
                            SampleApp.GameWon()
                        else:
                            pass
            elif 'Spoiler' in gotItems:
                print("Can't buy more than one of the same upgrade")
                sameUpgrade = messagebox.showinfo('', "Can't buy more than one of the same upgrade")


    def pressD1():

            cost = shopDict['ShopD']['Suspension']
                
            if  totalMoney >= int(cost) and 'Suspension' not in gotItems:
                        gotItems['Suspension'] = cost
                        print (gotItems)
                        global totalMoney
                        global moneySpent
                        totalMoney = totalMoney - int(cost)
                        moneySpent = moneySpent + int(cost)
                        print(totalMoney)
                        print(moneySpent)
                        if 'Suspension' in neededItems:
                            neededItems.remove('Suspension')
                        gotItemArray.append("Suspension")
                        print("1: " + str(gotItemArray))
                        print("2: " + str(neededItems))
                        gameActions.bubble(gotItemArray)
                        global totalGot
                        totalGot = totalGot + 1
                        update.addToGot()
                        global testList 
                        if 'Suspension' in gotItemArray:
                            if 'Suspension' in neededItems:
                                testList.append('Suspension')
                        if neededItems == []:
                            print("Game Won")
                            SampleApp.GameWon()
                        else:
                            pass
            elif 'Suspension' in gotItems:
                print("Can't buy more than one of the aame upgrade")
                sameUpgrade = messagebox.showinfo('', "Can't buy more than one of the aame upgrade")
                

    def pressC2():


            cost = shopDict['ShopC']['Suspension']
                
            if  totalMoney >= int(cost) and 'Suspension' not in gotItems:
                        gotItems['Suspension'] = cost
                        print (gotItems)
                        global totalMoney
                        global moneySpent
                        totalMoney = totalMoney - int(cost)
                        moneySpent = moneySpent + int(cost)
                        print(moneySpent)
                        print(totalMoney)
                        if 'Suspension' in neededItems:
                            neededItems.remove('Suspension')
                        gotItemArray.append("Suspension")
                        print("1: " + str(gotItemArray))
                        print("2: " + str(neededItems))
                        gameActions.bubble(gotItemArray)
                        global totalGot
                        totalGot = totalGot + 1
                        update.addToGot()
                        global testList 
                        if 'Suspension' in gotItemArray:
                            if 'Suspension' in neededItems:
                                testList.append('Suspension')
                        if neededItems == []:
                            print("Game Won")
                            SampleApp.GameWon()
                        else:
                            pass
            elif 'Suspension' in gotItems:
                print("Can't buy more than one of the aame upgrade")
                sameUpgrade = messagebox.showinfo('', "Can't buy more than one of the aame upgrade")


    def pressC3():


            cost = shopDict['ShopC']['Gear Stick']
                
            if  totalMoney >= int(cost) and 'Gear Stick' not in gotItems:
                        gotItems['Gear Stick'] = cost
                        print (gotItems)
                        global totalMoney
                        global moneySpent
                        totalMoney = totalMoney - int(cost)
                        moneySpent = moneySpent + int(cost)
                        print(moneySpent)
                        print(totalMoney)
                        if 'Gear Stick' in neededItems:
                            neededItems.remove('Gear Stick')
                        gotItemArray.append("Gear Stick")
                        print("1: " + str(gotItemArray))
                        print("2: " + str(neededItems))
                        gameActions.bubble(gotItemArray)
                        global totalGot
                        totalGot = totalGot + 1
                        update.addToGot()
                        global testList 
                        if 'Gear Stick' in gotItemArray:
                            if 'Gear Stick' in neededItems:
                                testList.append('Gear Stick')
                        if neededItems == []:
                            print("Game Won")
                            SampleApp.GameWon()
                        else:
                            pass
            elif 'Gear Stick' in gotItems:
                print("Can't buy more than one of the aame upgrade")
                sameUpgrade = messagebox.showinfo('', "Can't buy more than one of the aame upgrade")
                    
    def pressA1():

            cost = shopDict['ShopA']['Tryes']
                
            if  totalMoney >= int(cost) and 'Tryes' not in gotItems:
                        gotItems['Tryes'] = cost
                        print (gotItems)
                        global totalMoney
                        global moneySpent
                        totalMoney = totalMoney - int(cost)
                        moneySpent = moneySpent + int(cost)
                        print(totalMoney)
                        print(moneySpent)
                        if 'Tryes' in neededItems:
                            neededItems.remove('Tryes')
                        gotItemArray.append("Tryes")
                        print("1: " + str(gotItemArray))
                        print("2: " + str(neededItems))
                        gameActions.bubble(gotItemArray)
                        global totalGot
                        totalGot = totalGot + 1
                        update.addToGot()
                        global testList 
                        if 'Tryes' in gotItemArray:
                            if 'Tryes' in neededItems:
                                testList.append('Tryes')
                        if neededItems == []:
                            print("Game Won")
                            SampleApp.GameWon()
                        else:
                            pass
            elif 'Tryes' in gotItems:
                print("Can't buy more than one of the aame upgrade")
                sameUpgrade = messagebox.showinfo('', "Can't buy more than one of the aame upgrade")

    def pressA2():

            cost = shopDict['ShopA']['Suspension']
                
            if  totalMoney >= int(cost) and 'Suspension' not in gotItems:
                        gotItems['Suspension'] = cost
                        print (gotItems)
                        global totalMoney
                        global moneySpent
                        totalMoney = totalMoney - int(cost)
                        moneySpent = moneySpent + int(cost)
                        print(totalMoney)
                        print(moneySpent)
                        if 'Suspension' in neededItems:
                            neededItems.remove('Suspension')
                        gotItemArray.append("Suspension")
                        print("1: " + str(gotItemArray))
                        print("2: " + str(neededItems))
                        gameActions.bubble(gotItemArray)
                        global totalGot
                        totalGot = totalGot + 1
                        update.addToGot()
                        global testList 
                        if 'Suspension' in gotItemArray:
                            if 'Suspension' in neededItems:
                                testList.append('Suspension')
                        if neededItems == []:
                            print("Game Won")
                            SampleApp.GameWon()
                        else:
                            pass
            elif 'Suspension' in gotItems:
                print("Can't buy more than one of the aame upgrade")
                sameUpgrade = messagebox.showinfo('', "Can't buy more than one of the aame upgrade")


    def pressA3():

            cost = shopDict['ShopA']['MOT']
                
            if  totalMoney >= int(cost) and 'MOT' not in gotItems:
                        gotItems['MOT'] = cost
                        print (gotItems)
                        global totalMoney
                        global moneySpent
                        totalMoney = totalMoney - int(cost)
                        moneySpent = moneySpent + int(cost)
                        print(totalMoney)
                        print(moneySpent)
                        if 'MOT' in neededItems:
                            neededItems.remove('MOT')
                        gotItemArray.append("MOT")
                        print("1: " + str(gotItemArray))
                        print("2: " + str(neededItems))
                        gameActions.bubble(gotItemArray)
                        global totalGot
                        totalGot = totalGot + 1
                        update.addToGot()
                        global testList 
                        if 'MOT' in gotItemArray:
                            if 'MOT' in neededItems:
                                testList.append('MOT')
                        if neededItems == []:
                            print("Game Won")
                            SampleApp.GameWon()
                        else:
                            pass
            elif 'MOT' in gotItems:
                print("Can't buy more than one of the aame upgrade")
                sameUpgrade = messagebox.showinfo('', "Can't buy more than one of the aame upgrade")

                    
    def pressB1():

            cost = shopDict['ShopB']['Tryes']
                
            if  totalMoney >= int(cost) and 'Tryes' not in gotItems:
                        gotItems['Tryes'] = cost
                        print (gotItems)
                        global totalMoney
                        global moneySpent
                        totalMoney = totalMoney - int(cost)
                        moneySpent = moneySpent + int(cost)
                        print(totalMoney)
                        print(moneySpent)
                        if 'Tryes' in neededItems:
                            neededItems.remove('Tryes')
                        gotItemArray.append("Tryes")
                        print("1: " + str(gotItemArray))
                        print("2: " + str(neededItems))
                        gameActions.bubble(gotItemArray)
                        global totalGot
                        totalGot = totalGot + 1
                        update.addToGot()
                        global testList 
                        if 'Tryes' in gotItemArray:
                            if 'Tryes' in neededItems:
                                testList.append('Tryes')
                        if neededItems == []:
                            print("Game Won")
                            SampleApp.GameWon()  
                        else:
                            pass
            elif 'Tryes' in gotItems:
                print("Can't buy more than one of the aame upgrade")
                sameUpgrade = messagebox.showinfo('', "Can't buy more than one of the aame upgrade")

                    
    def pressB2():

            cost = shopDict['ShopB']['Windows']
                
            if  totalMoney >= int(cost) and 'Windows' not in gotItems:
                        gotItems['Windows'] = cost
                        print (gotItems)
                        global totalMoney
                        global moneySpent
                        totalMoney = totalMoney - int(cost)
                        moneySpent = moneySpent + int(cost)
                        print(totalMoney)
                        print(moneySpent)
                        if 'Windows' in neededItems:
                            neededItems.remove('Windows')
                        gotItemArray.append("Windows")
                        print("1: " + str(gotItemArray))
                        print("2: " + str(neededItems))
                        gameActions.bubble(gotItemArray)
                        global totalGot
                        totalGot = totalGot + 1
                        update.addToGot()
                        global testList
                        if 'Windows' in gotItemArray:
                            if 'Windows' in neededItems:
                                testList.append('Windows')
                        if neededItems == []:
                            print("Game Won")
                            SampleApp.GameWon() 
                        else:
                            pass
            elif 'Windows' in gotItems:
                print("Can't buy more than one of the aame upgrade")
                sameUpgrade = messagebox.showinfo('', "Can't buy more than one of the aame upgrade")

                    
    def pressB3():

            cost = shopDict['ShopB']['Spoiler']
                
            if  totalMoney >= int(cost) and 'Spoiler' not in gotItems:
                        gotItems['Spoiler'] = cost
                        print (gotItems)
                        global totalMoney
                        global moneySpent
                        totalMoney = totalMoney - int(cost)
                        moneySpent = moneySpent + int(cost)
                        print(totalMoney)
                        print(moneySpent)
                        if 'Spoiler' in neededItems:
                            neededItems.remove('Spoiler')
                        gotItemArray.append("Spoiler")
                        print("1: " + str(gotItemArray))
                        print("2: " + str(neededItems))
                        gameActions.bubble(gotItemArray)
                        global totalGot
                        totalGot = totalGot + 1
                        update.addToGot()
                        global testList
                        if 'Spoiler' in gotItemArray:
                            if 'Spoiler' in neededItems:
                                testList.append('Spoiler')
                        if neededItems == []:
                            print("Game Won")
                            SampleApp.GameWon()  
                        else:
                            pass
            elif 'Spoiler' in gotItems:
                print("Can't buy more than one of the aame upgrade")
                sameUpgrade = messagebox.showinfo('', "Can't buy more than one of the aame upgrade")


    def pressS1():

            cost = shopDict['ShopS']['Engine']
                
            if  totalMoney >= int(cost) and 'Engine' not in gotItems:
                        gotItems['Engine'] = cost
                        print (gotItems)
                        global totalMoney
                        global moneySpent
                        totalMoney = totalMoney - int(cost)
                        moneySpent = moneySpent + int(cost)
                        print(totalMoney)
                        print(moneySpent)
                        if 'Engine' in neededItems:
                            neededItems.remove('Engine')
                        gotItemArray.append("Engine")
                        print("1: " + str(gotItemArray))
                        print("2: " + str(neededItems))
                        gameActions.bubble(gotItemArray)
                        global totalGot
                        totalGot = totalGot + 1
                        update.addToGot()
                        global testList 
                        if 'Engine' in gotItemArray:
                            if 'Engine' in neededItems:
                                testList.append('Engine')
                        if neededItems == []:
                            print("Game Won")
                            SampleApp.GameWon()
                        else:
                            pass
            elif 'Engine' in gotItems:
                print("Can't buy more than one of the aame upgrade")
                sameUpgrade = messagebox.showinfo('', "Can't buy more than one of the aame upgrade")

    def pressS2():

            cost = shopDict['ShopS']['Exhaughst']
                
            if  totalMoney >= int(cost) and 'Exhaughst' not in gotItems:
                        gotItems['Exhaughst'] = cost
                        print (gotItems)
                        global totalMoney
                        global moneySpent
                        totalMoney = totalMoney - int(cost)
                        moneySpent = moneySpent + int(cost)
                        print(totalMoney)
                        print(moneySpent)
                        if 'Exhaughst' in neededItems:
                            neededItems.remove('Exhaughst')
                        gotItemArray.append("Exhaughst")
                        print("1: " + str(gotItemArray))
                        print("2: " + str(neededItems))
                        gameActions.bubble(gotItemArray)
                        global totalGot
                        totalGot = totalGot + 1
                        update.addToGot()
                        global testList 
                        if 'Exhaughst' in gotItemArray:
                            if 'Exhaughst' in neededItems:
                                testList.append('Exhaughst')
                        if neededItems == []:
                            print("Game Won")
                            SampleApp.GameWon()
                        else:
                            pass
            elif 'Exhaughst' in gotItems:
                print("Can't buy more than one of the aame upgrade")
                sameUpgrade = messagebox.showinfo('', "Can't buy more than one of the aame upgrade")

    def pressS3():

            cost = shopDict['ShopS']['Pink Fluffy Dice']
                
            if  totalMoney >= int(cost) and 'Pink Fluffy Dice' not in gotItems:
                        gotItems['Pink Fluffy Dice'] = cost
                        print (gotItems)
                        global totalMoney
                        global moneySpent
                        totalMoney = totalMoney - int(cost)
                        moneySpent = moneySpent + int(cost)
                        print(totalMoney)
                        print(moneySpent)
                        if 'Pink Fluffy Dice' in neededItems:
                            neededItems.remove('Pink Fluffy Dice')
                        gotItemArray.append("Pink Fluffy Dice")
                        print("1: " + str(gotItemArray))
                        print("2: " + str(neededItems))
                        gameActions.bubble(gotItemArray)
                        global totalGot
                        totalGot = totalGot + 1
                        update.addToGot()
                        global testList 
                        if 'Pink Fluffy Dice' in gotItemArray:
                            if 'Pink Fluffy Dice' in neededItems:
                                testList.append('Pink Fluffy Dice')
                        if neededItems == []:
                            print("Game Won")
                            SampleApp.GameWon()
                        else:
                            pass
            elif 'Pink Fluffy Dice' in gotItems:
                print("Can't buy more than one of the aame upgrade")
                sameUpgrade = messagebox.showinfo('', "Can't buy more than one of the aame upgrade")

    def pressT1():

            cost = shopDict['ShopT']['Brakes']
                
            if  totalMoney >= int(cost) and 'Brakes' not in gotItems:
                        gotItems['Brakes'] = cost
                        print (gotItems)
                        global totalMoney
                        global moneySpent
                        totalMoney = totalMoney - int(cost)
                        moneySpent = moneySpent + int(cost)
                        print(totalMoney)
                        print(moneySpent)
                        if 'Brakes' in neededItems:
                            neededItems.remove('Brakes')
                        gotItemArray.append("Brakes")
                        print("1: " + str(gotItemArray))
                        print("2: " + str(neededItems))
                        gameActions.bubble(gotItemArray)
                        global totalGot
                        totalGot = totalGot + 1
                        update.addToGot()
                        global testList 
                        if 'Brakes' in gotItemArray:
                                if 'Brakes' in neededItems:
                                        testList.append('Brakes')
                        if neededItems == []:
                            print("Game Won")
                            SampleApp.GameWon()
                        else:
                            pass
            elif 'Brakes' in gotItems:
                print("Can't buy more than one of the aame upgrade")
                sameUpgrade = messagebox.showinfo('', "Can't buy more than one of the aame upgrade")


    def pressT2():

            cost = shopDict['ShopT']['Paint Job']
                
            if  totalMoney >= int(cost) and 'Paint Job' not in gotItems:
                        gotItems['Paint Job'] = cost
                        print (gotItems)
                        global totalMoney
                        global moneySpent
                        totalMoney = totalMoney - int(cost)
                        moneySpent = moneySpent + int(cost)
                        print(totalMoney)
                        print(moneySpent)
                        if 'Paint Job' in neededItems:
                            neededItems.remove('Paint Job')
                        gotItemArray.append("Paint Job")
                        print("1: " + str(gotItemArray))
                        print("2: " + str(neededItems))
                        gameActions.bubble(gotItemArray)
                        global totalGot
                        totalGot = totalGot + 1
                        update.addToGot()
                        global testList 
                        if 'Paint Job' in gotItemArray:
                            if 'Paint Job' in neededItems:
                                testList.append('Paint Job')
                        if neededItems == []:
                            print("Game Won")
                            SampleApp.GameWon()
                        else:
                                pass
            elif 'Paint Job' in gotItems:
                print("Can't buy more than one of the aame upgrade")
                sameUpgrade = messagebox.showinfo('', "Can't buy more than one of the aame upgrade")

    def pressT3():

            cost = shopDict['ShopT']['Seats']
                
            if  totalMoney >= int(cost) and 'Seats' not in gotItems:
                        gotItems['Seats'] = cost
                        print (gotItems)
                        global totalMoney
                        global moneySpent
                        totalMoney = totalMoney - int(cost)
                        moneySpent = moneySpent + int(cost)
                        print(totalMoney)
                        print(moneySpent)
                        if 'Seats' in neededItems:
                            neededItems.remove('Seats')
                        gotItemArray.append("Seats")
                        print("1: " + str(gotItemArray))
                        print("2: " + str(neededItems))
                        gameActions.bubble(gotItemArray)
                        global totalGot
                        totalGot = totalGot + 1
                        update.addToGot()
                        global testList 
                        if 'Seats' in gotItemArray:
                            if 'Seats' in neededItems:
                                testList.append('Seats')
                        if neededItems == []:
                            print("Game Won")
                            SampleApp.GameWon()
                        else:
                            pass
            elif 'Seats' in gotItems:
                print("Can't buy more than one of the aame upgrade")
                sameUpgrade = messagebox.showinfo('', "Can't buy more than one of the aame upgrade")
    
    def close_windowcurrentPage(): 
            shop.withdraw()

    def gameDoneCheck():
        if testList == neededItems:
            print("Game Won")
            SampleApp.GameWon() 
  

class SampleApp(tk.Tk ,gameActions):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        super(gameActions, self).__init__()
        

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)


        self.frames = {}
        for F in (StartPage, GamePage, GameChose, ShopPA, ShopPB, ShopPC, ShopPD, ShopPS, ShopPT):
            frame = F(container, self)
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

            self.show_frame(StartPage)


    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def enterShopQ(self, shopLetter):
        enterQuest = messagebox.askquestion('','Enter the store?')

        if enterQuest == "yes":
                if shopLetter == "a":
                        app.show_frame(ShopPA)
                if shopLetter == "b":
                        app.show_frame(ShopPB)
                if shopLetter == "c":
                        app.show_frame(ShopPC)
                if shopLetter == "d":
                        app.show_frame(ShopPD)
                if shopLetter == 's':
                        app.show_frame(ShopPS)
                if shopLetter == "t":
                        app.show_frame(ShopPT)   

    def restartGame():
        reStart = messagebox.askquestion('','Game Over: No Fuel Left. Do you want to retry?')
        if reStart == "yes":
            gameActions.neededReset()
            gameActions.loopDictCheck()
            app.show_frame(GamePage)
        if reStart == "No":
            app.show_frame(StartPage)
    def GameWon():
        global finalScore
        finalScore = int(totalMoney * (10/currentFuel))
        if COMused == True:
            lines = ['You Win!', 'Money Left: ' + str(totalMoney) + '      COM Left: ' + str(COMmoney)  , 'Fuel used: ' + str(currentFuel) +  '      COM used: ' + str(COMFuel) , 'Final Score: ' + str(finalScore) + '      COM Socre: ' + str(COMScore)]
            goStart = messagebox.showinfo('', "\n".join(lines))
        else:
            lines = ['You Win!', 'Money Left: ' + str(totalMoney), 'Fuel used: ' + str(currentFuel), 'Final Score: ' + str(finalScore)]
            goStart = messagebox.showinfo('', "\n".join(lines))
        if goStart == "ok":
            gameActions.neededReset()
            app.show_frame(StartPage)
            update.gameWonDeltLists()
        

class StartPage(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        
        global gameMade
        gameMade = True

        
        toGame = tk.Button(self, text="Start Game",
                            command=lambda: controller.show_frame(GameChose))
        '''gameActions.loopDictCheck() or'''
        toGame.pack()
               
        '''command=lambda: gameActions.loopDictCheck() or controller.show_frame(GamePage))'''

class GameChose(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)


        
        UserGame = tk.Button(self, text="User Only",
                            command=lambda:  gameActions.MakeUser() or  controller.show_frame(GamePage))
        UserGame.pack()

        

        COMgameE = tk.Button(self, text="Vs Easy COM",
                            command=lambda: Computer.startGame("Easy"))
        COMgameE.pack()

        COMgameM = tk.Button(self, text="Vs Med COM",
                            command=lambda: Computer.startGame("Med"))
        COMgameM.pack()

        

        
class GamePage(tk.Frame, gameActions):


        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            super(gameActions, self).__init__()
            
            change3 = tk.Button(self, text="Quit",
                                command=lambda: gameActions.neededReset() or controller.show_frame(StartPage))
      
            change3.pack()




            canvas1 = tk.Canvas(self, height=300, width=300, bg="white")
            canvas1.create_line(100,105,250,255)
            canvas1.create_line(100,105,30,15)
            canvas1.create_line(100,105,40,255)
            canvas1.create_line(40,255,30,15)
            canvas1.create_line(250,15,30,15)
            canvas1.create_line(40,255,250,255)
            canvas1.create_line(250,15,250,255)
            canvas1.create_line(250,15,175,130)
            canvas1.create_line(100,105,175,130)
            canvas_id = canvas1.create_text(140, 20, anchor="nw")
            canvas1.itemconfig(canvas_id, text="3")
            canvas_id2 = canvas1.create_text(137, 120, anchor="nw")
            canvas1.itemconfig(canvas_id2, text="3")
            canvas_id3 = canvas1.create_text(212, 72, anchor="nw")
            canvas1.itemconfig(canvas_id3, text="5")
            canvas_id4 = canvas1.create_text(235, 135, anchor="nw")
            canvas1.itemconfig(canvas_id4, text="7")
            canvas_id5 = canvas1.create_text(145, 240, anchor="nw")
            canvas1.itemconfig(canvas_id5, text="7")
            canvas_id6 = canvas1.create_text(45, 135, anchor="nw")
            canvas1.itemconfig(canvas_id6, text="5")
            canvas_id5 = canvas1.create_text(70, 180, anchor="nw")
            canvas1.itemconfig(canvas_id5, text="3")
            canvas_id6 = canvas1.create_text(60, 60, anchor="nw")
            canvas1.itemconfig(canvas_id6, text="2")
            canvas_id7 = canvas1.create_text(175, 180, anchor="nw")
            canvas1.itemconfig(canvas_id7, text="3")
            
            ball = canvas1.create_oval(120, 130, 80, 90, fill ="red", outline="black", width=1)
            canvas1.tag_raise(ball)

            
            canvas1.pack()

            print(canvas1.coords(ball))

            nodeA = tk.Button(self, text="a",
                              command=lambda: app.enterShopQ("a") or dijkstraA(graph, 'a', currentNode))
            nodeA_window = canvas1.create_window(100, 100, anchor=N, window=nodeA, tags="NodeA")
            #nodeA.pack(side=LEFT)
            nodeB = tk.Button(self, text="b",
                              command=lambda: app.enterShopQ("b") or dijkstraB(graph, 'b', currentNode) )
            nodeB_window = canvas1.create_window(30, 10, anchor=N, window=nodeB)
            #nodeB.pack(side=LEFT)
            nodeC = tk.Button(self, text="c",
                              command=lambda: app.enterShopQ("c") or dijkstraC(graph, 'c', currentNode) )
            nodeC_window = canvas1.create_window(40, 250, anchor=N, window=nodeC)
            #nodeC.pack(side=LEFT)
            nodeD= tk.Button(self, text="d",
                             command=lambda: app.enterShopQ("d") or dijkstraD(graph, 'd', currentNode) )
            nodeD_window = canvas1.create_window(250, 10, anchor=N, window=nodeD)
            #nodeD.pack(side=LEFT)
            nodeT = tk.Button(self, text="t",
                              command=lambda: app.enterShopQ("t") or dijkstraT(graph, 't', currentNode) )
            nodeT_window = canvas1.create_window(175, 125, anchor=N, window=nodeT)
            #nodeT.pack(side=LEFT)

            nodeS = tk.Button(self, text="s",
                              command=lambda: app.enterShopQ("s") or dijkstraS(graph, 's', currentNode))
            nodeS_window = canvas1.create_window(250, 250, anchor=N, window=nodeS)
           # nodeS.pack(side=LEFT)

            checkItem = tk.Button(self, text="Cheapest shop",
                              command=lambda: update.whereToGet())
            checkItem.pack()

            nearestShop = tk.Button(self, text="Closest shop",
                              command=lambda: update.closestShop())
            nearestShop.pack()
           

            #gameActions.loopDictCheck()
            #lbNeed = tk.Listbox()
            #lbGot = tk.Listbox()
            #lbGot.insert(1, "Items Bought")
            #lbNeed.insert(1, "Items Needed")

class update(GamePage):
                    def __init__(self):
                            auper(GamePage).__init__()
                    def updater(deleteList):
        
                            global loopAdd
                            global currentFuel
                            currentFuel = 0
                            if deleteList == False:
                                    lbNeed = tk.Listbox()
                                    lbGot = tk.Listbox()
                                    lbGot.insert(1, "Items Bought:")
                                    lbNeed.insert(1, "Items Needed:")
                                    money = tk.Label(text= "Money: " + str(totalMoney))
                                    fuel = tk.Label(text= "Fuel Used: " + str(currentFuel))
                                    money.pack()
                                    fuel.pack()
                                    
                                   
                                    while loopAdd < randomInt:
                                            #app.canvas1.itemconfig(nodeS_window, bg = "yellow") 
                                            
                                            lbNeed.insert(loopAdd + 1, str(neededItems[loopAdd]))
                                            loopAdd = loopAdd + 1
                                            lbNeed.pack(side = LEFT)
                                            lbGot.pack(side= RIGHT)
                                       
                                    
                            if deleteList == True:
                                        global lbNeed
                                        global money
                                        global fuel
                                        lbNeed.delete(0, randomInt )
                                        lbNeed.destroy()
                                        global lbGot
                                        lbGot.destroy()
                                        money.destroy()
                                        fuel.destroy()
                            loopAdd = 0
                            loopGot = 0
                            #app.after(1000, update.updater)

                    def addToGot():
                            global lbNeed
                            global money
                            global fuel
                            lbNeed.delete(1,END)
                            global randomInt
                            money.destroy()
                            fuel.destroy()
                            money = tk.Label(text= "Money: " + str(totalMoney))
                            fuel = tk.Label(text= "Fuel Used: " + str(currentFuel))
                            money.pack()
                            fuel.pack()
                            
                            randomInt = randomInt - 1
                            global lbGot
                            global totalGot
                            global loopGot
                            lbGot.delete(1,END)
                            while loopGot < totalGot:
                                    lbGot.insert(loopGot + 1, str(gotItemArray[loopGot]))
                                    loopGot = loopGot+ 1
                                    lbNeed.pack(side = LEFT)
                                    lbGot.pack(side= RIGHT)
                            global loopAdd
                            while loopAdd < randomInt:
                                            #app.canvas1.itemconfig(nodeS_window, bg = "yellow") 
                                            
                                            lbNeed.insert(loopAdd, str(neededItems[loopAdd]))
                                            loopAdd = loopAdd + 1
                                            lbNeed.pack(side = LEFT)
                                            lbGot.pack(side= RIGHT)
                                            
                            
                            #global lbGot
                            #global totalGot
                           # global loopGot

                            loopAdd = 0
                            loopGot = 0
                            
                            #update.updater()
                            
                    def gameWonDeltLists():
                              
                        global lbNeed
                        lbNeed.delete(0, randomInt )
                        lbNeed.destroy()
                        global lbGot
                        lbGot.destroy()


                    def whereToGet():
                        global lbNeed
                        searchItem = lbNeed.get(ACTIVE)
                        print(searchItem)
                        gameActions.searchDict(searchItem)
                        
                    def closestShop():
                        global lbNeed
                        searchItem = lbNeed.get(ACTIVE)
                        print(searchItem)
                        gameActions.nearestShop(searchItem)
                        

                    def ballMoveTo(currentNodeMove, nextNodeMove, NodeList):
                        global ballLoop
                        print("here")
                        while ballLoop < NodeList:
                            print("There")
                            if currentNodeMove == 'a':
                                if nextNodeMove == 's':
                                    for i in range(250, 250):
                                        time.sleep(0.025)
                                        canvas1.move(ball, 15, 15)
                                        canvas1.update()
                                        print("I am here 1")
                                if nextNodeMove == 'b':
                                    for i in range(30, 10):
                                        time.sleep(0.025)
                                        canvas1.move(ball, -7, -9)
                                        canvas1.update()
                                        print("I am here 2")
                                if nextNodeMove == 'c':
                                    for i in range(40, 250):
                                        time.sleep(0.025)
                                        canvas1.move(ball, -6, 15)
                                        canvas1.update()
                                        print("I am here 3")
                                if nextNodeMove == 't':
                                    for i in range(175, 125):
                                        time.sleep(0.025)
                                        canvas1.move(ball, 7.5, 2.5)
                                        canvas1.update()
                                        print("I am here 4")
                            if currentNodeMove == 'b':
                                if nextNodeMove == 'a':
                                    pass
                                if nextNodeMove == 'c':
                                    pass
                                if nextNodeMove == 'd':
                                    pass
                            if currentNodeMove == 'c':
                                if nextNodeMove == 'a':
                                    pass
                                if nextNodeMove == 'b':
                                    pass
                                if nextNodeMove == 's':
                                    pass
                            if currentNodeMove == 'd':
                                if nextNodeMove == 'b':
                                    pass
                                if nextNodeMove == 't':
                                    pass
                                if nextNodeMove == 's':
                                    pass
                            if currentNodeMove == 't':
                                if nextNodeMove == 'a':
                                    pass
                                if nextNodeMove == 'd':
                                    pass
                            if currentNodeMove == 's':
                                if nextNodeMove == 'a':
                                    pass
                                if nextNodeMove == 'c':
                                    pass
                                if nextNodeMove == 'd':
                                    pass
                            ballLoop = ballLoop + 1

                        
                        





class ShopPA(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        #text1 = str(ShopA.items[0])
        #text2 = str(ShopA.items[1])
       
        ShopA1 = tk.Button(self, text = "Tyres" ,
                        command = lambda: gameActions.pressA1())
        ShopA1.pack()

        ShopA2 = tk.Button(self, text= "Suspension",
                           command = lambda: gameActions.pressA2())
        ShopA2.pack()

        ShopA3 = tk.Button(self, text= "MOT",
                           command = lambda: gameActions.pressA3())
        ShopA3.pack()

        ShopAClose = tk.Button(self, text = "Leave Shop",
                               command = lambda: controller.show_frame(GamePage))
        ShopAClose.pack()

class ShopPB(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        #text1 = str(ShopA.items[0])
        #text2 = str(ShopA.items[1])

        ShopB1 = tk.Button(self, text = "Tyres",
                           command = lambda: gameActions.pressB1())
        ShopB1.pack()

        ShopB2 = tk.Button(self, text= "Windows",
                           command = lambda: gameActions.pressB2())
        ShopB2.pack()

        ShopB3 = tk.Button(self, text= "Spoilers",
                           command = lambda: gameActions.pressB3() or gameActions.gameDoneCheck())
        ShopB3.pack()

        ShopBClose = tk.Button(self, text = "Leave Shop",
                               command = lambda: controller.show_frame(GamePage))
                               
        ShopBClose.pack()

class ShopPC(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        #text1 = str(ShopA.items[0])
        #text2 = str(ShopA.items[1])
       
        ShopC1 = tk.Button(self, text = "Windows",
                           command = lambda: gameActions.pressC1())
        ShopC1.pack()

        ShopC2 = tk.Button(self, text= "Suspension",
                           command = lambda: gameActions.pressC2())
        ShopC2.pack()

        ShopC3 = tk.Button(self, text= "Gear Stick",
                           command = lambda: gameActions.pressC3())
        ShopC3.pack()

        ShopCClose = tk.Button(self, text = "Leave Shop",
                               command = lambda: controller.show_frame(GamePage))
        ShopCClose.pack()

class ShopPD(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        #text1 = str(ShopA.items[0])
        #text2 = str(ShopA.items[1])
       
        ShopD1 = tk.Button(self, text = "Suspension",
                           command = lambda: gameActions.pressD1())
        ShopD1.pack()

        ShopD2 = tk.Button(self, text= "Spoiler",
                           command = lambda: gameActions.pressD2())
        ShopD2.pack()

        ShopDClose = tk.Button(self, text = "Leave Shop",
                               command = lambda: controller.show_frame(GamePage))
        ShopDClose.pack()

class ShopPS(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        #text1 = str(ShopA.items[0])
        #text2 = str(ShopA.items[1])
       
        ShopS1 = tk.Button(self, text = "Engine" ,
                        command = lambda: gameActions.pressS1())
        ShopS1.pack()

        ShopS2 = tk.Button(self, text= "Exhaughst",
                           command = lambda: gameActions.pressS2())
        ShopS2.pack()

        ShopS3 = tk.Button(self, text= "Pink Fluffy Dice",
                           command = lambda: gameActions.pressS3())
        ShopS3.pack()

        ShopSClose = tk.Button(self, text = "Leave Shop",
                               command = lambda: controller.show_frame(GamePage))
        ShopSClose.pack()

class ShopPT(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        #text1 = str(ShopA.items[0])
        #text2 = str(ShopA.items[1])
       
        ShopT1 = tk.Button(self, text = "Brakes" ,
                        command = lambda: gameActions.pressT1())
        ShopT1.pack()

        ShopT2 = tk.Button(self, text= "Paint Job",
                           command = lambda: gameActions.pressT2())
        ShopT2.pack()

        ShopT3 = tk.Button(self, text= "Seats",
                           command = lambda: gameActions.pressT3())
        ShopT3.pack()

        ShopTClose = tk.Button(self, text = "Leave Shop",
                               command = lambda: controller.show_frame(GamePage))
        ShopTClose.pack()

def dijkstraC(graph, curNode, toNode, visitedNodes=[], travelDistances={}, predecessors={}):
 
                if curNode not in graph:
                    raise TypeError('the root of the shortest path tree cannot be found in the graph')
                if toNode not in graph:
                    raise TypeError('the target of the shortest path cannot be found in the graph')    
                if curNode == toNode:
                    path=[]
                    pred=toNode
                    while pred != None:
                        path.append(pred)
                        pred=predecessors.get(pred,None)
                    print('shortest path: '+str(path)+" cost="+str(travelDistances[toNode]))
                    global lastFuelUsage
                    lastFuelUsage = int(travelDistances[toNode])
                    gameActions.FuelLeft(lastFuelUsage)
                    
                    if searc == False:
                        global currentNode
                        currentNode = 'c'
                        global COMCurrentNode
                        COMCurrentNode = 'c'
                    else:
                        path=[]
                    
                else : 
                    if not visitedNodes: 
                        travelDistances[curNode]=0
                    for nextToNode in graph[curNode] :
                        if nextToNode not in visitedNodes:
                            new_distance = travelDistances[curNode] + graph[curNode][nextToNode]
                            if new_distance < travelDistances.get(nextToNode,float('inf')):
                                travelDistances[nextToNode] = new_distance
                                predecessors[nextToNode] = curNode
                    visitedNodes.append(curNode)
                    unvisited={}
                    for k in graph:
                        if k not in visitedNodes:
                            unvisited[k] = travelDistances.get(k,float('inf'))        
                    x=min(unvisited, key=unvisited.get)
                    dijkstraC(graph,x,toNode,visitedNodes,travelDistances,predecessors)
if gameMade == True:
                dijkstraC(graph, 'c' , currentNode)

def dijkstraS(graph, curNode, toNode, visitedNodes=[], travelDistances={}, predecessors={}):   
                if curNode not in graph:
                    raise TypeError('the root of the shortest path tree cannot be found in the graph')
                if toNode not in graph:
                    raise TypeError('the target of the shortest path cannot be found in the graph')    
                if curNode == toNode:
                    path=[]
                    pred=toNode
                    while pred != None:
                        path.append(pred)
                        pred=predecessors.get(pred,None)
                    print('shortest path: '+str(path)+" cost="+str(travelDistances[toNode]))
                    global lastFuelUsage
                    lastFuelUsage = int(travelDistances[toNode])
                    gameActions.FuelLeft(lastFuelUsage)
                    if searc == False:
                        global currentNode
                        currentNode = 's'
                        global COMCurrentNode
                        COMCurrentNode = 's'
                    else:
                        path=[]
                else : 
                    if not visitedNodes: 
                        travelDistances[curNode]=0
                    for nextToNode in graph[curNode] :
                        if nextToNode not in visitedNodes:
                            new_distance = travelDistances[curNode] + graph[curNode][nextToNode]
                            if new_distance < travelDistances.get(nextToNode,float('inf')):
                                travelDistances[nextToNode] = new_distance
                                predecessors[nextToNode] = curNode
                    visitedNodes.append(curNode)
                    unvisited={}
                    for k in graph:
                        if k not in visitedNodes:
                            unvisited[k] = travelDistances.get(k,float('inf'))        
                    x=min(unvisited, key=unvisited.get)
                    dijkstraS(graph,x,toNode,visitedNodes,travelDistances,predecessors)
if gameMade == True:
            dijkstraS(graph, 's' , currentNode)

def dijkstraD(graph, curNode, toNode, visitedNodes=[], travelDistances={}, predecessors={}):
    
                if curNode not in graph:
                    raise TypeError('the root of the shortest path tree cannot be found in the graph')
                if toNode not in graph:
                    raise TypeError('the target of the shortest path cannot be found in the graph')    
                if curNode == toNode:
                    path=[]
                    pred=toNode
                    while pred != None:
                        path.append(pred)
                        pred=predecessors.get(pred,None)
                    print('shortest path: '+str(path)+" cost="+str(travelDistances[toNode]))
                    global lastFuelUsage
                    lastFuelUsage = int(travelDistances[toNode])
                    gameActions.FuelLeft(lastFuelUsage)
                    if searc == False:
                        global currentNode
                        currentNode = 'd'
                        global COMCurrentNode
                        COMCurrentNode = 'd'
                    else:
                        path=[]
                else : 
                    if not visitedNodes: 
                        travelDistances[curNode]=0
                    for nextToNode in graph[curNode] :
                        if nextToNode not in visitedNodes:
                            new_distance = travelDistances[curNode] + graph[curNode][nextToNode]
                            if new_distance < travelDistances.get(nextToNode,float('inf')):
                                travelDistances[nextToNode] = new_distance
                                predecessors[nextToNode] = curNode
                    visitedNodes.append(curNode)
                    unvisited={}
                    for k in graph:
                        if k not in visitedNodes:
                            unvisited[k] = travelDistances.get(k,float('inf'))        
                    x=min(unvisited, key=unvisited.get)
                    dijkstraD(graph,x,toNode,visitedNodes,travelDistances,predecessors)
if gameMade == True:
            dijkstraD(graph, 'd' , currentNode)

def dijkstraA(graph, curNode, toNode, visitedNodes=[], travelDistances={}, predecessors={}):
        
                if curNode not in graph:
                    raise TypeError('the root of the shortest path tree cannot be found in the graph')
                if toNode not in graph:
                    raise TypeError('the target of the shortest path cannot be found in the graph')    
                if curNode == toNode:
                    path=[]
                    pred=toNode
                    while pred != None:
                        path.append(pred)
                        pred=predecessors.get(pred,None)
                    print('shortest path: '+str(path)+" cost="+str(travelDistances[toNode]))
                    global lastFuelUsage
                    lastFuelUsage = int(travelDistances[toNode])
                    gameActions.FuelLeft(lastFuelUsage)
                    if searc == False:
                        global currentNode
                        currentNode = 'a'
                        global COMCurrentNode
                        COMCurrentNode = 'a'
                    else:
                        path=[]
                    
                else : 
                    if not visitedNodes: 
                        travelDistances[curNode]=0
                    for nextToNode in graph[curNode] :
                        if nextToNode not in visitedNodes:
                            new_distance = travelDistances[curNode] + graph[curNode][nextToNode]
                            if new_distance < travelDistances.get(nextToNode,float('inf')):
                                travelDistances[nextToNode] = new_distance
                                predecessors[nextToNode] = curNode
                    visitedNodes.append(curNode)
                    unvisited={}
                    for k in graph:
                        if k not in visitedNodes:
                            unvisited[k] = travelDistances.get(k,float('inf'))        
                    x=min(unvisited, key=unvisited.get)
                    dijkstraA(graph,x,toNode,visitedNodes,travelDistances,predecessors)
if gameMade == True:
            dijkstraA(graph, 'a' , currentNode)

def dijkstraT(graph, curNode, toNode, visitedNodes=[], travelDistances={}, predecessors={}):
        
                if curNode not in graph:
                    raise TypeError('the root of the shortest path tree cannot be found in the graph')
                if toNode not in graph:
                    raise TypeError('the target of the shortest path cannot be found in the graph')    
                if curNode == toNode:
                    path=[]
                    pred=toNode
                    while pred != None:
                        path.append(pred)
                        pred=predecessors.get(pred,None)
                    print('shortest path: '+str(path)+" cost="+str(travelDistances[toNode]))
                    global lastFuelUsage
                    lastFuelUsage = int(travelDistances[toNode])
                    print(lastFuelUsage)
                    gameActions.FuelLeft(lastFuelUsage)
                    if searc == False:
                        global currentNode
                        currentNode = 't'
                        global COMCurrentNode
                        COMCurrentNode = 't'
                    else:
                        path=[]
                else : 
                    if not visitedNodes: 
                        travelDistances[curNode]=0
                    for nextToNode in graph[curNode] :
                        if nextToNode not in visitedNodes:
                            new_distance = travelDistances[curNode] + graph[curNode][nextToNode]
                            if new_distance < travelDistances.get(nextToNode,float('inf')):
                                travelDistances[nextToNode] = new_distance
                                predecessors[nextToNode] = curNode
                    visitedNodes.append(curNode)
                    unvisited={}
                    for k in graph:
                        if k not in visitedNodes:
                            unvisited[k] = travelDistances.get(k,float('inf'))        
                    x=min(unvisited, key=unvisited.get)
                    dijkstraT(graph,x,toNode,visitedNodes,travelDistances,predecessors)
if gameMade == True:
            dijkstraT(graph, 't' , currentNode)

def dijkstraB(graph, curNode, toNode, visitedNodes=[], travelDistances={}, predecessors={}):
        
                if curNode not in graph:
                    raise TypeError('the root of the shortest path tree cannot be found in the graph')
                if toNode not in graph:
                    raise TypeError('the target of the shortest path cannot be found in the graph')    
                if curNode == toNode:
                    path=[]
                    pred=toNode
                    while pred != None:
                        path.append(pred)
                        pred=predecessors.get(pred,None)
                    print('shortest path: '+str(path)+" cost="+str(travelDistances[toNode]))
                    global lastFuelUsage
                    lastFuelUsage = int(travelDistances[toNode])
                    gameActions.FuelLeft(lastFuelUsage)
                    if searc == False:
                        global currentNode
                        currentNode = 'b'
                        global COMCurrentNode
                        COMCurrentNode = 'b'
                    else:
                        path=[]
                    
                else : 
                    if not visitedNodes: 
                        travelDistances[curNode]=0
                    for nextToNode in graph[curNode] :
                        if nextToNode not in visitedNodes:
                            new_distance = travelDistances[curNode] + graph[curNode][nextToNode]
                            if new_distance < travelDistances.get(nextToNode,float('inf')):
                                travelDistances[nextToNode] = new_distance
                                predecessors[nextToNode] = curNode
                    visitedNodes.append(curNode)
                    unvisited={}
                    for k in graph:
                        if k not in visitedNodes:
                            unvisited[k] = travelDistances.get(k,float('inf'))        
                    x=min(unvisited, key=unvisited.get)
                    dijkstraB(graph,x,toNode,visitedNodes,travelDistances,predecessors)
if gameMade == True:
            djikstraB(graph, 'b' , currentNode)


class Computer(gameActions):
    def __init__(self):
            super(gameActions, self).__init__()

    def startGame(difficulty):
        COMStartPos = random.choice(list(graph.keys()))
        print("COM starts at: " + COMStartPos)
        COMmoneySpent = 0
        COMFuelUssed = 0
        global COMused
        COMused = True

        COMCurrentNode = COMStartPos
        COMItemsGot = []
        COMGameDone = False
        COMatShop = ''
        COMFuelUssed = 0

        if difficulty == "Easy":
            global diff
            diff = difficulty
            gameActions.loopDictCheck()
            while COMGameDone == False:
                COMTarget = random.choice(neededItems)
                while COMTarget in COMItemsGot:
                    COMTarget = random.choice(neededItems)
                    
                gameActions.nearestShop(COMTarget)
                print("COM Found cheapest at " + COMnextNODE)
                COMdone = False
                if COMnextNODE == 'a' and COMdone == False:
                    Computer.dijkstraCOM(graph, 'a', COMCurrentNode)
                    COMdone = True
                    COMatShop = 'ShopA'
                    COMFuelUssed = COMFuelUssed + lastFuelUsage
                    
                if COMnextNODE == 'b'and COMdone == False:
                    COMdone = True
                    COMatShop = 'ShopB'
                    Computer.dijkstraCOM(graph, 'b', COMCurrentNode)
                    COMFuelUssed = COMFuelUssed + lastFuelUsage
                    
                if COMnextNODE == 'c'and COMdone == False:
                    COMdone = True
                    COMatShop = 'ShopC'
                    Computer.dijkstraCOM(graph, 'c', COMCurrentNode)
                    COMFuelUssed = COMFuelUssed + lastFuelUsage
                    
                if COMnextNODE == 'd'and COMdone == False:
                    COMdone = True
                    COMatShop = 'ShopD'
                    Computer.dijkstraCOM(graph, 'd', COMCurrentNode)
                    COMFuelUssed = COMFuelUssed + lastFuelUsage
                    
                if COMnextNODE == 't'and COMdone == False:
                    COMdone = True
                    COMatShop = 'ShopT'
                    Computer.dijkstraCOM(graph, 't', COMCurrentNode)
                    COMFuelUssed = COMFuelUssed + lastFuelUsage
                    
                if COMnextNODE == 's'and COMdone == False:
                    COMdone = True
                    COMatShop = 'ShopS'
                    Computer.dijkstraCOM(graph, 's', COMCurrentNode)
                    COMFuelUssed = COMFuelUssed + lastFuelUsage
                    
                print("COM now at " + str(COMCurrentNode))
                COMItemsGot.append(COMTarget)
                cost = shopDict[COMatShop][COMTarget]
                COMmoneySpent = COMmoneySpent + int(cost)
                print("COM has spent: " + str(COMmoneySpent))
                print("COM has collected: " + str(COMItemsGot))
                print("COM has used " + str(COMFuelUssed) + "fuel")
                gameActions.bubble(COMItemsGot)
                if COMItemsGot == neededItems:
                    print("COM complete!")
                    print("COM spent " + str(COMmoneySpent))
                    print ("COM used " + str(COMFuelUssed))
                    global COMScore
                    global COMFuel
                    global COMmoney
                    COMFuel = COMFuelUssed
                    COMmoney = 6000 - COMmoneySpent
                    
                    COMScore = int((6000 - COMmoneySpent) * (20/COMFuelUssed))
                    lines = ['COM finished!', 'Money Left: ' + str(6000 - COMmoneySpent) , 'Fuel used: ' + str(COMFuelUssed), 'Final Score: ' + str(COMScore)]
                    goStart = messagebox.showinfo('', "\n".join(lines))
                    COMGameDone = True
                    app.show_frame(GamePage)
                    update.updater(False)
                    global user
                    user = "Player"
                    
        if difficulty == "Med":
                global diff
                diff = difficulty
                gameActions.loopDictCheck()
                while COMGameDone == False:
                    COMTarget = random.choice(neededItems)
                    while COMTarget in COMItemsGot:
                        COMTarget = random.choice(neededItems)
                    gameActions.searchDict(COMTarget)
                    print("COM Found cheapest at " + COMnextNODE)
                    COMdone = False
                    if COMnextNODE == 'a' and COMdone == False:
                        Computer.dijkstraCOM(graph, 'a', COMCurrentNode)
                        COMdone = True
                        searchDone = False
                        COMatShop = 'ShopA'
                        if len(COMRoute) > 2:
                            global shopBasket
                            while searchDone == False:
                                
                                    i = 1
                                    checkCOMNode = COMRoute[i]
                                    if COMRoute[i] == 'a':
                                        COMshop = "ShopA"
                                        val = 0
                                        neededItemSearch = False
                                        while neededItemSearch == False:
                                            if neededItems[val] in shopDict[COMshop]:
                                                if neededItems[val] not in shopBasket:
                                                    shopBasket.append(neededItems[val])
                                                    val = val + 1
                                                    searchDone = True
                                                    if val > len(neededItems):
                                                        neededItemSearch = True
                                                    print(shopBasket)
                                    if COMRoute[i] == 'b':
                                        COMshop = "ShopB"
                                        val = 0
                                        neededItemSearch = False
                                        while neededItemSearch == False:
                                            if neededItems[val] in shopDict[COMshop]:
                                                if neededItems[val] not in shopBasket:
                                                    shopBasket.append(neededItems[val])
                                                    val = val + 1
                                                    searchDone = True
                                                    if val > len(neededItems):
                                                        neededItemSearch = True
                                                    print(shopBasket)
                                    if COMRoute[i] == 'c':
                                        COMshop = "ShopC"
                                        val = 0
                                        neededItemSearch = False
                                        while neededItemSearch == False:
                                            if neededItems[val] in shopDict[COMshop]:
                                                if neededItems[val] not in shopBasket:
                                                    shopBasket.append(neededItems[val])
                                                    val = val + 1
                                                    searchDone = True
                                                    if val > len(neededItems):
                                                        neededItemSearch = True
                                                    print(shopBasket)
                                    if COMRoute[i] == 'd':
                                        COMshop = "ShopD"
                                        val = 0
                                        neededItemSearch = False
                                        while neededItemSearch == False:
                                            if neededItems[val] in shopDict[COMshop]:
                                                if neededItems[val] not in shopBasket:
                                                    shopBasket.append(neededItems[val])
                                                    val = val + 1
                                                    searchDone = True
                                                    if val > len(neededItems):
                                                        neededItemSearch = True
                                                    print(shopBasket)
                                    if COMRoute[i] == 't':
                                        COMshop = "ShopT"
                                        val = 0
                                        neededItemSearch = False
                                        while neededItemSearch == False:
                                            if neededItems[val] in shopDict[COMshop]:
                                                if neededItems[val] not in shopBasket:
                                                    shopBasket.append(neededItems[val])
                                                    val = val + 1
                                                    searchDone = True
                                                    if val > len(neededItems):
                                                        neededItemSearch = True
                                                    print(shopBasket)
                                    if COMRoute[i] == 's':
                                        COMshop = "ShopS"
                                        val = 0
                                        neededItemSearch = False
                                        while neededItemSearch == False:
                                            if neededItems[val] in shopDict[COMshop]:
                                                if neededItems[val] not in shopBasket:
                                                    shopBasket.append(neededItems[val])
                                                    val = val + 1
                                                    searchDone = True
                                                    if val > len(neededItems):
                                                        neededItemSearch = True
                                                    print(shopBasket)
                            print(shopBasket)
                            shop = False
                            i = 0
                            if shop == False:
                                    for neededItems[i] in shopBasket:
                                        while neededItems[i] not in COMItemsGot:
                                            COMItemsGot.append(neededItems[i])
                                            i = i + 1
                                            print(COMItemsGot)
                       
                        
                    if COMnextNODE == 'b'and COMdone == False:
                        COMdone = True
                        COMatShop = 'ShopB'
                        searchDone = False
                        Computer.dijkstraCOM(graph, 'b', COMCurrentNode)
                        if len(COMRoute) > 2:
                            global shopBasket
                            while searchDone == False:
                                
                                    i = 0
                                    checkCOMNode = COMRoute[i]
                                    if COMRoute[i] == 'a':
                                        COMshop = "ShopA"
                                        val = 0
                                        neededItemSearch = False
                                        while neededItemSearch == False:
                                            if neededItems[val] in shopDict[COMshop]:
                                                if neededItems[val] not in shopBasket:
                                                    shopBasket.append(neededItems[val])
                                                    val = val + 1
                                                    searchDone = True
                                                    if val > len(neededItems):
                                                        neededItemSearch = True
                                                    print(shopBasket)
                                    if COMRoute[i] == 'b':
                                        COMshop = "ShopB"
                                        val = 0
                                        neededItemSearch = False
                                        while neededItemSearch == False:
                                            if neededItems[val] in shopDict[COMshop]:
                                                if neededItems[val] not in shopBasket:
                                                    shopBasket.append(neededItems[val])
                                                    val = val + 1
                                                    searchDone = True
                                                    if val > len(neededItems):
                                                        neededItemSearch = True
                                                    print(shopBasket)
                                    if COMRoute[i] == 'c':
                                        COMshop = "ShopC"
                                        val = 0
                                        neededItemSearch = False
                                        while neededItemSearch == False:
                                            if neededItems[val] in shopDict[COMshop]:
                                                if neededItems[val] not in shopBasket:
                                                    shopBasket.append(neededItems[val])
                                                    val = val + 1
                                                    searchDone = True
                                                    if val > len(neededItems):
                                                        neededItemSearch = True
                                                    print(shopBasket)
                                    if COMRoute[i] == 'd':
                                        COMshop = "ShopD"
                                        val = 0
                                        neededItemSearch = False
                                        while neededItemSearch == False:
                                            if neededItems[val] in shopDict[COMshop]:
                                                if neededItems[val] not in shopBasket:
                                                    shopBasket.append(neededItems[val])
                                                    val = val + 1
                                                    searchDone = True
                                                    if val > len(neededItems):
                                                        neededItemSearch = True
                                                    print(shopBasket)
                                    if COMRoute[i] == 't':
                                        COMshop = "ShopT"
                                        val = 0
                                        neededItemSearch = False
                                        while neededItemSearch == False:
                                            if neededItems[val] in shopDict[COMshop]:
                                                if neededItems[val] not in shopBasket:
                                                    shopBasket.append(neededItems[val])
                                                    val = val + 1
                                                    searchDone = True
                                                    if val > len(neededItems):
                                                        neededItemSearch = True
                                                    print(shopBasket)
                                    if COMRoute[i] == 's':
                                        COMshop = "ShopS"
                                        val = 0
                                        neededItemSearch = False
                                        while neededItemSearch == False:
                                            if neededItems[val] in shopDict[COMshop]:
                                                if neededItems[val] not in shopBasket:
                                                    shopBasket.append(neededItems[val])
                                                    val = val + 1
                                                    searchDone = True
                                                    if val > len(neededItems):
                                                        neededItemSearch = True
                                                    print(shopBasket)

                        print(shopBasket)
                        shop = False
                        i = 0
                        if shop == False:
                                    for neededItems[i] in shopBasket:
                                        while neededItems[i] not in COMItemsGot:
                                            COMItemsGot.append(neededItems[i])
                                            i = i + 1
                                            print(COMItemsGot)
                        
                        
                    if COMnextNODE == 'c'and COMdone == False:
                        COMdone = True
                        COMatShop = 'ShopC'
                        searchDone = False
                        Computer.dijkstraCOM(graph, 'c', COMCurrentNode)
                        if len(COMRoute) > 2:
                            global shopBasket
                            while searchDone == False:
                                
                                    i = 0
                                    checkCOMNode = COMRoute[i]
                                    if COMRoute[i] == 'a':
                                        COMshop = "ShopA"
                                        val = 0
                                        neededItemSearch = False
                                        while neededItemSearch == False:
                                            if neededItems[val] in shopDict[COMshop]:
                                                if neededItems[val] not in shopBasket:
                                                    shopBasket.append(neededItems[val])
                                                    val = val + 1
                                                    searchDone = True
                                                    if val > len(neededItems):
                                                        neededItemSearch = True
                                                    print(shopBasket)
                                    if COMRoute[i] == 'b':
                                        COMshop == "ShopB"
                                        val = 0
                                        neededItemSearch = False
                                        while neededItemSearch == False:
                                            if neededItems[val] in shopDict[COMshop]:
                                                if neededItems[val] not in shopBasket:
                                                    shopBasket.append(neededItems[val])
                                                    val = val + 1
                                                    searchDone = True
                                                    if val > len(neededItems):
                                                        neededItemSearch = True
                                                    print(shopBasket)
                                    if COMRoute[i] == 'c':
                                        COMshop = "ShopC"
                                        val = 0
                                        neededItemSearch = False
                                        while neededItemSearch == False:
                                            if neededItems[val] in shopDict[COMshop]:
                                                if neededItems[val] not in shopBasket:
                                                    shopBasket.append(neededItems[val])
                                                    val = val + 1
                                                    searchDone = True
                                                    if val > len(neededItems):
                                                        neededItemSearch = True
                                                    print(shopBasket)
                                    if COMRoute[i] == 'd':
                                        COMshop = "ShopD"
                                        val = 0
                                        neededItemSearch = False
                                        while neededItemSearch == False:
                                            if neededItems[val] in shopDict[COMshop]:
                                                if neededItems[val] not in shopBasket:
                                                    shopBasket.append(neededItems[val])
                                                    val = val + 1
                                                    searchDone = True
                                                    if val > len(neededItems):
                                                        neededItemSearch = True
                                                    print(shopBasket)
                                    if COMRoute[i] == 't':
                                        COMshop = "ShopT"
                                        val = 0
                                        neededItemSearch = False
                                        while neededItemSearch == False:
                                            if neededItems[val] in shopDict[COMshop]:
                                                if neededItems[val] not in shopBasket:
                                                    shopBasket.append(neededItems[val])
                                                    val = val + 1
                                                    searchDone = True
                                                    if val > len(neededItems):
                                                        neededItemSearch = True
                                                    print(shopBasket)
                                    if COMRoute[i] == 's':
                                        COMshop = "ShopS"
                                        val = 0
                                        neededItemSearch = False
                                        while neededItemSearch == False:
                                            if neededItems[val] in shopDict[COMshop]:
                                                if neededItems[val] not in shopBasket:
                                                    shopBasket.append(neededItems[val])
                                                    val = val + 1
                                                    searchDone = True
                                                    if val > len(neededItems):
                                                        neededItemSearch = True
                                                    
                                                    print(shopBasket)
                       
                        
                    if COMnextNODE == 'd'and COMdone == False:
                        COMdone = True
                        COMatShop = 'ShopD'
                        searchDone = False
                        Computer.dijkstraCOM(graph, 'd', COMCurrentNode)
                        if len(COMRoute) > 2:
                            global shopBasket
                            while searchDone == False:
                                
                                    i = 0
                                    checkCOMNode = COMRoute[i]
                                    if COMRoute[i] == 'a':
                                        COMshop = "ShopA"
                                        val = 0
                                        neededItemSearch = False
                                        while neededItemSearch == False:
                                            if neededItems[val] in shopDict[COMshop]:
                                                if neededItems[val] not in shopBasket:
                                                    shopBasket.append(neededItems[val])
                                                    val = val + 1
                                                    searchDone = True
                                                    if val > len(neededItems):
                                                        neededItemSearch = True
                                                    print(shopBasket)
                                    if COMRoute[i] == 'b':
                                        COMshop = "ShopB"
                                        val = 0
                                        neededItemSearch = False
                                        while neededItemSearch == False:
                                            if neededItems[val] in shopDict[COMshop]:
                                                if neededItems[val] not in shopBasket:
                                                    shopBasket.append(neededItems[val])
                                                    val = val + 1
                                                    searchDone = True
                                                    if val > len(neededItems):
                                                        neededItemSearch = True
                                                    print(shopBasket)
                                    if COMRoute[i] == 'c':
                                        COMshop = "ShopC"
                                        val = 0
                                        neededItemSearch = False
                                        while neededItemSearch == False:
                                            if neededItems[val] in shopDict[COMshop]:
                                                if neededItems[val] not in shopBasket:
                                                    shopBasket.append(neededItems[val])
                                                    val = val + 1
                                                    searchDone = True
                                                    if val > len(neededItems):
                                                        neededItemSearch = True
                                                    print(shopBasket)
                                    if COMRoute[i] == 'd':
                                        COMshop = "ShopD"
                                        val = 0
                                        neededItemSearch = False
                                        while neededItemSearch == False:
                                            if neededItems[val] in shopDict[COMshop]:
                                                if neededItems[val] not in shopBasket:
                                                    shopBasket.append(neededItems[val])
                                                    val = val + 1
                                                    searchDone = True
                                                    if val > len(neededItems):
                                                        neededItemSearch = True
                                                    print(shopBasket)
                                    if COMRoute[i] == 't':
                                        COMshop = "ShopT"
                                        val = 0
                                        neededItemSearch = False
                                        while neededItemSearch == False:
                                            if neededItems[val] in shopDict[COMshop]:
                                                if neededItems[val] not in shopBasket:
                                                    shopBasket.append(neededItems[val])
                                                    val = val + 1
                                                    searchDone = True
                                                    if val > len(neededItems):
                                                        neededItemSearch = True
                                                    print(shopBasket)
                                    if COMRoute[i] == 's':
                                        COMshop = "ShopS"
                                        val = 0
                                        neededItemSearch = False
                                        while neededItemSearch == False:
                                            if neededItems[val] in shopDict[COMshop]:
                                                if neededItems[val] not in shopBasket:
                                                    shopBasket.append(neededItems[val])
                                                    val = val + 1
                                                    searchDone = True
                                                    if val > len(neededItems):
                                                        neededItemSearch = True
                                                    print(shopBasket)
                        
                        
                    if COMnextNODE == 't'and COMdone == False:
                        COMdone = True
                        COMatShop = 'ShopT'
                        searchDone = False
                        Computer.dijkstraCOM(graph, 't', COMCurrentNode)
                        if len(COMRoute) > 2:
                            global shopBasket
                            while searchDone == False:
                                
                                    i = 0
                                    checkCOMNode = COMRoute[i]
                                    if COMRoute[i] == 'a':
                                        COMshop = "ShopA"
                                        val = 0
                                        neededItemSearch = False
                                        while neededItemSearch == False:
                                            if neededItems[val] in shopDict[COMshop]:
                                                if neededItems[val] not in shopBasket:
                                                    shopBasket.append(neededItems[val])
                                                    val = val + 1
                                                    searchDone = True
                                                    if val > len(neededItems):
                                                        neededItemSearch = True
                                                    print(shopBasket)
                                    if COMRoute[i] == 'b':
                                        COMshop = "ShopB"
                                        val = 0
                                        neededItemSearch = False
                                        while neededItemSearch == False:
                                            if neededItems[val] in shopDict[COMshop]:
                                                if neededItems[val] not in shopBasket:
                                                    shopBasket.append(neededItems[val])
                                                    val = val + 1
                                                    searchDone = True
                                                    if val > len(neededItems):
                                                        neededItemSearch = True
                                                    print(shopBasket)
                                    if COMRoute[i] == 'c':
                                        COMshop = "ShopC"
                                        val = 0
                                        neededItemSearch = False
                                        while neededItemSearch == False:
                                            if neededItems[val] in shopDict[COMshop]:
                                                if neededItems[val] not in shopBasket:
                                                    shopBasket.append(neededItems[val])
                                                    val = val + 1
                                                    searchDone = True
                                                    if val > len(neededItems):
                                                        neededItemSearch = True
                                                    print(shopBasket)
                                    if COMRoute[i] == 'd':
                                        COMshop = "ShopD"
                                        val = 0
                                        neededItemSearch = False
                                        while neededItemSearch == False:
                                            if neededItems[val] in shopDict[COMshop]:
                                                if neededItems[val] not in shopBasket:
                                                    shopBasket.append(neededItems[val])
                                                    val = val + 1
                                                    searchDone = True
                                                    if val > len(neededItems):
                                                        neededItemSearch = True
                                                    print(shopBasket)
                                    if COMRoute[i] == 't':
                                        COMshop = "ShopT"
                                        val = 0
                                        neededItemSearch = False
                                        while neededItemSearch == False:
                                            if neededItems[val] in shopDict[COMshop]:
                                                if neededItems[val] not in shopBasket:
                                                    shopBasket.append(neededItems[val])
                                                    val = val + 1
                                                    searchDone = True
                                                    if val > len(neededItems):
                                                        neededItemSearch = True
                                                    print(shopBasket)
                                    if COMRoute[i]== 's':
                                        COMshop = "ShopS"
                                        val = 0
                                        neededItemSearch = False
                                        while neededItemSearch == False:
                                            if neededItems[val] in shopDict[COMshop]:
                                                if neededItems[val] not in shopBasket:
                                                    shopBasket.append(neededItems[val])
                                                    val = val + 1
                                                    searchDone = True
                                                    if val > len(neededItems):
                                                        neededItemSearch = True
                                                    print(shopBasket)
                        
                       
                    if COMnextNODE == 's'and COMdone == False:
                        COMdone = True
                        COMatShop = 'ShopS'
                        Computer.dijkstraCOM(graph, 's', COMCurrentNode)
                        if len(COMRoute) > 2:
                            global shopBasket
                            while searchDone == False:
                                
                                    i = 0
                                    checkCOMNode = COMRoute[i]
                                    if COMRoute[i] == 'a':
                                        COMshop = "ShopA"
                                        val = 0
                                        neededItemSearch = False
                                        while neededItemSearch == False:
                                            if neededItems[val] in shopDict[COMshop]:
                                                if neededItems[val] not in shopBasket:
                                                    shopBasket.append(neededItems[val])
                                                    val = val + 1
                                                    searchDone = True
                                                    if val > len(neededItems):
                                                        neededItemSearch = True
                                                    print(shopBasket)
                                    if COMRoute[i] == 'b':
                                        COMshop = "ShopB"
                                        val = 0
                                        neededItemSearch = False
                                        while neededItemSearch == False:
                                            if neededItems[val] in shopDict[COMshop]:
                                                if neededItems[val] not in shopBasket:
                                                    shopBasket.append(neededItems[val])
                                                    val = val + 1
                                                    searchDone = True
                                                    if val > len(neededItems):
                                                        neededItemSearch = True
                                                    print(shopBasket)
                                    if COMRoute[i] == 'c':
                                        COMshop = "ShopC"
                                        val = 0
                                        neededItemSearch = False
                                        while neededItemSearch == False:
                                            if neededItems[val] in shopDict[COMshop]:
                                                if neededItems[val] not in shopBasket:
                                                    shopBasket.append(neededItems[val])
                                                    val = val + 1
                                                    searchDone = True
                                                    if val > len(neededItems):
                                                        neededItemSearch = True
                                                    print(shopBasket)
                                    if COMRoute[i] == 'd':
                                        COMshop = "ShopD"
                                        val = 0
                                        neededItemSearch = False
                                        while neededItemSearch == False:
                                            if neededItems[val] in shopDict[COMshop]:
                                                if neededItems[val] not in shopBasket:
                                                    shopBasket.append(neededItems[val])
                                                    val = val + 1
                                                    searchDone = True
                                                    if val > len(neededItems):
                                                        neededItemSearch = True
                                                    print(shopBasket)
                                    if COMRoute[i] == 't':
                                        COMshop = "ShopT"
                                        val = 0
                                        neededItemSearch = False
                                        while neededItemSearch == False:
                                            if neededItems[val] in shopDict[COMshop]:
                                                if neededItems[val] not in shopBasket:
                                                    shopBasket.append(neededItems[val])
                                                    val = val + 1
                                                    searchDone = True
                                                    if val > len(neededItems):
                                                        neededItemSearch = True
                                                    print(shopBasket)
                                    if COMRoute[i] == 's':
                                        COMshop = "ShopS"
                                        val = 0
                                        neededItemSearch = False
                                        while neededItemSearch == False:
                                            if neededItems[val] in shopDict[COMshop]:
                                                if neededItems[val] not in shopBasket:
                                                    shopBasket.append(neededItems[val])
                                                    val = val + 1
                                                    searchDone = True
                                                    if val > len(neededItems):
                                                        neededItemSearch = True
                                                    print(shopBasket)
                            #COMFuelUssed = COMFuelUssed + lastFuelUsage

                
                    

    def dijkstraCOM(graph, curNode, toNode, visitedNodes=[], travelDistances={}, predecessors={}):
        
                if curNode not in graph:
                    raise TypeError('the root of the shortest path tree cannot be found in the graph')
                if toNode not in graph:
                    raise TypeError('the target of the shortest path cannot be found in the graph')    
                if curNode == toNode:
                    path=[]
                    pred=toNode
                    while pred != None:
                        path.append(pred)
                        pred=predecessors.get(pred,None)
                        global COMRoute
                        COMRoute = path
                    print('shortest path: '+str(path)+" cost="+str(travelDistances[toNode]))
                    global lastFuelUsage
                    lastFuelUsage = int(travelDistances[toNode])
                    gameActions.FuelLeft(lastFuelUsage)
                    if searc == False:
                        global currentNode
                        currentNode = 'b'
                        global COMCurrentNode
                        COMCurrentNode = 'b'
                    else:
                        path=[]
                    
                else : 
                    if not visitedNodes: 
                        travelDistances[curNode]=0
                    for nextToNode in graph[curNode] :
                        if nextToNode not in visitedNodes:
                            new_distance = travelDistances[curNode] + graph[curNode][nextToNode]
                            if new_distance < travelDistances.get(nextToNode,float('inf')):
                                travelDistances[nextToNode] = new_distance
                                predecessors[nextToNode] = curNode
                    visitedNodes.append(curNode)
                    unvisited={}
                    for k in graph:
                        if k not in visitedNodes:
                            unvisited[k] = travelDistances.get(k,float('inf'))        
                    x=min(unvisited, key=unvisited.get)
                    Computer.dijkstraCOM(graph,x,toNode,visitedNodes,travelDistances,predecessors)
    if gameMade == True:
        if COMCurrentNode == COMnextNODE:
            pass
        else:
            Computer.dijkstraCOM(graph, COMnextNODE , COMCurrentNode)
            
            

   

app = SampleApp()
app.mainloop()
