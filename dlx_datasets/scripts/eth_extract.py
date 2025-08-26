"""This script creates a JSON file with data extracted from the libray
catalogue. Once the dlx-datasets package is installed in a Python virtual
environment, the script can be run as a CLI command as follows:

`eth-extract --help`
"""

import json
from argparse import ArgumentParser
from bson import Regex
from dlx import DB
from dlx.marc import BibSet
from dlx.file import File, Identifier

def get_args():
    parser = ArgumentParser()
    parser.add_argument('--connect', help='Database connection string', required=True)
    parser.add_argument('--database', help='Database name', required=True)
    parser.add_argument('--output', help='Path to write the JSON output file to', required=True)

    return parser.parse_args()

def run():
    args = get_args()
    DB.connect(args.connect, database=args.database)
    
    q = {
        '_record_type': 'default', # no votes or speeches
        '269.subfields.value': Regex('^2'), # publication date > 2000
        '$or': [
            {'191.subfields': {'$elemMatch': {'code': 'a', 'value': Regex(r'^S/(PV\.|RES/|PRST/)')}}},
            {
                '$and': [
                    {'191.subfields': {'$elemMatch': {'code': 'a', 'value': Regex('^S/')}}},
                    {'989.subfields.value': 'Letters and Notes Verbales'}
                ]
            }
        ]
    }

    print('Executing query...')
    all_data, i, started = [], 1, False

    for bib in BibSet.from_query(q):
        if started is False:
            print('Records scanned:')
            started = True

        symbol = bib.get_value('191', 'a')
        file = File.latest_by_identifier_language(Identifier('symbol', symbol), 'EN')

        # extract the wanted data
        doc = {
            'symbol': symbol,
            'title': ' '.join(bib.get_values('245', 'a', 'b', 'c')),
            'date': bib.get_value('269', 'a'),
            'subjects': bib.get_values('650', 'a'),
            'types': bib.get_values('989'),
            'data_url': f'https://metadata.un.org/editor/api/marc/bibs/records/{bib.id}',
            'file_url': f'https://metadata.un.org/editor/api/files/{file.id}' if file else None,
            #'file_text': file.text if file else None,
        }
        all_data.append(doc)

        #status
        print(('\b' * (len(str(i)))) + str(i), end='', flush=True)
        symbol = bib.get_value('191', 'a')
        i += 1

    with open(args.output, 'w') as f:
        f.write(json.dumps(all_data))

    return

###

if __name__ == '__main__':
    run()