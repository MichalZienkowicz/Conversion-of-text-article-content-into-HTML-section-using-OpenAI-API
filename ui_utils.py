class UserInterface:

    def __init__(self):
        self.successful_save_message = ("File generated and saved successfully!")
    
    def display_app_info(self, key_folder_name, article_folder_name):
        print(f"Application for generating the article content in HTML format to be injected to <body></body> code section, based on provided text content. Using the OpenAI API. For the application to work properly, the OpenAI API key must be stored in a .txt file located in the {key_folder_name}, and .txt file containing the content of an article must be located in {article_folder_name} - both have to be the only .txt files present in folder. \n© Michał Zienkowicz, 2024. All rights reserved.\n")

    def display_successful_save_message(self):
        print(self.successful_save_message)