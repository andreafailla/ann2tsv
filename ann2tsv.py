""" @Author(s): Andrea Failla
    @VersionID: 2.0
    @LastUpdated: 13 apr 2021, 14:09:26
"""

import sys, argparse, os

def tsv_file(x):
    ext = os.path.splitext(x)[1]
    if ext.lower() != '.tsv':
        raise argparse.ArgumentTypeError('Output file must end in .tsv')
    return x

def convert(input, output):
    text = ''
    with open(input, 'r', encoding = "utf8") as fhand:
        text = fhand.readlines()
    out = open(output, 'a')
    
    for line in text: 
        newline = ""
        if line.startswith("#"): 
            for char in line:
                if char == ' ': 
                    char = '_'
                newline += char
            out.write(newline) 
            continue 
        
        if "-" in line[0:3]: 
            newline += "'" # prevents MS Excel from converting numbers to dates
        for char in line:  
            if char == ' ':
                char = '\t' 
            newline += char
        out.write(newline) 
    out.close()
    print('Done!')

def main(argv):
    parser = argparse.ArgumentParser(description='Conllu format to tsv converter')
    parser.add_argument('input', help='your input file')
    parser.add_argument("output", action='store', 
                    type=tsv_file, default=sys.stdout,
                    help="Directs the output to a name of your choice")
    
    args = parser.parse_args()
    
    convert(args.input, args.output)


if __name__ == "__main__":
    main(sys.argv)