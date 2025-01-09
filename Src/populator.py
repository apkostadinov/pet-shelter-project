# For Testing purposes

from project import write_to_database
from classes import Patient
from random import randrange

boy_names = ['Abel', 'Bits', 'Bitsy', 'Bizzy', 'Bj', 'Blackie', 'Black-Jack', 'Blast', 'Blaze', 'Blue', 'Bo', 'Bob', 'Bobbie', 'Bobby', 'Bobo', 'Bodie', 'Bogey', 'Bones', 'Bongo', 'Boo', 'Boo-boo', 'Booker', 'Boomer', 'Boone', 'Booster', 'Bootie', 'Boots', 'Boozer', 'Boris', 'Bosco', 'Bosley', 'Boss', 'Boy', 'Bozley', 'Bradley', 'Brady', 'Braggs', 'Brando', 'Bruiser', 'Bruno', 'Brutus', 'Bubba', 'Bubbles', 'Buck', 'Buckeye', 'Bucko', 'Bucky', 'Bud', 'Budda', 'Buddie', 'Buddy', 'Buddy Boy', 'Kane', 'Karma', 'Kato', 'Katz', 'Kibbles', 'Kid', 'Killian', 'King', 'Kipper', 'Kirby', 'Kismet', 'Klaus', 'Koba', 'Kobe', 'Koda', 'Koko', 'Kona', 'Kosmo', 'Koty', 'Kramer', 'Kujo', 'Kurly', 'Lassie', 'Latte', 'Lincoln', 'Linus', 'Little Bit', 'Little-guy', 'Little-one', 'Little-rascal', 'Lucifer', 'Lucky', 'Maverick', 'Max', 'Maximus', 'Mercle', 'Merlin', 'Pooch', 'Poochie', 'Rover', 'Scoobie', 'Scooby', 'Scooby-doo', 'Slick', 'Slinky', 'Sly', 'Snoopy', 'Smarty', 'Sox', 'Spanky', 'Spud', 'Spunky', 'Squeeky', 'Squirt', 'Stanley', 'Sterling', 'Stich', 'Stink', 'Ty', 'Tyler', 'Tyson', 'Vinnie', 'Vinny', 'Willie', 'Wizard', 'Wolfgang', 'Wolfie', 'Woody', 'Woofie', 'Wrigley', 'Wrinkles', 'Wyatt', 'Yin', 'Yoda', 'Yogi', 'Yogi-bear', 'Yukon', 'Zack', 'Zeke', 'Zeus',]
girl_names = ['Abbey', 'Abbie', 'Abby', 'Blanche', 'Blondie', 'Blossom', 'Bonnie', 'Brandi', 'Brandy', 'Bridgett', 'Bridgette', 'Brie', 'Brindle', 'Brit', 'Brittany', 'Brodie', 'Brook', 'Brooke', 'Brownie', 'Buffie', 'Buffy', 'Bug', 'Bugsey', 'Bugsy', 'Butter', 'Butterball', 'Buttercup', 'Butterscotch', 'Buttons', 'Buzzy', 'Cali', 'Callie', 'Cameo', 'Camille', 'Candy', 'Carley', 'Casey', 'Casper', 'Cassie', 'Cassis', 'Cha Cha', 'Chanel', 'Chaos', 'Charisma', 'Chelsea', 'Cherokee', 'Chessie', 'Cheyenne', 'Chi Chi', 'Chic', 'Chiquita', 'Chivas', 'Chloe', 'Chocolate', 'Chrissy', 'Cinnamon', 'Cisco', 'Claire', 'Coconut', 'Codi', 'Cody', 'Kali', 'Kallie', 'Kasey', 'Katie', 'Kayla', 'KC', 'Keesha', 'Kellie', 'Kelly', 'Kelsey', 'Kenya', 'Kerry', 'Kiki', 'Kira', 'Kissy', 'Kitty', 'Kiwi', 'Kyra', 'Lacey', 'Lady', 'Ladybug', 'Laney', 'Layla', 'Lexi', 'Lexie', 'Lexus', 'Libby', 'Lightning', 'Nikita', 'Nikki', 'Niko', 'Nina', 'Olive', 'Olivia', 'Ollie', 'Onie', 'Pandora', 'Patsy', 'Patty', 'Peaches', 'Tequila', 'Tess', 'Tessa', 'Tessie', 'Valinto', 'Vava', 'Vegas', 'Velvet', 'Abbey', 'Abbie', 'Abby', 'Blanche', 'Blondie', 'Blossom', 'Bonnie', 'Brandi', 'Brandy', 'Bridgett', 'Bridgette', 'Brie', 'Brindle', 'Brit', 'Brittany', 'Brodie', 'Brook', 'Brooke', 'Brownie', 'Buffie', 'Buffy', 'Bug', 'Bugsey', 'Bugsy', 'Butter', 'Butterball', 'Buttercup', 'Butterscotch', 'Buttons', 'Buzzy', 'Cali', 'Callie', 'Cameo', 'Camille', 'Candy', 'Carley', 'Casey', 'Casper', 'Cassie', 'Cassis', 'Cha Cha', 'Chanel', 'Chaos', 'Charisma', 'Chelsea', 'Cherokee', 'Chessie', 'Cheyenne', 'Chi Chi', 'Chic', 'Chiquita', 'Chivas', 'Chloe', 'Chocolate', 'Chrissy', 'Cinnamon', 'Cisco', 'Claire', 'Coconut', 'Codi', 'Cody', 'Kali', 'Kallie', 'Kasey', 'Katie', 'Kayla', 'KC', 'Keesha', 'Kellie', 'Kelly', 'Kelsey', 'Kenya', 'Kerry', 'Kiki', 'Kira', 'Kissy', 'Kitty', 'Kiwi', 'Kyra', 'Lacey', 'Lady', 'Ladybug', 'Laney', 'Layla', 'Lexi', 'Lexie', 'Lexus', 'Libby', 'Lightning', 'Nikita', 'Nikki', 'Niko', 'Nina', 'Olive', 'Olivia', 'Ollie', 'Onie', 'Pandora', 'Patsy', 'Patty', 'Peaches', 'Tequila', 'Tess', 'Tessa', 'Tessie', 'Valinto', 'Vava', 'Vegas', 'Velvet', 'Abbey', 'Abbie', 'Abby', 'Blanche', 'Blondie', 'Blossom', 'Bonnie', 'Brandi', 'Brandy', 'Bridgett', 'Bridgette', 'Brie', 'Brindle', 'Brit', 'Brittany', 'Brodie', 'Brook', 'Brooke', 'Brownie', 'Buffie', 'Buffy', 'Bug', 'Bugsey', 'Bugsy', 'Butter', 'Butterball', 'Buttercup', 'Butterscotch', 'Buttons', 'Buzzy', 'Cali', 'Callie', 'Cameo', 'Camille', 'Candy', 'Carley', 'Casey', 'Casper', 'Cassie', 'Cassis', 'Cha Cha', 'Chanel', 'Chaos', 'Charisma', 'Chelsea', 'Cherokee', 'Chessie', 'Cheyenne', 'Chi Chi', 'Chic', 'Chiquita', 'Chivas', 'Chloe', 'Chocolate', 'Chrissy', 'Cinnamon', 'Cisco', 'Claire', 'Coconut', 'Codi', 'Cody', 'Kali', 'Kallie', 'Kasey', 'Katie', 'Kayla', 'KC', 'Keesha', 'Kellie', 'Kelly', 'Kelsey', 'Kenya', 'Kerry', 'Kiki', 'Kira', 'Kissy', 'Kitty', 'Kiwi', 'Kyra', 'Lacey', 'Lady', 'Ladybug', 'Laney', 'Layla', 'Lexi', 'Lexie', 'Lexus', 'Libby', 'Lightning', 'Nikita', 'Nikki', 'Niko', 'Nina', 'Olive', 'Olivia', 'Ollie', 'Onie', 'Pandora', 'Patsy', 'Patty', 'Peaches', 'Tequila', 'Tess', 'Tessa', 'Tessie', 'Valinto', 'Vava', 'Vegas', 'Velvet', 'Abbey', 'Abbie', 'Abby', 'Blanche', 'Blondie', 'Blossom', 'Bonnie', 'Brandi', 'Brandy', 'Bridgett', 'Bridgette', 'Brie', 'Brindle', 'Brit', 'Brittany', 'Brodie', 'Brook', 'Brooke', 'Brownie', 'Buffie', 'Buffy', 'Bug', 'Bugsey', 'Bugsy', 'Butter', 'Butterball', 'Buttercup', 'Butterscotch', 'Buttons', 'Buzzy', 'Cali', 'Callie', 'Cameo', 'Camille', 'Candy', 'Carley', 'Casey', 'Casper', 'Cassie', 'Cassis', 'Cha Cha', 'Chanel', 'Chaos', 'Charisma', 'Chelsea', 'Cherokee', 'Chessie', 'Cheyenne', 'Chi Chi', 'Chic', 'Chiquita', 'Chivas', 'Chloe', 'Chocolate', 'Chrissy', 'Cinnamon', 'Cisco', 'Claire', 'Coconut', 'Codi', 'Cody', 'Kali', 'Kallie', 'Kasey', 'Katie', 'Kayla', 'KC', 'Keesha', 'Kellie', 'Kelly', 'Kelsey', 'Kenya', 'Kerry', 'Kiki', 'Kira', 'Kissy', 'Kitty', 'Kiwi', 'Kyra', 'Lacey', 'Lady', 'Ladybug', 'Laney', 'Layla', 'Lexi', 'Lexie', 'Lexus', 'Libby', 'Lightning', 'Nikita', 'Nikki', 'Niko', 'Nina', 'Olive', 'Olivia', 'Ollie', 'Onie', 'Pandora', 'Patsy', 'Patty', 'Peaches', 'Tequila', 'Tess', 'Tessa', 'Tessie', 'Valinto', 'Vava', 'Vegas', 'Velvet', ]

def boy_name():
    idx = randrange(0, len(boy_names))
    return boy_names[idx]

def girl_name():
    idx = idx = randrange(0, len(girl_names))
    return girl_names[idx]

def main():
    population = int(input('How many entries? '))

    for i in range(population):
        gend = randrange(0,2)
        if gend == 0:
            gend = 'male'
            name_rand = str(boy_name())
        else:
            gend = 'female'
            name_rand = str(girl_name())

        spec = randrange(0,2)
        if spec == 0:
            spec = 'dog'
            age_rand = randrange(0, 12)
        else:
            spec = 'cat'
            age_rand = randrange(0, 18)
        patient = Patient(spec, gend, name_rand, age_rand)
        write_to_database(patient, silent = True)
        print(f'Added entry number {i}.')
    else:
        print(f'Finished. Added {population} entries')

if __name__ == "__main__":
    main()



