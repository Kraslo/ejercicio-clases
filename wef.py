from os import get_terminal_size
import re

x = open("response_1636122060619.txt")
print(x) #lista de eventos en formato txt 

emails = []
usuarios: dict = {}
eventos: dict = {}

class User():

    def __init__(self,line: str):
        print(line)

        self.email = re.search(r'[\w.+-]+@[\w-]+\.[\w.-]+', line).group(0) # obtengo el email asociado al evento con regex
        self.exit = bool(re.match("exit", line)) #compruebo si el evento es exit o access
        self.current1 = (False if self.exit else True)
        #print("DEBUG EXIT" , self.exit)
        '''
        Self.current: si es TRUE, el usuario está en el club ahora mismo. Sin embargo, no se puede tenenr el estado EXIT y ACCESS a la vez
        ya que es una contradiccion, por lo que la única manera que current sea TRUE sin contradicciones, es que EXIT sea false. 

        Por lo tanto current siempre tiene el estado cotrario a self.exit
        '''

    def update(self, event: str):
        self.exit = bool(re.search("exit", event))
        self.current1 =  (False if self.exit else True)

class Evento(User):

    def __init__(self,line: str):
        self.event = line
        self.id = re.match("\A[0-9]{1:4}",line)

    def currentstate(self, key: str): #key: mismo formato que self.event
        self.current = bool(re.match("access", self.event))   
        super().update(key)

dictID_events = 0
dictID_users = 0
 

for i in x:
    #print(i)
    
    email = re.search(r'[\w.+-]+@[\w-]+\.[\w.-]+',i).group(0)
    eventos[dictID_events] = Evento(i)
    #print(getattr(eventos[dictID_events],"id")
    if email not in emails or len(usuarios.keys()) == 0: # POR ALGUNA RAZÓN usuarios.values().email no funciona
        #print("tu hermana") #debug
        usuarios[dictID_users] = User(i)
        dictID_users += 1
    else:
        eventos[dictID_events].currentstate(i)

    dictID_events += 1


for n in usuarios.values():
    #print(getattr(n, "current1")) #aquí tampoco parece que le guste la idea de recorrer los objetos y acceder a uno de sus atributos a la vez
    if getattr(n, "current1") ==  True:
        print(getattr(n, "email"))




    

        
    
    

