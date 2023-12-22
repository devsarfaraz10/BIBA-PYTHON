class Father:
    def quality(self):
        print('inside Father class')
        print('Father has intelligence & deep thinking power')
        print('\n')
        
class Son(Father):
    def aim(self):
        print('inside Son class')
        print('child wants to be a software engineer')
        print('\n')
        
mushfiq = Son()
mushfiq.quality()
mushfiq.aim()                