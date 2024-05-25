# Donald Duck Pocket Parser

As a kid, I absolutely adored
[https://shop.donaldduck.nl/categorie/pockets](these) Dutch comics. As an
adult, I love to re-explore these comics and feel the nostalgia that comes with
it. Having recently gotten my hands on an almost complete collection of `.cbr`
files of Donald Duck Pockets, I was suddenly in need of a tool that could
filter and rename these files, for doing this manually for 300 files would be
painful.

### A synopsis

The `.cbr` files come in the form of a directory of files with the following format:
```
Donald Duck Pocket - <series-number> - <title> [(Prop)].cbr
```

The filenames are well structured and consistent between files, so the structure is taken as assumption in the script. There can be multiple files per series, these then come with different props at the end, examples:

```
Donald Duck Pocket - 001 - Title.cbr
Donald Duck Pocket - 001 - Title (Bewerkt).cbr
```

My observation is that the files with `(Bewerkt)` in it, are of better quality, thus these are preferred.

The preferred file is copied to a new directory stated in the script, and is renamed to a standard format.
