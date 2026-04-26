import sys
from argparse import ArgumentParser

import yaml

def only_songs(timestamp_list):
    songs = dict()

    for ts in timestamp_list:
        (time, event) = next(iter(ts.items()))

        if event.startswith('START '):
            title = event[6:]
            if title in songs:
                print(f"error: start of song '{title}' found twice", file=sys.stderr)
                exit(1)
            songs[title] = [time, None]
        elif event.startswith('END '):
            title = event[4:]
            if title not in songs:
                print(f"error: end of song '{title}' found without start", file=sys.stderr)
                exit(1)
            songs[title][1] = time

    print('only songs:')
    for title in songs:
        if songs[title][1] == None:
            print(f"error: no end of song '{title}' found", file=sys.stderr)
            exit(1)

        duration = songs[title]
        print(f'  {title}: {duration[0]}-{duration[1]}')

def all_things(timestamp_list):
    print('all items in the list:')
    for ts in timestamp_list:
        (time, event) = next(iter(ts.items()))
        print(f'  {time:>7} - {event}')


def main():
    parser = ArgumentParser()
    parser.add_argument('filename', help='Path to YAML file with `timestamps` list')
    args = parser.parse_args()

    with open(args.filename, 'r') as infile:
        data = yaml.safe_load(infile)

    only_songs(data['timestamps'])
    print()
    all_things(data['timestamps'])

if __name__ == "__main__":
    main()
