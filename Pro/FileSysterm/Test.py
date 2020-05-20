from FileSysterm import File


def Test():
    print("Check __init__ ...")
    _file = File('PCreditCard.py', '/Users/Angold4/WorkSpace/algorithms_in_python/Chapters/Chapter_2')
    print("Finished")
    print('')

    print("Check get_filename() and get_filepath() ...")
    _name = _file.get_filename()
    _path = _file.get_filepath()
    print("Name:", _name, "Path:", _path)
    print("Finished")
    print('')

    print("Check get_content()...")
    _content = _file.get_content()
    print(_content)
    print("Finished!")
    print('')

    print("Check get_lines()...")
    _lines = _file.get_lines()
    print("Lines:", _lines)
    print("Finished")
    print('')

    print("Check count_letter()...")
    _n = _file.count_letter('p')
    print("Number of p:", _n)
    print("Finished")
    print('')

    print("Check count_word()...")
    _n = _file.count_word('print')
    print("Number of print:", _n)
    print("Finished")
    print('')

    print("Check count_letters()...")
    print(_file.count_letters(True))
    print("Finished")
    print('')

    print("Check count_words()...")
    print(_file.count_words(True))
    print("Finished")
    print('')


Test()
