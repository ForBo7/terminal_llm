# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/01_interface.ipynb.

# %% auto 0
__all__ = ['UserInterface']

# %% ../nbs/01_interface.ipynb 3
from .chat import Chat

# %% ../nbs/01_interface.ipynb 4
class UserInterface:
    def __init__(self, api_key, model): self.chat = Chat(api_key, model)
    
    def start_app(self): pass

    def menu(self):
      # TODO: Implement first time check.
      print("Welcome to the chat interface. Type 'quit' to exit.")
      print("0 – Settings")
      print("1 – Start Chat")
      print("2 – Previous Chats")
      print("3 – Exit")

      while True:
        choice = input('... ')
        if   choice == '0': self.settings()
        elif choice == '1': self.start_chat()
        elif choice == '2': self.previous_chats()
        elif choice == '3': break
        else              : print('Invalid choice.')
                
        # TODO: Implement full processing on exit term.
        # if user_input.lower() == 'quit': break
        # response = self.chat(user_input)
        # print(f"Assistant: {response}")

    def settings(self):
        print("Settings")
        print("0 – Change API Key")
        print("1 – Change Model")
        print("2 – Back")
        choice = input('... ')
        match choice:
          case '0': self.change_api_key()
          case '1': self.change_model()
          case '2': pass
          case  _ : print('Invalid choice.')
    
    def start_chat(self):
        print("Start Chat")
        while True:
          user_input = input('... ')
          if user_input.lower() == 'quit': break
          response = self.chat(user_input)
          print(f"Assistant: {response}")
    
    def previous_chats(self):
        print("Previous Chats")
        pass

