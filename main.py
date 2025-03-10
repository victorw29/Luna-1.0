#Arquivo principal


#import speech_recognition as sr 

#Cria um reconhecedor de fala online
#r = sr.Recognizer()

#Abrir o microfone para a captura
#with sr.Microphone() as source:
#    while True:
#        audio = r.listen(source) #Define microfone como fonte de audio

    
#        print(r.recognize_google(audio, language = 'pt'))


from vosk import Model, KaldiRecognizer
import os 
import pyaudio
import pyttsx3
import json
import webbrowser
from core import _init_
import time
import datetime
import urllib.parse  # Adicione esta importação no início do arquivo

#Síntese de voz
engine = pyttsx3.init()
engine.setProperty('rate', 180)  
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) 

def speak(text):
    engine.say(text)
    engine.runAndWait()

#Instancia de classe
info = _init_.SystemInfo()

#recebe a função das horas 
hora_atual = info.get_time()

# reconhecimento de fala 

model_path = 'C:/Users/Martins/Desktop/victor/projetos/Luna-1.0/models'

model = Model(model_path)
rec = KaldiRecognizer(model, 16000)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=2048)
stream.start_stream()

#Fala Inicial da assistente
speak('Oi! Sou a Luna em que posso ajudar??')

#Função para criar lista de Tarefas e adicionar tarefas
def add_task():
     task = [] #cria a lista de tarefas
     while True:
        print('Que tarefa você quer adicionar?? \n')
        speak('Que tarefa você quer adicionar??')

        # Aguarda a resposta do usuário
        while True:
            data = stream.read(2048, exception_on_overflow=False)
            if rec.AcceptWaveform(data):
                result = rec.Result()
                result = json.loads(result)
                if result is not None:
                    item = result['text']
                    break

        if item:  # Verifica se o item não está vazio
            task.append(item)  # Adiciona a tarefa à lista
            print(f'Tarefa adicionada: {item} \n')
        else:
            print("Não foi possível adicionar a tarefa. Tente novamente. \n")
            continue  # Volta ao início do loop

        time.sleep(5)

        print('Deseja continuar adicionando itens a lista? \n')
        continuar = speak('Deseja continuar adicionando itens a lista?') #Pergunta se o usuário quer continuar adicionando itens a lista

        # Aguarda a resposta do usuário
        while True:
            data = stream.read(2048, exception_on_overflow=False)
            if rec.AcceptWaveform(data):
                result = rec.Result()
                result = json.loads(result)
                if result is not None:
                    continuar = result['text']
                    break

        if continuar == 'sim':
             continue
        time.sleep(5)
        if continuar == 'não': 
             break
        print(f'Lista de tarefas Atualizada {task} \n')
        speak(f'Lista de tarefas Atualizada: {task}') #Exibe a lista de tarefas atualizada
        break
     
# Função para buscar na web
def buscar_web():
    while True:
        speak('O que você gostaria de buscar na web?')

        # Aguarda a resposta do usuário
        result = None  # Inicializa a variável result
        while True:
            data = stream.read(2048, exception_on_overflow=False)
            if rec.AcceptWaveform(data):
                result = rec.Result()
                result = json.loads(result)
                break  # Sai do loop quando obtém uma resposta válida

        if result is not None and 'text' in result:
            busca = result['text']
            print(f"Você quer buscar: {busca}")

            # Codifica o texto da busca para uso em URLs
            busca_codificada = urllib.parse.quote(busca)
            url = f'https://www.google.com/search?q={busca_codificada}'
            
            # Abre a URL no navegador
            webbrowser.open(url)
            speak(f'Aqui estão os resultados da busca para {busca}')
            break  # Sai do loop após realizar a busca
        else:
            speak('Não entendi o que você quer buscar. Por favor, tente novamente.')

def reminder():
    speak('Diga o que quer que eu te lembre?')

    # Aguarda a resposta do usuário
    data = stream.read(2048, exception_on_overflow=False)
    if rec.AcceptWaveform(data):
        result = rec.Result()
        result = json.loads(result)
        if result is not None:
            lembrete = result['text']
        else:
            speak('Não entendi o lembrete. Por favor, tente novamente.')
            return

    speak('Que dia e que horas quer que te lembre?')

    # Aguarda a resposta do usuário
    data = stream.read(2048, exception_on_overflow=False)
    if rec.AcceptWaveform(data):
        result = rec.Result()
        result = json.loads(result)
        if result is not None:
            data_str = result['text']
        else:
            speak('Não entendi a data e hora. Por favor, tente novamente.')
            return

    # Converter a string de data/hora para um objeto datetime
    try:
        reminder_time = datetime.datetime.strptime(data_str, '%d/%m/%Y %H:%M')
    except ValueError:
        speak('Formato de data e hora inválido. Por favor, use o formato DD/MM/AAAA HH:MM.')
        return

    # Agora você pode usar `lembrete` e `reminder_time` para configurar o lembrete
    speak(f'Lembrete configurado: {lembrete} para {reminder_time.strftime("%d/%m/%Y %H:%M")}')

        
#Loop do reconhecimento de fala

while True:
    data = stream.read(2048, exception_on_overflow=False)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        result = rec.Result()
        result = json.loads(result)
    
        if result is not None:
            text = result['text']

            print(text)

        if text == None:
            engine.runAndWait()

        if text == 'me diga as horas' or text == 'que horas são':
            speak(hora_atual)
            print(f"A hora atual é: ", hora_atual)

        if text == 'lista de tarefas' or text == 'Abrir a lista':
             print('Abrindo lista de tarefas')
             speak('Abrindo lista de tarefas')
             add_task()

        if text == 'buscar na web' or text == 'busca na web':
             print('Buscando na web')
             speak('Buscando na web')
             buscar_web()

        if text == 'lembrete' or text == 'lembretes':
            print('Configurando lembrete')
            speak('Configurando lembrete')
            reminder()


             