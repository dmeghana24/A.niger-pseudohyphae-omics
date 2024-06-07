
import os
import subprocess
import glob

def run_fastqc(input_dir, output_dir):
    fastqs = glob.glob(f"{input_dir}/*.fastq.gz")
    for fq in fastqs:
        subprocess.run(["fastqc", fq, "-o", output_dir])

def run_trimmomatic(fq1, fq2, out1, out2):
    cmd = [
        "trimmomatic", "PE", fq1, fq2, out1, "/dev/null", out2, "/dev/null",
        "ILLUMINACLIP:TruSeq3-PE.fa:2:30:10", "LEADING:3", "TRAILING:3",
        "SLIDINGWINDOW:4:15", "MINLEN:36"
    ]
    subprocess.run(cmd)

if __name__ == "__main__":
    run_fastqc("../data/raw/", "../data/processed/fastqc/")
    # Add trim commands as needed
