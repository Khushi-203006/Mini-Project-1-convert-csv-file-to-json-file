import argparse

def parse_args():
    parser = argparse.ArgumentParser(description = "Modularize.ipynb")
    parser.add_argument('--source_dir',required = True, help = 'Source directory containing input files.')
    parser.add_argument('--output_format', required = True, choices = ['csv','json'], help = 'Output format')
    return parser.parse_args()

args = parse_args()
print(f'Source: {args.source_dir}, Format: {args.output_format}')
