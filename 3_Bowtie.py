import os,sys, glob

os.system("module load Bowtie2/2.3.4.1-foss-2016b")

for sFiles in glob.glob("/scratch/sb14489/3.ChipSeq/2.Trimmomatic/*_Trimmed*"):
	print(sFiles)
	FileName = os.path.split(sFiles)[1]
	Outfile = "/scratch/sb14489/3.ChipSeq/3.Bowtie/"+FileName.replace("_Trimmed.fastq.gz","_bowtie2_algn.sam")
	Logfile = "/scratch/sb14489/3.ChipSeq/3.Bowtie/"+FileName.replace("_Trimmed.fastq.gz",".log")
	cmd = "bowtie2 -x /scratch/sb14489/3.ChipSeq/0.Reference/Sbicolor_454_v3.0.1 -U %s -S %s -p 24 2> %s"%(sFiles,Outfile,Logfile)
	print(cmd)
	os.system(cmd)

