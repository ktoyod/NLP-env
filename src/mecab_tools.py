import MeCab


def mecab_parser(sys_dic_path=None, user_dic_path=None):
    if sys_dic_path and user_dic_path:
        mecab = MeCab.Tagger(f'-d {sys_dic_path} -u {user_dic_path}')
    elif sys_dic_path:
        mecab = MeCab.Tagger(f'-d {sys_dic_path}')
    elif user_dic_path:
        mecab = MeCab.Tagger(f'-u {user_dic_path}')
    else:
        mecab = MeCab.Tagger
    mecab.parse('')

    return mecab
