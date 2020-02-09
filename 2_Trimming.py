import os,sys

os.system("module load Trimmomatic/0.36-Java-1.8.0_144")

def Trimm(FileList,MinLen):
	
	for sFiles in FileList:
		print(sFiles)
		Infile = "/scratch/sb14489/3.ChipSeq/1.RawData_Input/"+sFiles
		Outfile = "/scratch/sb14489/3.ChipSeq/2.Trimmomatic_log/"+sFiles.replace(".fastq.gz","_Trimmed.fastq.gz")
		Logfile = "/scratch/sb14489/3.ChipSeq/2.Trimmomatic_log/"+sFiles.replace(".fastq.gz","_Trimmed.log")

		cmd = "java -jar /usr/local/apps/eb/Trimmomatic/0.36-Java-1.8.0_144/trimmomatic-0.36.jar \
       SE -threads 24  -phred33 %s %s \
       ILLUMINACLIP:/scratch/sb14489/3.ChipSeq/2.Trimmomatic/adapter.fa:2:30:10 \
       LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:%s 2> %s"%(Infile,Outfile,MinLen,Logfile)
		print(cmd)
		os.system(cmd)


Read76bpList = ["Sb_H3K36_S6_R1_001.fastq.gz",
"Sb_H3K41_S5_R1_001.fastq.gz",
"sorghum_V2_leaf_input_S15_R1_001.fastq.gz",
"sorghum_V2_leaf_rep1_H3K4me3_S15_R1_001.fastq.gz",
"sorghum_V2_leaf_rep2_H3K4me3_S5_R1_001.fastq.gz",
"sorghum_V2_leaf_rep1_H3K56ac_S12_R1_001.fastq.gz",
"sorghum_V2_leaf_rep2_H3K56ac_S15_R1_001.fastq.gz"]
Trimm(Read76bpList,36)

Read36bpList = ["SBL_input_S7_001.fastq.gz"]

Trimm(Read36bpList,23)
