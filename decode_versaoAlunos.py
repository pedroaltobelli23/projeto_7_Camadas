#!/usr/bin/env python3
"""Show a text-mode spectrogram using live microphone data."""

# Importe todas as bibliotecas
# -------------------------------- IMPORTAÇÕES ------------------------------- #
import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
from suaBibSignal import *
from time import sleep
import peakutils as pk


def main():


    signal = signalMeu()
    sample_frequency = 44100
    
    #configurações do módulo sounddevice
    sd.default.samplerate = sample_frequency
    sd.default.channels = 2  # voce pode ter que alterar isso dependendo da sua placa
    duration = 2  # tempo de amostragem em segundos


    print('Captura começara em 5 segundos')
    sleep(2)
    print('------------------- GRAVAÇÃO INICIADA -------------------')

   #calcule o numero de amostras "numAmostras" que serao feitas (numero de aquisicoes)
   # Já que em 1s temos 44100 amostras, então o numero de amostras será o tempo de amostragem multiplicado pela frequencia de amostragem
    numAmostras = int(duration * sample_frequency)
    audio = sd.rec(numAmostras, samplerate=sample_frequency, channels=2)
    sd.wait()
    print("...FIM")

    #analise sua variavel "audio". pode ser um vetor com 1 ou 2 colunas, lista ...
    #grave uma variavel com apenas a parte que interessa (dados)
    audioMono1 = audio[:,0]
    audioMono2 = audio[:,1]
    # use a funcao linspace e crie o vetor tempo. Um instante correspondente a cada amostra!
    t = np.linspace(0, duration, numAmostras)

    # plot do gravico  áudio vs tempo!


    ## Calcula e exibe o Fourier do sinal audio. como saida tem-se a amplitude e as frequencias
    xf, yf = signal.calcFFT(audioMono1, sample_frequency)
    signal.plotFFT(audioMono1, sample_frequency)
    #esta funcao analisa o fourier e encontra os picos
    #voce deve aprender a usa-la. ha como ajustar a sensibilidade, ou seja, o que é um pico?
    #voce deve tambem evitar que dois picos proximos sejam identificados, pois pequenas variacoes na
    #frequencia do sinal podem gerar mais de um pico, e na verdade tempos apenas 1.

    index = pk.indexes(yf, thres=.25, min_dist=500)
    print(index)

    #encontre na tabela duas frequencias proximas às frequencias de pico encontradas e descubra qual foi a tecla
    #print a tecla.


    ## Exibe gráficos
    plt.show()

if __name__ == "__main__":
    main()
