# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/01_interface.ipynb.

# %% auto 0
__all__ = ['UserInterface']

# %% ../nbs/01_interface.ipynb 3
from fastcore.all import *
from .chat import Chat
from .session_handler import SessionHandler

# %% ../nbs/01_interface.ipynb 7
class UserInterface:
  """An interface that simply passes all input on to the appropriate classes."""
  def __init__(self): 
    self.handler = SessionHandler()
    self.handler.start_app()
    

  def menu(self):
    print("Welcome to the chat interface. Type 'quit' to exit.")
    print("0 – Settings")
    print("1 – Start Chat")
    print("2 – Previous Chats")
    print("3 – Exit")

    while True:
      choice = input('... ')
      if   choice == '0': self.settings()
      elif choice == '1': self.handler.start_chat()
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
    
    if   choice == '0': self.handler.set_api_key()
    elif choice == '1': self.handler.set_model()
    elif choice == '2': pass
    else							: print('Invalid choice.')
  
  def save_chat(self): pass
    
  
  def previous_chats(self): pass

