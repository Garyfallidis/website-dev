import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.customization import homogeneize_latex_encoding


def remove_chars(s, chars='{}'):
    for c in chars:
        s.strip(c)
    return s


fbib = 'scilBibTex_20150310.bib'
fmybib = 'mybib.rst'

with open(fbib) as bibfile:
    parser = BibTexParser()
    parser.customization = homogeneize_latex_encoding
    bib_database = bibtexparser.load(bibfile, parser=parser)
    #print(bib_database.entries)


rst_str = ""

fobj = open(fmybib, 'w+')

buff = ""

cnt = 0

for entry in bib_database.entries:


    print(entry)

    try:

        if entry['author'].lower().find('garyfallidis') >= 0:

            print(entry)

            cnt += 1 

            template = '.. ' + str(cnt) + ' ' + entry['author'] 

            if entry['type'].find('article') >=0:
                publication = entry['journal']
            if entry['type'].find('inproceedings') >=0:
                publication = entry['booktitle']
            if entry['type'].find('phd') >=0 :
                publication = 'PhD Thesis'      

            template += ' ' + entry['title'] + ' ' + publication + ' ' + entry['year']

            template += ' \n\n'

            buff += template

    except KeyError:
        pass

fobj.write(buff)

fobj.close()


