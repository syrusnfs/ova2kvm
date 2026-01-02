#!/usr/bin/env python3

import tarfile
import subprocess
import os
import shutil
import sys

BANNER = r"""
 ██████╗ ██╗   ██╗ █████╗ ██████╗ ██╗  ██╗██╗   ██╗███╗   ███╗
██╔═══██╗██║   ██║██╔══██╗╚════██╗██║ ██╔╝██║   ██║████╗ ████║
██║   ██║██║   ██║███████║ █████╔╝█████╔╝ ██║   ██║██╔████╔██║
██║   ██║╚██╗ ██╔╝██╔══██║██╔═══╝ ██╔═██╗ ╚██╗ ██╔╝██║╚██╔╝██║
╚██████╔╝ ╚████╔╝ ██║  ██║███████╗██║  ██╗ ╚████╔╝ ██║ ╚═╝ ██║
 ╚═════╝   ╚═══╝  ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚═╝     ╚═╝   
           OVA2KVM Multi Image Converter | by Syrus
"""

def extract_vmdks(ova_path):
    temp_dir = "./temp_ova_extracted"
    os.makedirs(temp_dir, exist_ok=True)
    try:
        with tarfile.open(ova_path, 'r') as tar:
            tar.extractall(path=temp_dir)
    except:
        return []

    vmdk_files = []
    for root, dirs, files in os.walk(temp_dir):
        for file in files:
            if file.endswith(".vmdk"):
                vmdk_files.append(os.path.join(root, file))
    return vmdk_files

def convert_vmdk_to_qcow2(vmdk_file, qcow2_file):
    try:
        subprocess.run(
            ["qemu-img", "convert", "-f", "vmdk", "-O", "qcow2", vmdk_file, qcow2_file],
            check=True
        )
        print(f"[SUCCESS] Converted: {qcow2_file}")
    except subprocess.CalledProcessError:
        print(f"[ERROR] Conversion failed: {vmdk_file}")

def clean_temp():
    shutil.rmtree("./temp_ova_extracted", ignore_errors=True)

def single_conversion():
    ova_path = input("Enter the full path of the OVA file: ").strip()
    if not os.path.isfile(ova_path):
        print(f"[ERROR] File {ova_path} does not exist.")
        return
    output_folder = input("Enter the folder to save QCOW2 files: ").strip()
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    vmdks = extract_vmdks(ova_path)
    if not vmdks:
        print("[ERROR] No VMDK files found in the OVA.")
        return

    for i, vmdk in enumerate(vmdks, start=1):
        base_name = os.path.splitext(os.path.basename(ova_path))[0]
        qcow2_file = os.path.join(output_folder, f"{base_name}_disk{i}.qcow2")
        convert_vmdk_to_qcow2(vmdk, qcow2_file)

    if input("Remove temporary files? (y/n): ").strip().lower() == 'y':
        clean_temp()

def multiple_conversion():
    folder_path = input("Enter the folder path containing OVAs: ").strip()
    if not os.path.isdir(folder_path):
        print(f"[ERROR] Folder {folder_path} does not exist.")
        return
    output_folder = input("Enter the folder path to save QCOW2s: ").strip()
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    ova_files = [f for f in os.listdir(folder_path) if f.endswith(".ova")]
    if not ova_files:
        print("[ERROR] No OVA files found in the folder.")
        return

    for ova in ova_files:
        ova_path = os.path.join(folder_path, ova)
        print(f"\n[INFO] Processing: {ova_path}")
        vmdks = extract_vmdks(ova_path)
        if not vmdks:
            print("[ERROR] No VMDK files found, skipping...")
            continue
        for i, vmdk in enumerate(vmdks, start=1):
            base_name = os.path.splitext(ova)[0]
            qcow2_file = os.path.join(output_folder, f"{base_name}_disk{i}.qcow2")
            convert_vmdk_to_qcow2(vmdk, qcow2_file)

    if input("Remove temporary files? (y/n): ").strip().lower() == 'y':
        clean_temp()

def main_menu():
    while True:
        print("\n===== OVA2KVM MENU =====\n")
        print("1 - Convert single image (all disks in OVA)")
        print("2 - Convert multiple images in folder")
        print("0 - Exit\n")
        choice = input("Select an option: ").strip()
        if choice == '1':
            single_conversion()
        elif choice == '2':
            multiple_conversion()
        elif choice == '0':
            sys.exit(0)
        else:
            print("[ERROR] Invalid option. Try again.")

if __name__ == "__main__":
    print(BANNER)
    main_menu()
