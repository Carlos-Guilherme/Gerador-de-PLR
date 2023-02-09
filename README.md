# Gerador-de-PLR

Este é um programa que usa a biblioteca PySimpleGUI e a API OpenAI para gerar ideias e conteúdo para um livro. O usuário pode escolher entre diferentes opções de geração de conteúdo, como ideias de títulos, introdução, capítulos e tópicos. Além disso, o usuário pode escolher se quer o conteúdo gerado de forma criativa ou detalhada.

A interface gráfica do programa é construída com o PySimpleGUI e inclui uma janela com opções de seleção para o tipo de conteúdo a ser gerado, opções de criatividade e detalhamento e um campo de entrada para o assunto sobre o qual o livro será escrito.

Ao clicar no botão "Enviar", o programa envia uma solicitação à API OpenAI com o prompt especificado pelo usuário. O prompt é construído com base nas opções selecionadas pelo usuário e no assunto escolhido. A API responde com o conteúdo gerado, que é exibido na janela do programa. O usuário também pode copiar o conteúdo gerado para a área de transferência clicando no botão "Copiar saída".

Este programa é uma ferramenta útil para escritores que precisam de ajuda para gerar ideias e conteúdo para seus livros. Com a combinação da API OpenAI e da biblioteca PySimpleGUI, o programa fornece uma solução fácil de usar para a geração de conteúdo de livros.

É necessário fazer a instalação das seguintes bibliotecas: PySimpleGUI, openai e pyperclip
