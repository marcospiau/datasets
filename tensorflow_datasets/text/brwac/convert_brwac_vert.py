from brwac_utils import parse_vert_file
import json
import more_itertools
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

if __name__ == '__main__':
  parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
  parser.add_argument(
      '--input_file', type=str, required=True, help='Input file'
  )
  parser.add_argument(
      '--output_file', type=str, required=True, help='Output file'
  )
  parser.add_argument(
      '--output_format',
      type=str,
      default='json',
      choices=['json', 'txt'],
      help='Output format. `json` saves entire document '
      'structure, `txt` saves only text of paragraphs '
      '(joined with spaces")'
  )
  parser.add_argument(
      '--notqdm', action='store_true', help='Hide tqdm progress bar.'
  )

  args = parser.parse_args()

  with open(args.output_file, 'w', encoding='utf8') as fout:
    for doc in parse_vert_file(
        path=args.input_file, show_progress=not (args.notqdm)
    ):
      if args.output_format == 'json':
        to_write = json.dumps(doc)
      else:
        to_write = ' '.join(more_itertools.flatten(doc['text']['paragraphs']))
      fout.write(to_write + '\n')
      del to_write
