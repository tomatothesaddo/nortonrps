#now that I'm not crunching out programs I can get back to adding pointless and frivolous little
#gimmicks to my projects :P
#\/core of the computer rps module
import random
#\/ surprise tools that will help us later
import os
import time


#title screen, might add a functional "press any key to continue" at some point but an uncalled variable works for now right?
print("")
print("")
print("")
print("              Norton Studios Proudly Presents. . .")
time.sleep(0.5)
print("              A game of well-thought strategy, deadly skill, and emotional turbulence...")
time.sleep(2)
os.system('cls' if os.name == 'nt' else "printf '\033c'")
print("              Norton Studios Proudly Presents. . .")
print("              A game of well-thought strategy, deadly skill, and emotional turbulence...")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")

print("=========================ROCK==============================")
print("===========================PAPER===========================")
print("==============================SCISSORS=====================")
print("")
print("")
print("     ~Norton Commander OS (tm) exclusive edition~")
print("")
print("")
print("")
print("         now with FULL Norton Eyespace (tm) support; take your work- ")
print("         -flow to the next level with all new patented technology!")
print("         call now and step into the future at: +1 202-918-2132")
print("")
print("")
print("")
print("c. Norton Studios (tm) ltd., a Norton Softproducts (tm) subsidiary")
print("")
print("")
print("")
cont = input("(press enter to continue)")

#pointless fluff because I like doing random stuff like these
print("loading...")
time.sleep(0.1)
print("initializing graphics:")
time.sleep(0.1)
print("")
print("-SUCCESS-")
time.sleep(0.01)
print("loading ruleset from /usr/share/bin/Norton Systems/gamedata/rules")
time.sleep(0.1)
print("")
print("-SUCCESS-")
time.sleep(0.01)
print("initializing enemy strategies...")
time.sleep(0.1)
print(" ")
print("-SUCCESS-")
time.sleep(0.01)
print("initializing SWEP classes from /usr/share/bin/Norton Systems/gamedata/sweps/classes")
time.sleep(0.1)
print("")
print("-SUCCESS-")
time.sleep(0.01)
print("initializing SWEP data from /usr/share/bin/Norton Systems/gamedata/sweps/data")
time.sleep(0.1)
print("")
print("-SUCCESS-")
print("loading foes from /usr/share/bin/Norton Systems/gamedata/chars")
time.sleep(0.01)
print("-SUCCESS-")
time.sleep(0.01)
print("loading all.spawn from /usr/share/bin/Norton Systems/gamedata/")
time.sleep(0.01)
print("-SUCCESS-")
print("")
time.sleep(0.1)
print("finalizing...")
time.sleep(0.3)
print("done!  press enter to continue!")
cont = input("#################################")
os.system('cls' if os.name == 'nt' else "printf '\033c'")
#rulescreen!
print("Selected SWEPSs: 'Default', -none-")
print("___________________________________")
print("Selected ruleset: 'Default', by 'Norton Studios'")
print("___________________________________")
print("rules:")
print("")
print("there are 3 tools at your disposal: Rock, (defeats: Scissors) (defeated by: paper)")
print("Paper, (defeats: Rock) (Defeated by: Scissors)")
print("Scissors, (defeats: paper) (defeated by: Rock)")
print("")
print("")
print("")
print("")
cont = input("ready?")
print("")
print("")
print("")
print("")
print("")
print("-------------------------------------------------------------------")


#random opponent selection system- the ramifications of this were tiring, but it adds some variety!
opnet = random.randint(1,4)
if opnet == 1:
    print("Barney, Master of the Universe is your opponent!")
else:
    if opnet == 2:
        print("Martin, King of the Spoons is your challenger")
    else:
        if opnet == 3:
            print("Sergiy, kind of the css community servers will now proceed to destroy you")
        else:
            if opnet == 4:
                print("Norton, the most handsome of the squirrels is your foe")
            else:
                print("if you're seeing this something has gone horribly wrong, TAKE OFF YOUR SKIN")
#for use in the endscreen and maybe some refactoring of the outcome module at a later date

if opnet == 1:
    opname = ("Barney")
if opnet == 2:
    opname = ("Martin")
if opnet == 3:
    opname = ("Sergiy")
if opnet == 4:
    opname = ("Norton")

#this thing above will never show unless the code has been modified lol
print('')
#this is where the random module comes in handy
numcomp = random.randint(1, 3)
#player choice selection screen, simple but nifty
print("enter one of the following:")
print("1- rock")
print("2- paper")
print("3- scissors")
numusr = int(input("enter your number choice (1,2,3) here!"))
#player choice announcement.  Again, pointless, but simple and nice
if numusr == 1:
    print("your choice: rock")
else:
    if numusr == 2:
        print("your choice: paper")
    else:
        print("your choice: scissors")
#the most time consuming part.  I hardcoded all of the char choices, which, looking back, wasn't done in the best way.
#I should have handled the namespace with a variable, significantly increasing the modifiability
#of the character list, but it's too late now, and this game isn't meant to be modded, contrary to what
#the fake loadscreen might imply lol
#doesn't really matter anyways :P
if numcomp == 1 and opnet == 1:
    print("Barney's choice: rock")
else:
    if numcomp == 1 and opnet == 2:
        print("Martin's choice: rock")
    else:
        if numcomp == 1 and opnet == 3:
            print("Sergiy's choice: rock")
        else:
            if numcomp == 1 and opnet == 4:
                print("Norton's choice: rock")
            else:
                if numcomp == 2 and opnet == 1:
                    print("Barney's choice: paper")
                else:
                     if numcomp == 2 and opnet == 2:
                         print("Martin's choice: paper")
                     else:
                        if numcomp == 2 and opnet == 3:
                            print("Sergiy's choice: paper")
                        else:
                            if numcomp == 2 and opnet == 4:
                                print("Norton's choice: paper")
                            else:
                                if numcomp == 3 and opnet == 1:
                                    print("Barney's choice: scissors")
                                else:
                                    if numcomp == 3 and opnet == 2:
                                        print("Martin's choice: scissors")
                                    else:
                                        if numcomp == 3 and opnet == 3:
                                            print("Sergiy's choice: scissors")
                                        else:
                                            if numcomp == 3 and opnet == 4:
                                                print("Norton's choice: scissors")
#ill use a numeric system for the endscreen, 0 will be tie, 1 will be victory, and 2 will be loss.
#shouldn't be too hard, but again, it'll form a neat little experience.
#after all, pointless and excessive use of my basic python skills are the point of this whole thing
#are they not?
endscrn = 0

#rock vs blank
if numusr == 1 and numcomp == 1:
    print("the rocks fruitlessly collide! (tie!)")
    endscrn = 0
if numusr == 1 and numcomp == 2:
    print("the paper envelops the rock! (loss!)")
    endscrn = 2
if numusr == 1 and numcomp == 3:
    print("the rock SMASHES the scissors apart! (victory!)")
    endscrn = 1

#paper vs blank
if numusr == 2 and numcomp == 1:
    print("the paper swallows the rock whole! (victory!)")
    endscrn = 1
if numusr == 2 and numcomp == 2:
    print("other than a vague shuffling sound, nothing happens.  Maybe a paper airplane..?  (tie!)")
    endscrn = 0
if numusr == 2 and numcomp == 3:
    print("the scissors viciously slash the paper (loss!)")
    endscrn = 2

#scissors vs blank
if numusr == 3 and numcomp == 1:
    print("the rock shatters your fruitless attempt to defeat it (loss!)")
    endscrn = 2
if numusr == 3 and numcomp == 2:
    print("your scissors artfully cut up the paper into a neat selection of triangles (victory!")
    endscrn = 1
if numusr == 3 and numcomp == 3:
    print("A long duel of scissors entails, but alas, it ends with no victor (tie!)")
print("")
cont = input("(press any key to continue)")
os.system('cls' if os.name == 'nt' else "printf '\033c'")
#endscreen- this is gonna take a whiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiile
if endscrn == 0:
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("|                                                      |")
    print("|                                                      |")
    print("|                                                      |")
    print("|                                                      |")
    print("|                                                      |")
    print("|                                                      |")
    print("|                                                      |")
    print("|        {tie: in the end, none came out on top}       |")
    print("|                                                      |")
    print("|                                                      |")
    print("|                =========================             |")
    print("|                =========================             |")
    print("|                                                      |")
    print("|                                                      |")
    print("|                =========================             |")
    print("|                =========================             |")
    print("|                                                      |")
    print("|                                                      |")
    print("|                                                      |")
    print("|                                                      |")
    print("|                                                      |")
    print("|                                                      |")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    
if endscrn == 1:
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("|                                                      |")
    print("|                                                      |")
    print("|                                                      |")
    print("|                                                      |")
    print("|                                                      |")
    print("|                                                      |")
    print("|                                                      |")
    print("|        {Victory!: Youuuuuuuuuuuu're a winner!}       |")
    print("|                                                      |")
    print("|                                                      |")
    print("|                                                      |")
    print("|                          |||||                       |")
    print("|                          |||||                       |")
    print("|                          |||||                       |")
    print("|                          |||||                       |")
    print("|                =========================             |")
    print("|                =========================             |")
    print("|                          |||||                       |")
    print("|                          |||||                       |")
    print("|                          |||||                       |")
    print("|                          |||||                       |")
    print("|                                                      |")
    print("|                                                      |")
    print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")


if endscrn == 2:
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("|                                                      |")
    print("|                                                      |")
    print("|                                                      |")
    print("|                                                      |")
    print("|                                                      |")
    print("|                                                      |")
    print("|                                                      |")
    print("|        {" + opname + " Defeated you!}                            |")
    print("|                                                      |")
    print("|                                                      |")
    print("|                                                      |")
    print("|                                                      |")
    print("|                                                      |")
    print("|                                                      |")
    print("|                =========================             |")
    print("|                =========================             |")
    print("|                                                      |")
    print("|                                                      |")
    print("|                                                      |")
    print("|                                                      |")
    print("|                                                      |")
    print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
print("")
print("thank you for playing Rock Paper Scissors- Norton Commander OS (tm) edition!")
time.sleep(5)
cont = input("(press any key to continue)")
