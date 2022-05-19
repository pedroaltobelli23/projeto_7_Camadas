
#importe as bibliotecas
from suaBibSignal import *
import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
import sys

#funções a serem utilizadas
def signal_handler(signal, frame):
    print('You pressed Ctrl+C!')
    sys.exit(0)

#converte intensidade em Db, caso queiram ...
def todB(s):
    sdB = 10*np.log10(s)
    return(sdB)




def main():
    
   
    #********************************************instruções*********************************************** 
    # seu objetivo aqui é gerar duas senoides. Cada uma com frequencia corresposndente à tecla pressionada
    # então inicialmente peça ao usuário para digitar uma tecla do teclado numérico DTMF
    # agora, voce tem que gerar, por alguns segundos, suficiente para a outra aplicação gravar o audio, duas senoides com as frequencias corresposndentes à tecla pressionada, segundo a tabela DTMF
    # se voce quiser, pode usar a funcao de construção de senoides existente na biblioteca de apoio cedida. Para isso, você terá que entender como ela funciona e o que são os argumentos.
    # essas senoides tem que ter taxa de amostragem de 44100 amostras por segundo, entao voce tera que gerar uma lista de tempo correspondente a isso e entao gerar as senoides
    # lembre-se que a senoide pode ser construída com A*sin(2*pi*f*t)
    # o tamanho da lista tempo estará associada à duração do som. A intensidade é controlada pela constante A (amplitude da senoide). Seja razoável.
    # some as senoides. A soma será o sinal a ser emitido.
    # utilize a funcao da biblioteca sounddevice para reproduzir o som. Entenda seus argumento.
    # grave o som com seu celular ou qualquer outro microfone. Cuidado, algumas placas de som não gravam sons gerados por elas mesmas. (Isso evita microfonia).
    
    # construa o gráfico do sinal emitido e o gráfico da transformada de Fourier. Cuidado. Como as frequencias sao relativamente altas, voce deve plotar apenas alguns pontos (alguns periodos) para conseguirmos ver o sinal
    #fs -> taxa de amostragem sample rate -> =44100 amostras por segundo

    print("Inicializando encoder")
    print("Aguardando usuário")
    print("Gerando Tons base")
    print("Executando as senoides (emitindo o som)")
    NUM = input("Escolha um numero: ")
    print("Gerando Tom referente ao símbolo : {}".format(NUM))
    freq1 = 0
    freq2 = 0
    outofrange=False

    if NUM == "1":
        freq1 = 1206
        freq2 = 697
    elif NUM == "2":
        freq1 = 1339
        freq2 = 697
    elif NUM == "3":
        freq1 = 1477
        freq2 = 697
    elif NUM == "4":
        freq1 = 1206
        freq2 = 770
    elif NUM == "5":
        freq1 = 1339
        freq2 = 770
    elif NUM == "6":
        freq1 = 1477
        freq2 = 770
    elif NUM == "7":
        freq1 = 1206
        freq2 = 852
    elif NUM == "8":
        freq1 = 1339
        freq2 = 852
    elif NUM == "9":
        freq1 = 1477
        freq2 = 852
    elif NUM == "0":
        freq1 = 1339
        freq2 = 941
    elif NUM == "X":
        freq1 = 1206
        freq2 = 941
    elif NUM == "#":
        freq1 = 1477
        freq2 = 941
    elif NUM == "A":
        freq1 = 1633
        freq2 = 697
    elif NUM == "B":
        freq1 = 1633
        freq2 = 770
    elif NUM == "C":
        freq1 = 1633
        freq2 = 852
    elif NUM == "D":
        freq1 = 1633
        freq2 = 941
    else:
        outofrange = True
        freq1 = 0
        freq2 = 0

    if not outofrange:
        fs = 44100
        classe = signalMeu()
        A = 0.5
        print(freq1)
        print(freq2)
        sinal1 = classe.generateSin(freq=freq1,amplitude=A,time=2,fs=fs)
        sinal2 = classe.generateSin(freq=freq2,amplitude=A,time=2,fs=fs)
        sinal = sinal1[1] + sinal2[1]
        
        #aguarda fim do audio
        sd.play(sinal,fs)
        sd.wait()
        
        # Exibe gráficos
        plt.plot(sinal1[0],sinal)
        plt.xlim([0, 0.1])
        plt.show()
    else:
        print("charactere nao esta dentro dos disponiveis")

    #plotFFT(self, signal, fs)
    

if __name__ == "__main__":
    main()
