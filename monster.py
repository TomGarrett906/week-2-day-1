player_hp = 100
monster_hp = 100
player_attack = int(input("Enter attack damgage: "))
monster_attack = 10

print("A wild monster approaches!")

while monster_hp > 0:
    monster_hp = monster_hp - player_attack
    print("Monster: ouch!")
    print(f"Monster HP: {monster_hp}")
    player_hp = player_hp - monster_attack
    print("Monster does 10hp of damage! ")
    print(f"Player HP: {player_hp}")
    player_attack = int(input("Enter attack damgage: "))
else:
    print("Congratulations! You've defeated the monster!!!")



