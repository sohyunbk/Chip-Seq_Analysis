import os, sys, glob

os.system("ml PeakRanger/1.18")

def run_bcp_broad(Chip_mod,Control):
	Chip_mod_file = "./4.UniqueReads/"+Chip_mod 
	Control_file =  "./4.UniqueReads/"+Control
	Output_file = "./5.PeakCalling/"+Chip_mod.replace("_unique_bowtie2_algn.bam","_peaks_broad")	
	Log_file = "./5.PeakCalling/"+Chip_mod.replace("_unique_bowtie2_algn.bam","_peaks_broad_region.log")
	cmd = "peakranger bcp --format bam --verbose --pval .001 --data %s --control %s\
    	--output %s &> %s"%(Chip_mod_file,Control_file,Output_file,Log_file)
	print(cmd)
	os.system(cmd)

def run_bcp_narrow(Chip_mod,Control):
        Chip_mod_file = "./4.UniqueReads/"+Chip_mod
        Control_file =  "./4.UniqueReads/"+Control
        Output_file = "./5.PeakCalling/"+Chip_mod.replace("_unique_bowtie2_algn.bam","_peaks_narrow")
        Log_file = "./5.PeakCalling/"+Chip_mod.replace("_unique_bowtie2_algn.bam","_peaks_narrow_region.log")
        cmd = "peakranger ranger  --format bam  --ext_length 250  --verbose\
    --pval .001  --data %s  --control %s  --output %s &> %s"%(Chip_mod_file,Control_file,Output_file,Log_file)

        print(cmd)
        os.system(cmd)




run_bcp_broad("Sb_H3K36_S6_R1_001_unique_bowtie2_algn.bam","SBL_input_S7_001_unique_bowtie2_algn.bam")
run_bcp_broad("Sb_H3K41_S5_R1_001_unique_bowtie2_algn.bam","SBL_input_S7_001_unique_bowtie2_algn.bam")

run_bcp_narrow("sorghum_V2_leaf_rep1_H3K4me3_S15_R1_001_unique_bowtie2_algn.bam","sorghum_V2_leaf_input_S15_R1_001_unique_bowtie2_algn.bam")
run_bcp_narrow("sorghum_V2_leaf_rep2_H3K4me3_S5_R1_001_unique_bowtie2_algn.bam","sorghum_V2_leaf_input_S15_R1_001_unique_bowtie2_algn.bam")
run_bcp_narrow("sorghum_V2_leaf_rep1_H3K56ac_S12_R1_001_unique_bowtie2_algn.bam","sorghum_V2_leaf_input_S15_R1_001_unique_bowtie2_algn.bam")
run_bcp_narrow("sorghum_V2_leaf_rep2_H3K56ac_S15_R1_001_unique_bowtie2_algn.bam","sorghum_V2_leaf_input_S15_R1_001_unique_bowtie2_algn.bam")
