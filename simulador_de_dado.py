import random
import PySimpleGUI as sg

class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6

        self.layout = [
            [sg.Text("Jogar o dado?")],
            [sg.Button("Sim"),sg.Button("Não")]
        ]

    def Iniciar(self):
        self.janela = sg.Window("Simulador de Dado",layout=self.layout)
        self.eventos, self.valores = self.janela.Read()
        try:
            if self.eventos =="Sim" or self.eventos =="s":
                self.GerarValorDoDado()
            elif self.eventos == "Não" or self.eventos =="n":
                print("Agradacemos a sua participação!")
            else:
                print("Favor digitar sim (s) ou não (n)!")
        except:
            print("Ocorreu um erro ao receber sua resposta!")
    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo,self.valor_maximo))


simulador = SimuladorDeDado()
simulador.Iniciar()
