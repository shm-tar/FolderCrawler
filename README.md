# FolderCrawler
A script to delete all files with matching extension (`*.png`) from numerous folders inside a directory.
## How it works
Let's assume you have a following directory tree:
```bash
├── dir
│   ├── dir1
│   │   ├── photo1.png
│   │   └── file1.txt
│   ├── dir2
│   │   ├── photo2.png
│   │   ├── photo3.png
│   │   └── file2.txt
│   ├── dir3
│   │   ├── photo4.png
│   │   └── file3.bin
...
```
If you have ~1000 folders inside `dir` directory and need to delete only `*.png` files from every folder inside (all other files are left untouched), the script comes handy and saves tons of time.
