from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.clock import Clock
from chat_bot_terminal.chatbot_groq import initialize_chatbot, generate_response  # Importa as funções do chatbot

gui = Builder.load_file("chat_bot_terminal\\window.kv")

class ChatWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.llm_chain = None  # Inicializa a variável com None
        try:
            self.llm_chain = initialize_chatbot()  # Inicializa o chatbot
            if not self.llm_chain:
                if not self.llm_chain:
                    error_message_label = Label(
                        text="Erro ao inicializar o chatbot. Tente novamente mais tarde.",
                        size_hint_y=None,
                        height=30,
                        color=(1, 1, 1, 1)
                    )
                    self.ids.messages_layout.add_widget(error_message_label)
                    self.ids.scroll_view.scroll_to(error_message_label)
                    
        except Exception as e:
            print(f"Erro ao inicializar o chatbot: {e}")

    def send_message(self, instance):
        user_input = str(self.ids.input_field.text).strip()
        if user_input:
            # Exibe a mensagem do usuário imediatamente
            self.show_user_message(user_input)
            
            # Limpa o campo de entrada
            self.ids.input_field.text = ''
            
            # Faz o scroll automático
            self.ids.scroll_view.scroll_to(self.ids.messages_layout.children[0])
            
            # Simula um atraso para gerar a resposta do chatbot
            Clock.schedule_once(lambda dt: self.show_assistant_response(user_input), 1)

    def show_user_message(self, user_input):
        user_message_label = Label(
            text=f'Você: {user_input}',
            size_hint_y=None,
            halign='right',
            valign='middle',
            text_size=(self.width - 20, None),
            padding=(10, 10),
            color=(1, 1, 1, 1)
        )
        user_message_label.bind(
            texture_size=lambda instance, value: setattr(user_message_label, 'height', value[1])
        )
        self.ids.messages_layout.add_widget(user_message_label)

    def show_assistant_response(self, user_input):
        if self.llm_chain:
            response = generate_response(user_input, self.llm_chain)
        else:
            response = "Erro: Não foi possível gerar a resposta."
        
        assistant_message_label = Label(
            text=f"Assistente: {response}",
            size_hint_y=None,
            halign='left',
            valign='middle',
            text_size=(self.width - 20, None),
            padding=(10, 10),
            color=(1, 1, 1, 1)
        )
        assistant_message_label.bind(
            texture_size=lambda instance, value: setattr(assistant_message_label, 'height', value[1])
        )
        self.ids.messages_layout.add_widget(assistant_message_label)
        self.ids.scroll_view.scroll_to(assistant_message_label)


class ChatApp(App):
    def build(self):
        return ChatWindow()

