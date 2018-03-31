class Turnstile_controller(object):
    def lock(self):
        print("турникет закрыт ,проход запрещен!!")

    def unlock(self):
        print("монета брошена,турникет открыт, ПРОХОДИТЕ!!")

    def thankyou(self):
        print("Монета брошена повторно.Спасибо за пожертвование")

    def alarm(self):
        print("Проход через закрытый турникет!!Виу,виу полиция уже едет ")


class Turnstile(object):
    pass


class Turnstile_state():
    def coin(self, t : Turnstile)->None:
        pass
    def passs(self, t : Turnstile)->None:
        pass


class Locked_turnstile_state(Turnstile_state):
    def coin(self, t : Turnstile):
        t.set_unlocked()
        t.unlock()
        
    def passs(self,t : Turnstile):
        t.alarm()
        

class Unlocked_turnstile_state(Turnstile_state):
    def coin(self,t :Turnstile):
        t.thankyou()
        
    def passs(self,t :Turnstile):
        print("проход выполнен")
        t.set_locked()
        t.lock()
        


class Turnstile(object):
    locked_state = Locked_turnstile_state()
    unlocked_state = Unlocked_turnstile_state()
    turnstile_controller = Turnstile_controller()
    def __init__(self ): #можт надо добавит tutnslitecontroller
        #self.turnstile_controller: = t        
        self.state = self.locked_state

    def coin(self)->None:
        self.state.coin(self)

    def passs(self)->None:
        self.state.passs(self)

    def set_locked(self)->None:
       self.state = self.locked_state

    def set_unlocked(self)->None:
        self.state = self.unlocked_state

    def is_locked(self)->bool:
        return self.state == self.locked_state

    def is_unlocked(self)->bool:
        return self.state == self.unlocked_state

    def thankyou(self)->None:
        self.turnstile_controller.thankyou()

    def alarm(self)->None:
        self.turnstile_controller.alarm()

    def lock(self)->None:
        self.turnstile_controller.lock()

    def unlock(self)->None:
        self.turnstile_controller.unlock()
    




my_turnstile = Turnstile()
print(my_turnstile.is_locked())
my_turnstile.coin()
print(my_turnstile.is_locked())
my_turnstile.coin()
print(my_turnstile.is_locked())
my_turnstile.passs()
print(my_turnstile.is_locked())
my_turnstile.passs()
print(my_turnstile.is_locked())
my_turnstile.coin()
print(my_turnstile.is_locked())
my_turnstile.passs()      
print(my_turnstile.is_locked())
my_turnstile.passs()     
    