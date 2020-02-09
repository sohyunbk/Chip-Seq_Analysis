import os, sys, glob


for sBamfiles in glob.glob("./3.Bowtie/*.sam"):
	FileName = os.path.split(sBamfiles)[1]
	Outfile_sam = "./4.UniqueReads/"+FileName.replace("_bowtie2_algn.sam","_unique_bowtie2_algn.sam")
	Outfile_bam = "./4.UniqueReads/"+FileName.replace("_bowtie2_algn.sam","_unique_bowtie2_algn.bam")	
	
	cmd1 = 'grep -E "@|NM:" %s | grep -v "XS:" > %s'%(sBamfiles,Outfile_sam)
        cmd2 = 'samtools sort %s > %s -@ 14'%(Outfile_sam,Outfile_bam)
	
	print(cmd1)
	os.system(cmd1)

	os.system("module load SAMtools/1.9-foss-2016b")
	print(cmd2)
	os.system(cmd2)	
