""" @Author(s): Andrea Failla
    @VersionID: 2.0
    @LastUpdated: 13 apr 2021, 14:09:26
"""

import sys, argparse

def convert(input, output):
    text = ''
    with open(input, 'r', encoding = "utf8") as fhand:
        text = fhand.readlines()
    
    for line in text: # cicla il testo
        newline = ""
        if line.startswith("#"): # se la linea inizia con #...
            for char in line:
                if char == ' ': # ...ne sostituisce gli spazi con un underscore...
                    char = '_'
                newline += char
            output.write(newline) # ...la scrive...
            continue # ...e passa alla linea successiva
        
        if "-" in line[0:3]: 
            newline += "'" # (questo controllo per evitare che MS Excel converta i numeri in date)
        for char in line:  
            if char == ' ':
                char = '\t' # ...converte gli spazi in tabulazioni...
            newline += char
        output.write(newline) # ... e la scrive 
    print('Done!')


def main(argv):
    parser = argparse.ArgumentParser(description='Conllu format to tsv converter')
    parser.add_argument('input', help='your input file')
    parser.add_argument("output", action='store', 
                    type=argparse.FileType('a'), default=sys.stdout,
                    help="Directs the output to a name of your choice")
    
    args = parser.parse_args()
    
    convert(args.input, args.output)


if __name__ == "__main__":
    main(sys.argv)