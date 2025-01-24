class OperasBas:
    numero1=0
    numero2=0
    res=0
    
    
    #declaracion de constructor de la clase
    def __init__(self, a,b):
        self.numero1=a 
        self.numero2=b

    #declaracion de metodos
    def suma(self):
        self.res=self.numero1+self.numero2
        print("La suma es: {}".format(self.res))


def main():
    obj=OperasBas(3,5)
    obj.suma()



if __name__=="__main__":
    main()