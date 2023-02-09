import openai
import PySimpleGUI as sg
import pyperclip

# Adicione sua chave de API aqui
openai.api_key = "SUA API"

# Defina o modelo a ser usado
model_engine = "text-davinci-003"

def buscar(prompt):
    global res
    try:
        response = openai.Completion.create(
        engine=model_engine,
        prompt= prompt,
        max_tokens=1024,
        temperature=0.5
        )
        res = response['choices'][0]['text']
        values['Output1'] = print(f'Prompt: {prompt}.')
        values['Output1'] = print(res)
    except:
        response = openai.Completion.create(
        engine=model_engine,
        prompt= prompt,
        max_tokens=1024,
        temperature=0.5
        )
        res = response['choices'][0]['text']
        values['Output1'] = print(f'Prompt: {prompt}.')
        values['Output1'] = print(res)

def main():
    sg.theme("Dark Blue")

    layout = [
              [sg.Text('GERADOR DE PLR')],
              [sg.Output(size=(75,15), key='Output1', text_color='white')],
              [sg.Checkbox("Criativo", key="criativo"),
                sg.Checkbox("Detalhado", key="detalhado")],
              [sg.Button('Copiar saida')],
              [sg.Combo(values=['Gerar ideias de livro sobre:',
                                'Gerar introdução de um livro sobre:',
                                'Gerar de capítulos de um livro sobre:',
                                'Gerar tópicos de um livro sobre:',
                                'Gerar conteúdo de um tópico sobre:'],
                                size=(30, 1), default_value='Gerar ideias de livro sobre:', key='opcoes'),
                                sg.Input(key='prompt', text_color='white', size=20), sg.Button('Enviar')],
             ]
    
    return sg.Window('Gerador de PLR', layout, finalize=True, resizable=True)

window = main()

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Enviar':
        criativo = values['criativo']
        detalhado = values['detalhado']
        opcoes = values['opcoes'] #opcoes de gerador
        
        if opcoes == 'Gerar ideias de livro sobre:':
            if criativo == True and detalhado == False:
                prompt = (f'Gere ideias de titulos criativos de um livros sobre {values["prompt"]}')
                buscar(prompt)
            elif detalhado == True and criativo == False:
                prompt = (f'Gere ideias detalhadas de titulos de um livros sobre {values["prompt"]}')
                buscar(prompt)
            elif criativo == True and detalhado == True:
                prompt = (f'Gere ideias criativas e detalhadas de livros sobre {values["prompt"]}')
                buscar(prompt)
            elif criativo == False and detalhado == False:
                prompt = (f'Gere ideias de livros sobre {values["prompt"]}')
                buscar(prompt)
        elif opcoes == 'Gerar introdução de um livro sobre:':
            if criativo == True and detalhado == False:
                prompt = (f'Gere uma introdução criativa de um livro sobre {values["prompt"]}')
                buscar(prompt)
            elif detalhado == True and criativo == False:
                prompt = (f'Gere uma introdução detalhada de um livros sobre {values["prompt"]}')
                buscar(prompt)
            elif criativo == True and detalhado == True:
                prompt = (f'Gere uma introdução criativa e detalhada de livro sobre {values["prompt"]}')
                buscar(prompt)
            elif criativo == False and detalhado == False:
                prompt = (f'Gere uma introdução de um livro sobre {values["prompt"]}')
                buscar(prompt)
        elif opcoes == 'Gerar capítulos de um livro sobre:':
            if criativo == True and detalhado == False:
                prompt = (f'Gere capítulos criativos de um livro sobre {values["prompt"]}')
                buscar(prompt)
            elif detalhado == True and criativo == False:
                prompt = (f'Gere capítulos detalhados de um livro sobre {values["prompt"]}')
                buscar(prompt)
            elif criativo == True and detalhado == True:
                prompt = (f'Gere capítulos criativos e detalhados de livros sobre {values["prompt"]}')
                buscar(prompt)
            elif criativo == False and detalhado == False:
                prompt = (f'Gere capítulos de livros sobre {values["prompt"]}')
                buscar(prompt)
        elif opcoes == 'Gerar tópicos de um livro sobre:':
            if criativo == True and detalhado == False:
                prompt = (f'Gere tópicos criativos de um livros sobre {values["prompt"]}')
                buscar(prompt)
            elif detalhado == True and criativo == False:
                prompt = (f'Gere tópicos detalhados de um livros sobre {values["prompt"]}')
                buscar(prompt)
            elif criativo == True and detalhado == True:
                prompt = (f'Gere tópicos criativos e detalhados de livros sobre {values["prompt"]}')
                buscar(prompt)
            elif criativo == False and detalhado == False:
                prompt = (f'Gere tópicos de livros sobre {values["prompt"]}')
                buscar(prompt)
        elif opcoes == 'Gerar conteúdo de um tópico sobre:':
            if criativo == True and detalhado == False:
                prompt = (f'Gere um texto criativo e sem direitos autorais de um tópico intitulado de {values["prompt"]}')
                buscar(prompt)
            elif detalhado == True and criativo == False:
                prompt = (f'Gere um texto detalhado e sem direitos autorais de um tópico intitulado de {values["prompt"]}')
                buscar(prompt)
            elif criativo == True and detalhado == True:
                prompt = (f'Gere um texto criativo, detalhado e sem direitos autorais de um tópico intitulado de {values["prompt"]}')
                buscar(prompt)
            elif criativo == False and detalhado == False:
                prompt = (f'Gere um texto sem direitos autorais de um tópico intitulado de {values["prompt"]}')
                buscar(prompt)
        
    elif event == 'Copiar saida':
        pyperclip.copy(res)
