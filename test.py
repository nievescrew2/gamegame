def combat():
        print("You have entered combat with the monsters. You can either attack or defend. If you attack, you will deal damage to the monster, but they will also deal damage to you. If you defend, you will block some of the damage from the monster's attack, but you won't deal any damage to them. Choose wisely! \n")
        health = 100
        monsterhealth = 50
        monsterdamage = 10
        yourdamage = 15
        while True:
        #health > 0:
        #and monsterhealth > 0:
            action = input("Do you attack or defend? | A = Attack | D = Defend").upper()
            if action == "A":
                monsterhealth -= yourdamage
                print(f"You attack the monster and deal {yourdamage} damage. The monster's health is now {monsterhealth}.")
                if monsterhealth <= 0:
                    print("You have defeated the monster! You win!")
                    break
                health -= monsterdamage
                print(f"The monster attacks you and deals {monsterdamage} damage. Your health is now {health}.")
            elif action == "D":
                health -= monsterdamage/2
                print(f"You block the monster's attack and take {monsterdamage/2} damage/ Your health is now {health}.")
                break
            else:
                print("Invalid input. Please enter A or D.")

combat()