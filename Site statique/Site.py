# coding=utf-8
import argparse
import markdown2
import os 
import re

convertiseur = argparse.ArgumentParser(description= 'Markdown vers Html')
convertiseur.add_argument("-i", '--input_directory', type=str, help='Markdown ver Html')
convertiseur.add_argument("-o", '--output_directory', type = str, help = 'Html en site statique')
link_patterns = [(re.compile(r'((([A-Za-z]{3,9}:(?:\/\/)?)(?:[\-;:&=\+\$,\w]+@)?[A-Za-z0-9\.\-]+(:[0-9]+)?|(?:www\.|[\-;:&=\+\$,\w]+@)[A-Za-z0-9\.\-]+)((?:\/[\+~%\/\.\w\-_]*)?\??(?:[\-\+=&;%@\.\w_]*)#?(?:[\.\!\/\\\w]*))?)'),r'\1')]

args = convertiseur.parse_args ()



def md_html():
       dossier_md = os.listdir(args.input_file)
       for fichier in dossier_md:
        with open(args.input_file + '/' + fichier, 'r+', encoding = 'utf-8') as fichier_md:
            HTML = markdown2.markdown(fichier_md.read())
            html1 = open(args.output_file + '/' + fichier.replace('.md', ".html"), "w+", encoding="utf-8")
            html1.write(HTML)
md_html()
   