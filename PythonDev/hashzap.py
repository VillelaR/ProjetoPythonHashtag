# título: Hashzap
# botão de iniciar Chat
    # popup (janela na frente da tela)
    # título: Bem vindo ao Hashzap
    # campo de texto -> Escreva seu nome no chat
    # botão: Entrar no chat
        # sumir com o título Hashzap
        #sumir com o botão "Iniciar chat"
        # fechar a janela popup
        # carregar o chat
            # as mensagens que já foram enviadas (chat)
            # campo: Digite sua mensagem
            # Botão de Enviar
# instalar o flet

# toda a vez que for importar o flet terá que usar estas 3 funções

# importar o flet
import flet as ft

    # 1. criar função principal do seu app
def main(pagina): # def(definir) = função 
    # 2. criar todas as funcionalidades
    
    #criar o elemento
    titulo = ft.Text("Hashzap")

    titulo_janela = ft.Text("Bem vindo ao Hashzap")
    campo_nome_usuario = ft.TextField(label="Escreva seu nome no chat")

    chat = ft.Column()

    def enviar_mensagem_tunel(mensagem): # para que duas paginas no browser consigam se conversar entre si
        texto_chat = ft.Text(mensagem) # esta linha irá fazer com que o campo da mensagem deixe o texto dinamico
        chat.controls.append(texto_chat)
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(evento):
        texto_mensagem = campo_mensagem.value # isso vai fazer com que o codigo armazene as informações do usuário
        nome_usuario = campo_nome_usuario.value # isso faz com que depois de armazenar no codigo ele exiba no site a/as mensagens escritas pelos usuários
        mensagem = f"{nome_usuario}: {texto_mensagem}" 
        pagina.pubsub.send_all(mensagem) # fazer o tunel de comunição funcionar 
        campo_mensagem.value = ""
        pagina.update()

    campo_mensagem = ft.TextField(label="Digite sau mensagem", on_submit=enviar_mensagem)
    botao_enviar_mensagem = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)

    linha_mensagem = ft.Row([campo_mensagem, botao_enviar_mensagem])

    def entrar_chat(evento):
        pagina.remove(titulo)
        pagina.remove(botao_iniciar)
        janela.open = False
        pagina.add(chat)
        pagina.add(linha_mensagem)
        mensagem = f"{campo_nome_usuario.value} entrou no chat"
        pagina.pubsub.send_all(mensagem)
        pagina.update()


    botao_entrar = ft.ElevatedButton("Entrar no chat", on_click=entrar_chat)
    janela = ft.AlertDialog(title=titulo_janela,
                            content=campo_nome_usuario,
                            actions=[botao_entrar]) # toda a lista no python tem que estar em colchetes

    # cria o elemento
    def iniciar_chat(evento):
        pagina.dialog = janela
        janela.open = True
        pagina.update()

    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=iniciar_chat)

    # adiciona o elemento a página
    pagina.add(titulo)
    pagina.add(botao_iniciar)

#ft.FilePicker - para o usuario conseguir enviar um arquivo

# 3. rodar o seu app
ft.app(main, view=ft.WEB_BROWSER) # para parar a interação com o browser usar Ctrl + C