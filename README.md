 ██████╗ ██╗   ██╗ █████╗ ██████╗ ██╗  ██╗██╗   ██╗███╗   ███╗
██╔═══██╗██║   ██║██╔══██╗╚════██╗██║ ██╔╝██║   ██║████╗ ████║
██║   ██║██║   ██║███████║ █████╔╝█████╔╝ ██║   ██║██╔████╔██║
██║   ██║╚██╗ ██╔╝██╔══██║██╔═══╝ ██╔═██╗ ╚██╗ ██╔╝██║╚██╔╝██║
╚██████╔╝ ╚████╔╝ ██║  ██║███████╗██║  ██╗ ╚████╔╝ ██║ ╚═╝ ██║
 ╚═════╝   ╚═══╝  ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚═╝     ╚═╝   

Simple Python tool to convert virtual machines from `.ova` format (VMware/VirtualBox) to `.qcow2` format (KVM/QEMU). Supports single or batch conversion.

## Features

- **Single Conversion:** Convert a specific `.ova` file.
- **Batch Conversion:** Convert all `.ova` files present in a folder.
- **Automatic Extraction:** Extracts `.vmdk` disks from within the `.ova` package.
- **Cleanup:** Option to remove temporary files after conversion.

## Prerequisites

- Python 3
- `qemu-utils` (for the `qemu-img` command)

### Dependency Installation (Linux)

```bash
sudo apt update
sudo apt install qemu-utils python3
```

## How to Use

1. Clone this repository or download the script.
```bash
git clone https://github.com/syrusnfs/ova2kvm.git
```

2. Run the tool:
```bash
python3 ova2kvm.py
```

## Menu

Upon starting, you will see the following options:

1. **Convert single image:** Select a single `.ova` file to convert.
2. **Convert multiple images:** Select a folder containing multiple `.ova` files to convert them all at once.
0. **Exit:** Exit the tool.

## Author
Syrus
