from wardrobe import Wardrobe
from wardrobe import Material
import random

class NarniaJourney:
    def __init__(self):
        self.enteredNarnia = 0
        self.journeyComplete = False
        self.safety = 10000
        self.n = 0
        self.startJourney()

    def startJourney(self):
        '''
        1 create a wardrobe
        2 kick the wardrobe
        3 if the wardrobe is not broken, open the wardrobe
        4 loop, trying to enter narnia:
            A 1:100 chance to enter narnia
            if in Narnia:
                fight the witch


        '''
        # create the wardrobe
        print('Starting the journey.')
        self.myWardrobe = Wardrobe("the wardrobe", Material.CARBON_FIBRE)

        # kick the wardrobe
        self.myWardrobe.kick(random.randint(1,15))

        # if the wardrobe is not broken, open the wardrobe
        if(not self.myWardrobe._broken):
            print("You kicked the wardrobe but luckily it didnt break!")
            # loop trying to enter narnia
            while not self.journeyComplete:
                self.n += 1
                self.myWardrobe.open()
                self.myWardrobe.get_in()

                # 1 in 100 chance to enter narnia
                if random.random() > 0.99:
                    print("You're lucky! Entering Narnia...")
                    self.enterNarnia()
                else:
                    pass
                    #print('no success')
                self.myWardrobe.get_out()
                self.myWardrobe.close()
                if self.n > self.safety:
                    print('broke off early')
                    self.journeyComplete = True
                    return
        else:
            print('The wardrobe broke. restarting...')
            self.startJourney()
            return


    def enterNarnia(self):
        self.enteredNarnia += 1

        # so now we're in narnia, you can fight the witch
        self.fightTheWitch()


    def fightTheWitch(self):
        '''
        we're in narnia and we can fight the witch.
        the chance we win depends on how often we have entered narnia already
        '''
        chance = self.enteredNarnia/100
        print ('Entered narnia ', self.enteredNarnia, 'times')
        print('New chance:', chance)
        r = random.random()
        if r < chance:
            print('You won the fight!')
            self.speakToLion()
            self.journeyComplete = True
        else:
            print('You lost the fight. Re-attempting to enter Narnia...')
        pass

    def speakToLion(self):
        print('Speaking to lion')
        print('Congratulations, you completed the journey!')
        return

class Lion:
    pass

class Witch:
    pass

if __name__ == "__main__":
    narno = NarniaJourney()
