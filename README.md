# Luna 1.0
 # Assistente Virtual Luna

A **Luna** é uma assistente virtual desenvolvida em Python, capaz de realizar tarefas básicas como informar a hora, gerenciar listas de tarefas e realizar buscas na web. Este projeto utiliza tecnologias de reconhecimento de fala e síntese de voz para proporcionar uma interação natural com o usuário.

## Funcionalidades

A Luna possui as seguintes funcionalidades:

1. **Informar a hora atual:**
   - Basta dizer "me diga as horas" ou "que horas são" para que a Luna informe a hora atual.

2. **Gerenciar lista de tarefas:**
   - A Luna pode criar e gerenciar uma lista de tarefas. Diga "lista de tarefas" ou "abrir a lista" para adicionar tarefas à lista.
   - A assistente perguntará qual tarefa deseja adicionar e se deseja continuar adicionando mais itens.

3. **Buscar na web:**
   - A Luna pode realizar buscas na web utilizando o Google. Diga "buscar na web" ou "busca na web" para iniciar uma busca.
   - A assistente perguntará o que você deseja buscar e abrirá os resultados no navegador.

## Tecnologias Utilizadas

- **Reconhecimento de fala:** Utiliza a biblioteca [Vosk](https://alphacephei.com/vosk/) para reconhecer comandos de voz.
- **Síntese de voz:** Utiliza a biblioteca [pyttsx3](https://pyttsx3.readthedocs.io/) para converter texto em fala.
- **Captura de áudio:** Utiliza a biblioteca [PyAudio](https://pypi.org/project/PyAudio/) para capturar áudio do microfone.
- **Integração com navegador:** Utiliza a biblioteca [webbrowser](https://docs.python.org/3/library/webbrowser.html) para abrir URLs no navegador padrão.

## Como Executar o Projeto

### Pré-requisitos

1. **Python 3.x:** Certifique-se de ter o Python instalado em sua máquina.
2. **Bibliotecas necessárias:** Instale as bibliotecas utilizadas no projeto executando o seguinte comando:
   ```bash
   pip install vosk pyaudio pyttsx3

   ## Como Executar a Luna

### Passo 1: Clone o repositório do projeto

Primeiro, clone o repositório do projeto para o seu computador:

```bash
git clone https://github.com/seu-usuario/luna-assistente.git
cd luna-assistente

### Passo 2: Configure o caminho do modelo Vosk

Certifique-se de que o caminho para o modelo de linguagem Vosk está correto no arquivo principal (`main.py`). Substitua `'caminho/para/pasta/model'` pelo caminho absoluto da pasta onde está o modelo baixado.

```python
model_path = 'caminho/para/pasta/model'

### Passo 3: Execute o arquivo principal

Por fim, execute o arquivo principal para iniciar a Luna:

```bash
python main.py

A Luna iniciará e estará pronta para receber comandos de voz. Fale claramente e utilize os comandos disponíveis para interagir com a assistente.