# Conversion-of-text-article-content-into-HTML-section-using-OpenAI-API
An application for generating HTML code section (the inside of the &lt;body> &lt;/body>) based on content of an article provided in .txt file. Model gpt-4o is used.

## How to use the app:
### Preparing environment
1. Download the repository
2. Insert single text file with desired content of the article into Article_content_folder
3. Insert your private OpenAI API key as a text file into API_key_folder

Structure of your documents should look as fallows:
```
Your Directory/
├── main.py
├── ui_utils.py
├── file_utils.py
├── api_utils.py
├── Article_content_folder/
     └── example_article_content.txt
├── API_key_folder/
     └── example_api_key.txt
```
   
### 2. Using the app
To use the appliaction run the main.py file.

The message:

"Application for generating the article content in HTML format to be injected to <body></body> code section, based on d on provided text content. Using the OpenAI API. For the application to work properly, the OpenAI API key must be stored in a .txt file located in the API_key_folder, and .txt file containing the content of an article must ocn 
be located in Article_content_folder - both have to be the only .txt files present in folder. © Michał Zienkowicz, 2024. All rights reserved." 

should be displayed.

If generation runs succesfully, you will receive 
"File article.html generated and saved successfully!"
message, and new file named artyklu.html will be generated in the directory where file_utils.py is located, which should be in the same directory as main.py.
```
Your Directory/
├── artykul.html
├── main.py
├── ui_utils.py
├── file_utils.py
├── api_utils.py
├── Article_content_folder/
     └── example_article_content.txt
├── API_key_folder/
     └── example_api_key.txt
```
You can then insert the content of artykul.html file into &lt;body> &lt;/body> section of your HTML file.
