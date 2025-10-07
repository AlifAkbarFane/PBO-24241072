class Hero: 
    pass

hero_1 = Hero() 
hero_2 = Hero() 

hero_1.name = "Madara Uchiha"
hero_2.name = "Hasirama Senju"

hero_1.power = 5000
hero_2.power = 5200

hero_1.health = 100
hero_2.Health = 100

print(hero_1.name)
print(hero_2.name)  
print(hero_1.__dict__) 
print(hero_2.__dict__)
