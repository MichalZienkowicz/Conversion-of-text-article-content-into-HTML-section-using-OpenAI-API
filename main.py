from ui_utils import UserInterface 
from file_utils import FileManager, save_file
from api_utils import generate_html_from_text

def main():

    article_name = "artykul.html"
    article_folder_name = "Article_content_folder"
    api_folder_name = "API_key_folder"
    article_fm = FileManager(folder_name = article_folder_name)
    api_fm = FileManager(folder_name = api_folder_name)
    ui = UserInterface()
    
    ui.display_app_info(api_folder_name, article_folder_name)

    # Read article content from provided path
    article_content = article_fm.read_single_text_file()

    # Read the OpenAI API key
    api_key = api_fm.read_single_text_file()

    html_content = generate_html_from_text(api_key, article_content)

    save_file(article_name, html_content)
    ui.display_successful_save_message()


if __name__ == "__main__":
    main()
