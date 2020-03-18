
import os
import sys #this allows you to use the sys.exit command to quit/logout of the application
def main():
    menu()
    # login()
  
# def login():
#     username="user"
#     password="pass"
#     print("Enter username : ")
#     answer1=input()
#     print("Enter password : ")
#     answer2=input()
#     if answer1==username and answer2==password:
#         print("Welcome - Access Granted")
#         menu()

def menu():
    os.system("clear")
    print("************MAIN MENU**************")
    #time.sleep(1)
    print()

    choice = input("""
                      !!!!!!!EARLY ACCESS!!!!!!!!
                      A: List Emulatores
                      B: List Games
                      C: Open Emulator
                      D: Open Emulator With Game (Just for mGBA!)
                      Q: Quit/Log Out

                      Please enter your choice: """)

    if choice == "A" or choice =="a":
        ListEmulatores()
    elif choice == "B" or choice =="b":
        ListGames()
    elif choice == "C" or choice =="c":
        openEmulator()
    elif choice=="D" or choice=="d":
        OpenEmulatorWithGame()
    elif choice=="Q" or choice=="q":
        sys.exit
    else:
        print("You must only select either A,B,C, or D.")
        print("Please try again")
        menu()

def ListEmulatores():
    os.system("clear")
    print("""List of Emulatores : 
                1-Nintendo DS:
                    1.1-Desmume
                2-GameBoy:
                    2.1-mGBA
                    2.2-Visual Boy Advance
                3-Nintendo 3DS:
                    3.1-Citra
    
                            """)
    input("Press Enter to continue...")
    menu()

def ListGames():
    os.system("clear")
    print("""List of Emulatores : 
                1-Nintendo DS:
                    1.1-Pokemon Platinum
                    1.2-Pokemon Heart Gold
                    1.3-Pokemon Soul Silver
                    1.4-New Super Mario Bros
                2-GameBoy:
                    2.1-pokemon Fire Red
                    2.2-Pokemon Jupiter
                3-Nintendo 3DS:
                    3.1-COMMING SOON
    
                            """)
    input("Press Enter to continue...")
    menu()


def OpenEmulatorWithGame():
    os.system("clear")
    print("************ Menu **************")
    #time.sleep(1)
    print()

    choice = input("""
                      !!!Please Select a Game!!!!
                      !!!!!!!EARLY ACCESS!!!!!!!!
                      1: Pokemon Fire Red   
                      2: Pokemon Jupiter
                      3: Pokemon Ultra violet
                      4: Pokemon Ruby
                      5: Pokemon League Of Legends
                      6: Pokemon Abandoned Ruby
                      7: Pokemon Adamantite
                      8: Pokemon A Grand Day Out
                      9: Pokemon Dark Rising 2
                      10: Pokemon Dreary
                      11: Pokemon Emerald
                      12: Pokemon Gold Chapter
                      13: Pokemon Kanlara Adventures
                      14: Pokemon Kanlara Ultimate
                      15: Pokemon Master Quest
                      16: Pokemon Mystery Dungeon
                      17: Pokemon Red Chapter
                      18: Yu-Gi-Oh Duel Academy
                      19: Mario Kart Super Circuit
                      20: Back to main menu

                      Please enter your choice: """)

    if choice == "1":
        OpenGameWithGame("mGBA", "PokemonFireRed")
    elif choice == "2":
        OpenGameWithGame("mGBA", "PokemonJupiter")
    elif choice == "3":
        OpenGameWithGame("mGBA", "PokemonUltraViolet")
    elif choice=="4":
        OpenGameWithGame("mGBA", "PokemonRuby")
    elif choice=="5":
        OpenGameWithGame("mGBA", "PokemonLeagueOfLegends")
    elif choice=="6":
        OpenGameWithGame("mGBA", "PokemonAbandonedRuby")
    elif choice=="7":
        OpenGameWithGame("mGBA", "PokemonAdamantite")
    elif choice=="8":
        OpenGameWithGame("mGBA", "PokemonAGrandDayOut")
    elif choice=="9":
        OpenGameWithGame("mGBA", "PokemonDarkRising2")
    elif choice=="10":
        OpenGameWithGame("mGBA", "PokemonDreary")
    elif choice=="11":
        OpenGameWithGame("mGBA", "PokemonEmerald")
    elif choice=="12":
        OpenGameWithGame("mGBA", "PokemonGoldChapter")
    elif choice=="13":
        OpenGameWithGame("mGBA", "PokemonKanlaraAdventures")
    elif choice=="14":
        OpenGameWithGame("mGBA", "PokemonKanlaraUltimate")
    elif choice=="15":
        OpenGameWithGame("mGBA", "PokemonMasterQuest")
    elif choice=="16":
        OpenGameWithGame("mGBA", "PokemonMysteryDungeon")
    elif choice=="17":
        OpenGameWithGame("mGBA", "PokemonRedChapter")
    elif choice=="18":
        OpenGameWithGame("mGBA", "YuGiOhDuelAcademy")
    elif choice=="19":
        OpenGameWithGame("mGBA", "MarioKartSuperCircuit")
    elif choice=="20":
       menu()
    else:
        print("You must only select either A,B,C,D or Q.")
        print("Please try again")
        OpenEmulatorWithGame()

def OpenGameWithGame(emulator, game):
    if emulator == "mGBA":
        os.system("/Volumes/PC_EMULATOR/Emuladores/mGBA/MacOS/bin/mgba -bios /Volumes/PC_EMULATOR/Games/GameBoy/" + game + "/" + game + ".gba");
    else:
        print("Error-Emulator not found!!")
        input("Press Enter to continue...")
        OpenEmulatorWithGame()
def openEmulator():
    os.system("clear")
    print("************ Menu **************")
    #time.sleep(1)
    print()

    choice = input("""
                      !!!!!!!EARLY ACCESS!!!!!!!!
                      1: mGBA  
                      2: DeSmuME
                      3: Citra
                      4: Back to main menu

                      Please enter your choice: """)

    if choice == "1" or choice =="1":
        OpenEmulatorWithGame()
        # os.system("/Volumes/PC_EMULATOR/Emuladores/mGBA/MacOS/bin/mgba");
    elif choice == "2" or choice =="2":
        os.system("/Volumes/PC_EMULATOR/Emuladores/Desmume/MacOS/DeSmuME.app/Contents//MacOS/DeSmuME");
    elif choice == "3" or choice =="3":
        os.system("/Volumes/PC_EMULATOR/Emuladores/Citra/MacOS/nightly/citra-qt.app/Contents/MacOS/citra-qt");
    elif choice=="4" or choice=="4":
        menu()
    else:
        print("You must only select either 1,2,3 or 4.")
        print("Please try again")
        OpenEmulatorWithGame()
def notDone():
    pass
main()

