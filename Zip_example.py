import zipfile
import os
#при запуске программы создаются две папки - my_folder и extracted_folder, если они еще не существуют в текущей директории. Далее в папке my_folder создается текстовый файл sample.txt
#с предопределенным текстом. Файлы из папки my_folder, включая созданный текстовый файл, сжимаются в ZIP-архив compressed.zip с использованием модуля zipfile. Содержимое архива compressed.zip
#извлекается в папку extracted_folder с помощью функции extract_zip. В консоли выводится список файлов внутри архива compressed.zip с помощью функции list_files_in_zip.
def create_folders():
    # Создание папок для примера
    folders = ['my_folder', 'extracted_folder']
    for folder in folders:
        if not os.path.exists(folder):
            os.makedirs(folder)

def create_text_file(file_path, text):
    # Создание текстового файла с заданным текстом
    with open(file_path, 'w') as file:
        file.write(text)

def compress_files(folder_path, output_zip):
    # Создание текстового файла
    text_file_path = os.path.join(folder_path, 'example_file.txt')
    create_text_file(text_file_path, "Какой-то текст в текстовом файле для архива")

    # Создание нового архива ZIP
    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Обход всех файлов в указанной папке и добавление их в архив
        for foldername, subfolders, filenames in os.walk(folder_path):
            for filename in filenames:
                file_path = os.path.join(foldername, filename)
                # Добавление файла в архив с сохранением структуры папок
                zipf.write(file_path, os.path.relpath(file_path, folder_path))

def extract_zip(zip_file, extract_folder):
    # Распаковка содержимого ZIP-архива
    with zipfile.ZipFile(zip_file, 'r') as zipf:
        # Извлечение всех файлов из архива в указанную папку
        zipf.extractall(extract_folder)

def list_files_in_zip(zip_file):
    # Вывод содержимого ZIP-архива в консоль
    with zipfile.ZipFile(zip_file, 'r') as zipf:
        print(f"Содержимое архива '{zip_file}':")
        for file_info in zipf.infolist():
            print(file_info.filename)


create_folders()

compress_files('my_folder', 'compressed.zip')

extract_zip('compressed.zip', 'extracted_folder')

list_files_in_zip('compressed.zip')
