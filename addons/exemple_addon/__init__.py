# Full Addon class. Not copy this. gulysh_lib have a simple template for you 
# You can see what is a Addon

# Это полный класс аддона. Не копируйте это. gulysh_lib имеет простой шаблон для вас
# Пока. что вы можете видеть, что такое аддон

class AddonExemple():
    """
    Addon structure for exemple
    """
    def __init__(self) -> None:


        # Init module dependence 

        self.pre_init()

        # Required Fields
        # Обязательные поля 

        self.addon_path = ""
        self.user_input_interface = [] # void -> str
        self.user_translate_interface = [] # str -> str

        self.ai_chat_interface = [] # str -> str
        self.ai_translate_interface = [] # str -> str
        self.ai_voice_interface = [] # str -> print(), play_voice()

        # Init interfaces
        # Здесь происходит вызов инициализации модулей интерфейсов 

        self.init_interfaces()

    def pre_init():
        pass

    # Definition of justification method
    # Определяю метод инициализации 
    
    def init_interfaces(self):

        # Add Modules Interface
        # Добавляю модули интерфейсов 
          
        @self.add_Interface("Input Exemple", "user_input_interface")
        def user_input_interface_exemple() -> str:
            return input("Write to Neuro: ")
        
        def translate(text, targetlang) -> str:
            # Translate realisation
            # text = translate.text
            return text

        @self.add_Interface("User Translate Exemple")
        def user_translate_interface_exemple(text, targetlang="") -> str:
            return translate(text, targetlang)

        
        @self.add_Interface("AI Translate Exemple")
        def ai_translate_interface_exemple(text, targetlang="") -> str:
            return translate(text, targetlang)
        
        
        @self.add_Interface("AI Chat Exemple")
        def ai_chat_interface_exemple(text) -> str:
            # AI chat realisation
            # response = request("POST", text)
            # text = response['data']['answer'] 
            return text
        
        @self.add_Interface("AI Voice Exemple")
        def ai_voice_interface_exemple(text) -> None:
            # Voice chat realisations
            print(text) 
            # response = request("POST", text)
            # audio = response['data']['audio'] 
            # audio.play_voice()


    def add_Interface(self, interface_name:str="", interface_type:str=""):
        def decorator(meth):
            def wrapper():
                match interface_type:
                    case "user_input_interface" | "uii":
                        self.user_input_interface.append([interface_name, meth])
                    case "user_translate_interface" | "uti":
                        self.user_translate_interface.append([interface_name, meth])
                    
                    case "ai_chat_interface" | "aci":
                        self.ai_chat_interface.append([interface_name, meth])
                    case "ai_translate_interface" | "ati":
                        self.ai_translate_interface.append([interface_name, meth])
                    case "ai_voice_interface" | "avi":
                        self.ai_voice_interface.append([interface_name, meth])         
            wrapper()
        return decorator
    


# It's better to use a template and override the methods: init_interfaces и pre_init
# Лучше воспользуйтесь шаблоном и переопределите методы: init_interfaces и pre_init

from gulysh_lib.addon_lib import AddonTemplate

class Addon_Simple_Use_Template(AddonTemplate):
    def __init__(self) -> None:
        super().__init__()
        self.addon_path="addons/exemple_addon"

    def pre_init(self):
        pass

    # Overriding the initialization for interface modules
    # Переопределяю метод инициализации модулей интерфейсов

    def init_interfaces(self): 

        # Add Modules Interface
        # Добавляю модули интерфейсов

        @self.add_Interface("Input Exemple", "user_input_interface")
        def user_input_interface_exemple() -> str:
            return input("Write to Neuro: ")
        ...

# Addon initialization function
# Функция инициализации аддона
        
def load_addon() -> AddonExemple:
    return Addon_Simple_Use_Template() # Your Addon Class




