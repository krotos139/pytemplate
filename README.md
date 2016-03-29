# pytemplate - Программа заполнения данных в документы из различных источников

Программа позволяет создавать документы в текстовом формате (включая latex, xetex, и др.) или ODF форматах используя шаблоны и наборы данных.

Программа представляет из себя утилиту, не имеющая интерактивного интерфейса с пользователем. Предназначена для использования в составе скриптов.

Программа использует язык шаблонов Jinja2, расширенный новыми командами, для загрузки данных из различных источников.

Поддерживаемые источники данных:
* CSV таблица (Может быть отредактирована в Exel при соблюдении определенных правил)
* XML документ
* Текстовый файл
* SQLite база данных
* Функция MD5 от файла
* Функция получения данных о файле

# Дополнительные функции для загрузки данных

## load_xml
Позволяет загружать древовидные данные из XML файла
Принимает аргумент - имя файла
Возращает - root element
Пример использования:
```
    {%- set root = load_xml("database1.xml") %}
    {%- for item in root.findall("hardware/i") %}
    {{ item.find("name").text }} & {{ item.find("sign").text }} / {{ item.find("version").text }} & {{ item.find("fullname").text }} \\\hline
    {%- endfor %}
```

## load_csv
Позволяет загружать табличные данные из CSV файла
Принимает аргумент - имя файла
Возращает - итератор
Пример использования:
```
    {%- set docs = load_csv("database2.csv")  %}
    {%- for item in docs %}
    {{ item.id }} & {{ item.name }} & {{ item.ref }} & {{ item.sign }} & {{ item.inv }} \\\hline
    {%- endfor %}
```

## load_sqlite
Позволяет загружать данные из SQLite базы данных
Принимает аргумент - имя файла
Возращает - курсор
Пример использования:
```
    {%- set db = load_sqlite("database3.sqlite") %}
    {%- set alboum = db.execute("select * from Album") %}
    {%- for item in alboum %}
    {{ item[0] }} & {{ le(item[1]) }} \\\hline
    {%- endfor %}
```

## load_text
Позволяет загружать текстовые данные из файла
Принимает аргумент - имя файла
Возращает - строку
Пример использования:
```
    {%- set content = load_text("database4.txt") %}
    {{ content }}
```

## file_md5
Позволяет подсчитать контрольную сумму файла
Принимает аргумент - имя файла
Возращает - строку
Пример использования:
```
    {%- set md5 = file_md5(sourcefile) %}
    {{md5}}
```

## file_stat
Позволяет получить информацию о файле (размер)
Принимает аргумент - имя файла
Возращает - объект, содержащий следующие поля:
* st_mode - protection bits,
* st_ino - inode number,
* st_dev - device,
* st_nlink - number of hard links,
* st_uid - user id of owner,
* st_gid - group id of owner,
* st_size - size of file, in bytes,
* st_atime - time of most recent access,
* st_mtime - time of most recent content modification,
* st_ctime - platform dependent; time of most recent metadata change on Unix, or the time of creation on Windows)
* st_blocks - number of 512-byte blocks allocated for file
* st_blksize - filesystem blocksize for efficient file system I/O
* st_rdev - type of device if an inode device
* st_flags - user defined flags for file
* st_gen - file generation number
* st_birthtime - time of file creation
* st_ftype (file type)
* st_attrs (attributes)
* st_obtype (object type).
Пример использования:
```
    {%- set stat = file_stat(sourcefile) %}
    {{ stat.st_size }}
```

## log
Позволяет выводить сообщения в консоль при разборе шаблона
Принимает аргумент - строка
Пример использования:
```
    {%- do log("Add alboum %s (authorid=%d)" % (item[1], item[2])) %}
```

## getargs
Позволяет получить аргументы запуска из командной строки
Возвращает значение - сущность, описанная на python в параметре "arg"

# Запуск программы
Usage: pytemplate.py [options]
Опции:
* --version 
Отобразить версию
* -h, --help
Отобразить информацию о ключах запуска
* -t TEMPLATE, --template=TEMPLATE 
Указать путь до файла шаблона
* -o OUTPUT, --output=OUTPUT
Указать путь до выходного файла
* -f FORMAT, --format=FORMAT
Формат файла шаблона, может принимать значения (odt и text)
* -a ARG, --arg=ARG
Дополнительная сущность для шаблона

# Примеры сгенерированных документов:
* Latex document: [IN](/examples/out_doc1.tex) + [IN 1](/examples/out_doc1_part1.template.tex) + [IN 2](/examples/out_doc1_part2.template.tex) + [IN 3](/examples/out_doc1_part3.template.tex) + [IN 4](/examples/out_doc1_part4.template.tex) + [IN 5](/examples/out_doc1_part5.template.tex) -> [OUT](/examples/output/out_doc1.pdf)
* ODT document: [IN](/examples/out_doc2.odt) -> [OUT](/examples/output/out_doc2_ready.odt)
