"""
Method 3:
Counting the Motif occurrence from BAM files using our script bellow, the idea is checking the alignment CIGAR string and store all candidate Indel which are close sgRNA sequence. 
The combination indel location and sequence content (Insertion/deletion) are unique.
"""
import pysam
# parse CIGAR string for indels and store them in a dictionary
def extract_indels_with_insertion_content(bam_file):
    indel_dict = {}
    with pysam.AlignmentFile(bam_file, "rb") as bam:
        # Iterate through each read in the BAM file
        for read in bam:
            # Check if the read has a valid CIGAR string
            if read.cigartuples is None:
                continue  # Skip reads with no CIGAR string
            ref_pos = read.reference_start  # Starting position on the reference
            query_pos = 0  # Position in the read sequence
            
            # Parse the CIGAR string, using CRISPRnano, minimap2 conventional indel code
            for cigar_tuple in read.cigartuples:
                cigar_op, length = cigar_tuple
                
                # Check for insertion (CIGAR op 1) or deletion (CIGAR op 2)
                if cigar_op == 1:  # Insertion
                    # Extract the inserted sequence from the read
                    inserted_sequence = read.query_sequence[query_pos:query_pos + length]
                    
                    # Store the insertion information with reference position as the key
                    if ref_pos not in indel_dict:
                        indel_dict[ref_pos] = []  # Initialize list if key doesn't exist
                    
                    # Append the insertion info, including the sequence
                    indel_dict[ref_pos].append({
                        'type': 'insertion',
                        'size': length,
                        'sequence': inserted_sequence
                    })
                
                elif cigar_op == 2:  # Deletion
                    # Store the deletion information
                    if ref_pos not in indel_dict:
                        indel_dict[ref_pos] = []  # Initialize list if key doesn't exist
                    
                    # Append the deletion info (no sequence for deletions)
                    indel_dict[ref_pos].append({
                        'type': 'deletion',
                        'size': length
                    })
                
                # Update positions based on the CIGAR operation
                if cigar_op == 1:  # Insertion
                    query_pos += length  
                elif cigar_op == 2:  # Deletion
                    ref_pos += length  
                else:
                    ref_pos += length  
                    query_pos += length  # Move forward in the read sequence
    
    return indel_dict

#Test, using our test_indel.bam
bam_file = 'test_indel.bam'  
indel_dict = extract_indels_with_insertion_content(bam_file)