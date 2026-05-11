# Gerador de Ideias de Jogos (Python + Flask)

Este é um projeto prático desenvolvido por Alisson Guarniêr como tarefa para a seleção de Tutores da Kodland para o curso de Python Pro. O objetivo principal desta aplicação web é inspirar alunos a criarem seus próprios jogos, gerando combinações aleatórias de temas, mecânicas e objetivos de forma dinâmica.

## Funcionalidades

- **Geração Aleatória:** Utiliza a biblioteca integrada `random` do Python para criar combinações únicas de ideias de jogos.
- **Interface Web:** Uma página interativa e estilizada renderizada pelo Flask, demonstrando como o Python pode atuar no back-end de um site.
- **Botão de Atualização:** Permite que o usuário gere infinitas novas ideias com um único clique.

## Tecnologias Utilizadas

- **Python**
- **Flask** (Microframework Web, incluindo o uso de `url_for` para arquivos estáticos)
- **HTML/CSS** (Para a interface visual e personalização com a logo da Kodland)

## Como executar o projeto

1. **Clone ou faça o download deste repositório.**
   Certifique-se de que todos os arquivos estejam na mesma pasta.

2. **Crie um Ambiente Virtual (Opcional, mas recomendado):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows use: venv\Scripts\activate
   ```
3. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Execute a aplicação:**

   ```bash
   python app.py
   ```

5. **Acesse no navegador:**
   Abra o endereço `http://127.0.0.1:5000` para ver o gerador em funcionamento.
