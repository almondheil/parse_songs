# parse_songs

I'm helping with tech for a rocky horror shadow cast, one thing that I want is a list of timestamps for where songs and important scenes happen.

## Usage

Write timestamps in a yaml file (see "File format" below), then:

```bash
uv run parse_songs.py path/to/timestamps.yaml
```

It will print:

- timestamps for each song identified with a `START` and `END` event
- a pretty list of timestamps for the whole range, including songs

## Installing

I used uv, so you can `uv run parse_songs.py` and it will do the dependencies for the project.

The actual dependencies I wanted are in `pyproject.toml`, so you can install them some other way. That's allowed

## File format

I took my notes in a YAML format that looks like this:

```yaml
timestamps:
  # 'time': event
  - '0:29': example standalone event
  # to mark a song, use a `START` and `END` event with the same title
  - '1:15': START example song
  # you can put events in the middle of a song
  - '1:55': events can go in the middle of a song
  - '2:50': END example song
  # I don't care how the times are formatted. just put them in sequential order
  - '1:00:03': example of something that has an hour component
```

The file is also in this repo because I might as well track it. Good file history doesn't hurt
