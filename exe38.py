from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.core.audio import SoundLoader
import os

# Direciona para o ficheiro .kv com o design 
Builder.load_file('exe38.kv')

class Galo(BoxLayout):
    primeiro = "X"
    segundo = "O"
    alterna = 0
    contador = 0
    cliques = 0

    def clicado(self, text):
        if text.text == "" and self.primeiro != "":
            if self.alterna % 2 == 0:
                text.text = self.primeiro
                self.cliques += 1
                self.ids.mensagem.text = "É a vez de " + self.segundo
            else:
                text.text = self.segundo
                self.cliques += 1
                self.ids.mensagem.text = "É a vez de " + self.primeiro
        self.alterna += 1

        if self.cliques > 4:
            # Verifica se ganhou
            # primeiro jogador
            # horizontais
            if self.ids.btn1.text == self.primeiro and self.ids.btn2.text == self.primeiro and self.ids.btn3.text == self.primeiro:
                self.ids.mensagem.text = "Ganhou o jogador " + self.primeiro
                self.contador += 1
                self.ids.score1.text = str(int(self.ids.score1.text) + 1)
                self.recomeca()
            elif self.ids.btn4.text == self.primeiro and self.ids.btn5.text == self.primeiro and self.ids.btn6.text == self.primeiro:
                self.ids.mensagem.text = "Ganhou o jogador " + self.primeiro
                self.contador += 1
                self.ids.score1.text = str(int(self.ids.score1.text) + 1)
                self.recomeca()
            elif self.ids.btn7.text == self.primeiro and self.ids.btn8.text == self.primeiro and self.ids.btn9.text == self.primeiro:
                self.ids.mensagem.text = "Ganhou o jogador " + self.primeiro
                self.contador += 1
                self.ids.score1.text = str(int(self.ids.score1.text) + 1)
                self.recomeca()
            # verticais
            elif self.ids.btn1.text == self.primeiro and self.ids.btn4.text == self.primeiro and self.ids.btn7.text == self.primeiro:
                self.ids.mensagem.text = "Ganhou o jogador " + self.primeiro
                self.contador += 1
                self.ids.score1.text = str(int(self.ids.score1.text) + 1)
                self.recomeca()
            elif self.ids.btn2.text == self.primeiro and self.ids.btn5.text == self.primeiro and self.ids.btn8.text == self.primeiro:
                self.ids.mensagem.text = "Ganhou o jogador " + self.primeiro
                self.contador += 1
                self.ids.score1.text = str(int(self.ids.score1.text) + 1)
                self.recomeca()
            elif self.ids.btn3.text == self.primeiro and self.ids.btn6.text == self.primeiro and self.ids.btn9.text == self.primeiro:
                self.ids.mensagem.text = "Ganhou o jogador " + self.primeiro
                self.contador += 1
                self.ids.score1.text = str(int(self.ids.score1.text) + 1)
                self.recomeca()
            # diagonais
            elif self.ids.btn1.text == self.primeiro and self.ids.btn5.text == self.primeiro and self.ids.btn9.text == self.primeiro:
                self.ids.mensagem.text = "Ganhou o jogador " + self.primeiro
                self.contador += 1
                self.ids.score1.text = str(int(self.ids.score1.text) + 1)
                self.recomeca()
            elif self.ids.btn3.text == self.primeiro and self.ids.btn5.text == self.primeiro and self.ids.btn7.text == self.primeiro:
                self.ids.mensagem.text = "Ganhou o jogador " + self.primeiro
                self.contador += 1
                self.ids.score1.text = str(int(self.ids.score1.text) + 1)
                self.recomeca()
            # segundo jogador
            # horizontais
            if self.ids.btn1.text == self.segundo and self.ids.btn2.text == self.segundo and self.ids.btn3.text == self.segundo:
                self.ids.mensagem.text = "Ganhou o jogador " + self.segundo
                self.contador += 1
                self.ids.score2.text = str(int(self.ids.score2.text) + 1)
                self.recomeca()
            elif self.ids.btn4.text == self.segundo and self.ids.btn5.text == self.segundo and self.ids.btn6.text == self.segundo:
                self.ids.mensagem.text = "Ganhou o jogador " + self.segundo
                self.contador += 1
                self.ids.score2.text = str(int(self.ids.score2.text) + 1)
                self.recomeca()
            elif self.ids.btn7.text == self.segundo and self.ids.btn8.text == self.segundo and self.ids.btn9.text == self.segundo:
                self.ids.mensagem.text = "Ganhou o jogador " + self.segundo
                self.contador += 1
                self.ids.score2.text = str(int(self.ids.score2.text) + 1)
                self.recomeca()
            # verticais
            elif self.ids.btn1.text == self.segundo and self.ids.btn4.text == self.segundo and self.ids.btn7.text == self.segundo:
                self.ids.mensagem.text = "Ganhou o jogador " + self.segundo
                self.contador += 1
                self.ids.score2.text = str(int(self.ids.score2.text) + 1)
                self.recomeca()
            elif self.ids.btn2.text == self.segundo and self.ids.btn5.text == self.segundo and self.ids.btn8.text == self.segundo:
                self.ids.mensagem.text = "Ganhou o jogador " + self.segundo
                self.contador += 1
                self.ids.score2.text = str(int(self.ids.score2.text) + 1)
                self.recomeca()
            elif self.ids.btn3.text == self.segundo and self.ids.btn6.text == self.segundo and self.ids.btn9.text == self.segundo:
                self.ids.mensagem.text = "Ganhou o jogador " + self.segundo
                self.contador += 1
                self.ids.score2.text = str(int(self.ids.score2.text) + 1)
                self.recomeca()
            # diagonais
            elif self.ids.btn1.text == self.segundo and self.ids.btn5.text == self.segundo and self.ids.btn9.text == self.segundo:
                self.ids.mensagem.text = "Ganhou o jogador " + self.segundo
                self.contador += 1
                self.ids.score2.text = str(int(self.ids.score2.text) + 1)
                self.recomeca()
            elif self.ids.btn3.text == self.segundo and self.ids.btn5.text == self.segundo and self.ids.btn7.text == self.segundo:
                self.ids.mensagem.text = "Ganhou o jogador " + self.segundo
                self.contador += 1
                self.ids.score2.text = str(int(self.ids.score2.text) + 1)
                self.recomeca()
            elif self.cliques == 9:
                self.ids.mensagem.text = "Empate "
                self.contador += 1
                self.recomeca()
    def recomeca(self):
        if int(self.ids.score1.text) == 3 or int(self.ids.score2.text) == 3: # self.contador < 3:
            self.ids.btn1.disabled = True
            self.ids.btn2.disabled = True
            self.ids.btn3.disabled = True
            self.ids.btn4.disabled = True
            self.ids.btn5.disabled = True
            self.ids.btn6.disabled = True
            self.ids.btn7.disabled = True
            self.ids.btn8.disabled = True
            self.ids.btn9.disabled = True
            self.ids.mensagem.text = "Terminou o jogo"
            self.ids.toca_musica.disabled = False
            self.ids.switch.disabled = False
            self.ids.switch.text = "Switch Ativado"
        else:
            self.ids.btn1.text = ""
            self.ids.btn2.text = ""
            self.ids.btn3.text = ""
            self.ids.btn4.text = ""
            self.ids.btn5.text = ""
            self.ids.btn6.text = ""
            self.ids.btn7.text = ""
            self.ids.btn8.text = ""
            self.ids.btn9.text = ""
            self.primeiro = "X"
            self.segundo = "O"
            self.alterna = 0
            self.cliques = 0

    def play_music(self, obj, valor):
        if valor:
            self.ids.toca_musica.active = True
            self.ids.switch.text = "Tocando"
            music_file = os.path.join(os.getcwd(), './AULA_12/musica-tema.mp3' )
            sound = SoundLoader.load(music_file)
            # sound = SoundLoader.load('applause-01.wav')
            if sound:
                sound.play()
        else:
            self.ids.switch.text = "On para música"

class JogoGaloApp(App):
    def build(self):
        return Galo()

if __name__ == '__main__':
    JogoGaloApp().run()